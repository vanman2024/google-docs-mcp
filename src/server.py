#!/usr/bin/env python3
"""Google Docs MCP Server - FastMCP v3 for document creation and editing.

Supports two credential modes:
  - Cloud (Horizon): Set GOOGLE_DOCS_TOKEN_JSON env var with the OAuth token JSON
  - Local: Uses file-based OAuth flow via ~/.config/mcp-gdrive/
"""

import os
import json
import base64
from typing import Optional

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse

SCOPES = ['https://www.googleapis.com/auth/documents']

mcp = FastMCP(
    "Google Docs",
    instructions="Use these tools to create, read, edit, and format Google Docs. "
    "Tools are tagged: 'read' for reading, 'write' for inserting/appending, "
    "'format' for styling, 'table' for table operations, 'delete' for destructive actions.",
    on_duplicate="warn",
    mask_error_details=True,
)

_creds: Optional[Credentials] = None


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: StarletteRequest):
    return JSONResponse({"status": "healthy", "server": "google-docs-mcp"})


def get_credentials():
    """Get or refresh Google OAuth credentials.

    Priority:
      1. GOOGLE_DOCS_TOKEN_JSON env var (for cloud/Horizon deployment)
      2. File-based token at GDRIVE_CREDS_DIR (for local development)
    """
    global _creds
    if _creds and _creds.valid:
        return _creds

    if _creds and _creds.expired and _creds.refresh_token:
        _creds.refresh(Request())
        return _creds

    creds = None

    token_json = os.getenv('GOOGLE_DOCS_TOKEN_JSON')
    if token_json:
        try:
            token_data = json.loads(token_json)
        except json.JSONDecodeError:
            token_data = json.loads(base64.b64decode(token_json).decode())
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
        if not creds.valid and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        _creds = creds
        return creds

    creds_dir = os.getenv('GDRIVE_CREDS_DIR', os.path.expanduser('~/.config/mcp-gdrive'))
    token_file = os.path.join(creds_dir, 'docs-token.json')
    credentials_file = os.path.join(creds_dir, 'gcp-oauth.keys.json')

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)

        os.makedirs(creds_dir, exist_ok=True)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    _creds = creds
    return creds


def _get_service():
    return build('docs', 'v1', credentials=get_credentials())


# --- Document CRUD ---

@mcp.tool(
    tags={"write", "create"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_create(title: str) -> dict:
    """Create a new Google Doc. Returns the document ID and title."""
    service = _get_service()
    doc = service.documents().create(body={'title': title}).execute()
    return {'documentId': doc['documentId'], 'title': doc['title']}


@mcp.tool(
    tags={"read"},
    timeout=30.0,
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
def docs_read(document_id: str) -> str:
    """Read all text content from a Google Doc."""
    service = _get_service()
    doc = service.documents().get(documentId=document_id).execute()

    content = doc.get('body', {}).get('content', [])
    text = []
    for element in content:
        if 'paragraph' in element:
            for text_element in element['paragraph'].get('elements', []):
                if 'textRun' in text_element:
                    text.append(text_element['textRun']['content'])

    return ''.join(text)


@mcp.tool(
    tags={"write"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_insert_text(document_id: str, text: str, index: int = 1) -> dict:
    """Insert text at a specific position (default: 1, after title)."""
    service = _get_service()
    requests = [{'insertText': {'location': {'index': index}, 'text': text}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"write"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_append_text(document_id: str, text: str) -> dict:
    """Append text to the end of a document."""
    service = _get_service()
    doc = service.documents().get(documentId=document_id).execute()
    end_index = doc.get('body', {}).get('content', [{}])[-1].get('endIndex', 1)

    requests = [{'insertText': {'location': {'index': end_index - 1}, 'text': text}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


# --- Text Formatting ---

@mcp.tool(
    tags={"format"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
def docs_format_text(
    document_id: str,
    start_index: int,
    end_index: int,
    bold: Optional[bool] = None,
    italic: Optional[bool] = None,
    underline: Optional[bool] = None,
    strikethrough: Optional[bool] = None,
    font_size: Optional[int] = None,
    font_family: Optional[str] = None,
    text_color: Optional[str] = None,
    background_color: Optional[str] = None
) -> dict:
    """Format a text range. Colors in hex format like #FF0000."""
    service = _get_service()

    text_style = {}
    if bold is not None:
        text_style['bold'] = bold
    if italic is not None:
        text_style['italic'] = italic
    if underline is not None:
        text_style['underline'] = underline
    if strikethrough is not None:
        text_style['strikethrough'] = strikethrough
    if font_size is not None:
        text_style['fontSize'] = {'magnitude': font_size, 'unit': 'PT'}
    if font_family is not None:
        text_style['weightedFontFamily'] = {'fontFamily': font_family}
    if text_color is not None:
        hex_color = text_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        text_style['foregroundColor'] = {'color': {'rgbColor': {'red': r, 'green': g, 'blue': b}}}
    if background_color is not None:
        hex_color = background_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        text_style['backgroundColor'] = {'color': {'rgbColor': {'red': r, 'green': g, 'blue': b}}}

    if not text_style:
        raise ToolError("No formatting options specified")

    requests = [{
        'updateTextStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'textStyle': text_style,
            'fields': ','.join(text_style.keys())
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"write", "search"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_find_replace(document_id: str, find_text: str, replace_text: str) -> dict:
    """Find and replace text throughout a document. Returns number of replacements."""
    service = _get_service()

    requests = [{
        'replaceAllText': {
            'containsText': {'text': find_text, 'matchCase': False},
            'replaceText': replace_text
        }
    }]

    result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    occurrences = result.get('replies', [{}])[0].get('replaceAllText', {}).get('occurrencesChanged', 0)
    return {'replacements': occurrences, 'documentId': document_id}


# --- Paragraph Styles ---

@mcp.tool(
    tags={"format"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
def docs_set_paragraph_style(
    document_id: str,
    start_index: int,
    end_index: int,
    style: str = 'NORMAL_TEXT'
) -> dict:
    """Set paragraph style. Styles: NORMAL_TEXT, HEADING_1-6, TITLE, SUBTITLE."""
    service = _get_service()

    requests = [{
        'updateParagraphStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'paragraphStyle': {'namedStyleType': style},
            'fields': 'namedStyleType'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"format"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
def docs_set_alignment(
    document_id: str,
    start_index: int,
    end_index: int,
    alignment: str = 'START'
) -> dict:
    """Set paragraph alignment. Options: START (left), CENTER, END (right), JUSTIFIED."""
    service = _get_service()

    requests = [{
        'updateParagraphStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'paragraphStyle': {'alignment': alignment},
            'fields': 'alignment'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"format"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
def docs_set_line_spacing(
    document_id: str,
    start_index: int,
    end_index: int,
    line_spacing: float = 100.0
) -> dict:
    """Set line spacing (percentage: 100=single, 150=1.5, 200=double)."""
    service = _get_service()

    requests = [{
        'updateParagraphStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'paragraphStyle': {'lineSpacing': line_spacing},
            'fields': 'lineSpacing'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"format"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_create_list(
    document_id: str,
    start_index: int,
    end_index: int,
    list_type: str = 'bulleted'
) -> dict:
    """Create a bulleted or numbered list. list_type: 'bulleted' or 'numbered'."""
    service = _get_service()

    requests = [{
        'createParagraphBullets': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE' if list_type == 'bulleted' else 'NUMBERED_DECIMAL_ALPHA_ROMAN'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


# --- Insert Elements ---

@mcp.tool(
    tags={"write", "table"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_insert_table(document_id: str, rows: int, columns: int, index: int = 1) -> dict:
    """Insert a table at the specified position."""
    service = _get_service()
    requests = [{'insertTable': {'rows': rows, 'columns': columns, 'location': {'index': index}}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"write"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_insert_image(document_id: str, uri: str, index: int = 1) -> dict:
    """Insert an inline image from a URL."""
    service = _get_service()
    requests = [{'insertInlineImage': {'location': {'index': index}, 'uri': uri}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"write"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_insert_page_break(document_id: str, index: int = 1) -> dict:
    """Insert a page break at the specified position."""
    service = _get_service()
    requests = [{'insertPageBreak': {'location': {'index': index}}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"write", "structure"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_create_header(document_id: str, text: str) -> dict:
    """Create a document header with text."""
    service = _get_service()

    result = service.documents().batchUpdate(
        documentId=document_id,
        body={'requests': [{'createHeader': {'type': 'DEFAULT'}}]}
    ).execute()

    header_id = result['replies'][0]['createHeader']['headerId']

    service.documents().batchUpdate(
        documentId=document_id,
        body={'requests': [{'insertText': {'location': {'segmentId': header_id, 'index': 0}, 'text': text}}]}
    ).execute()

    return {'success': True, 'headerId': header_id, 'documentId': document_id}


@mcp.tool(
    tags={"write", "structure"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_create_footer(document_id: str, text: str) -> dict:
    """Create a document footer with text."""
    service = _get_service()

    result = service.documents().batchUpdate(
        documentId=document_id,
        body={'requests': [{'createFooter': {'type': 'DEFAULT'}}]}
    ).execute()

    footer_id = result['replies'][0]['createFooter']['footerId']

    service.documents().batchUpdate(
        documentId=document_id,
        body={'requests': [{'insertText': {'location': {'segmentId': footer_id, 'index': 0}, 'text': text}}]}
    ).execute()

    return {'success': True, 'footerId': footer_id, 'documentId': document_id}


# --- Table Operations ---

@mcp.tool(
    tags={"write", "table"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_insert_table_row(
    document_id: str,
    table_start_index: int,
    row_index: int,
    insert_below: bool = True
) -> dict:
    """Insert a row in a table."""
    service = _get_service()

    requests = [{
        'insertTableRow': {
            'tableCellLocation': {
                'tableStartLocation': {'index': table_start_index},
                'rowIndex': row_index,
                'columnIndex': 0
            },
            'insertBelow': insert_below
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"write", "table"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
)
def docs_insert_table_column(
    document_id: str,
    table_start_index: int,
    column_index: int,
    insert_right: bool = True
) -> dict:
    """Insert a column in a table."""
    service = _get_service()

    requests = [{
        'insertTableColumn': {
            'tableCellLocation': {
                'tableStartLocation': {'index': table_start_index},
                'rowIndex': 0,
                'columnIndex': column_index
            },
            'insertRight': insert_right
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


# --- Destructive Operations ---

@mcp.tool(
    tags={"delete"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": True, "openWorldHint": True},
)
def docs_delete_content(document_id: str, start_index: int, end_index: int) -> dict:
    """Delete a content range from a document. This is destructive."""
    service = _get_service()
    requests = [{'deleteContentRange': {'range': {'startIndex': start_index, 'endIndex': end_index}}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'deleted_chars': end_index - start_index, 'documentId': document_id}


@mcp.tool(
    tags={"delete", "table"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": True, "openWorldHint": True},
)
def docs_delete_table_row(
    document_id: str,
    table_start_index: int,
    row_index: int
) -> dict:
    """Delete a table row. This is destructive."""
    service = _get_service()

    requests = [{
        'deleteTableRow': {
            'tableCellLocation': {
                'tableStartLocation': {'index': table_start_index},
                'rowIndex': row_index,
                'columnIndex': 0
            }
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


@mcp.tool(
    tags={"delete", "table"},
    timeout=30.0,
    annotations={"readOnlyHint": False, "destructiveHint": True, "openWorldHint": True},
)
def docs_delete_table_column(
    document_id: str,
    table_start_index: int,
    column_index: int
) -> dict:
    """Delete a table column. This is destructive."""
    service = _get_service()

    requests = [{
        'deleteTableColumn': {
            'tableCellLocation': {
                'tableStartLocation': {'index': table_start_index},
                'rowIndex': 0,
                'columnIndex': column_index
            }
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return {'success': True, 'documentId': document_id}


if __name__ == "__main__":
    mcp.run()
