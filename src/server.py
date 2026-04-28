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
    instructions="Use these tools to create, read, edit, and format Google Docs.",
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

    # Try refreshing cached creds first
    if _creds and _creds.expired and _creds.refresh_token:
        _creds.refresh(Request())
        return _creds

    creds = None

    # Mode 1: Env var token (cloud/Horizon) - supports raw JSON or base64-encoded
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

    # Mode 2: File-based token (local dev)
    creds_dir = os.getenv('GDRIVE_CREDS_DIR', os.path.expanduser('~/.config/mcp-gdrive'))
    token_file = os.path.join(creds_dir, 'docs-token.json')
    credentials_file = os.path.join(creds_dir, 'gcp-oauth.keys.json')

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Browser-based flow - only works locally
            from google_auth_oauthlib.flow import InstalledAppFlow
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)

        os.makedirs(creds_dir, exist_ok=True)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    _creds = creds
    return creds


def _get_service():
    """Build the Google Docs API service."""
    return build('docs', 'v1', credentials=get_credentials())


@mcp.tool
def docs_create(title: str) -> str:
    """Create a new Google Doc"""
    service = _get_service()
    doc = service.documents().create(body={'title': title}).execute()
    return json.dumps({
        'documentId': doc['documentId'],
        'title': doc['title']
    }, indent=2)


@mcp.tool
def docs_read(document_id: str) -> str:
    """Read content from a Google Doc"""
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


@mcp.tool
def docs_insert_text(document_id: str, text: str, index: int = 1) -> str:
    """Insert text at a specific position (default: 1, after title)"""
    service = _get_service()
    requests = [{'insertText': {'location': {'index': index}, 'text': text}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True, 'documentId': document_id}, indent=2)


@mcp.tool
def docs_append_text(document_id: str, text: str) -> str:
    """Append text to the end of document"""
    service = _get_service()
    doc = service.documents().get(documentId=document_id).execute()
    end_index = doc.get('body', {}).get('content', [{}])[-1].get('endIndex', 1)

    requests = [{'insertText': {'location': {'index': end_index - 1}, 'text': text}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
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
) -> str:
    """Format text range (bold, italic, underline, strikethrough, font size, font family, colors).
    Colors should be hex format like #FF0000"""
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
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_find_replace(document_id: str, find_text: str, replace_text: str) -> str:
    """Find and replace text throughout document"""
    service = _get_service()

    requests = [{
        'replaceAllText': {
            'containsText': {'text': find_text, 'matchCase': False},
            'replaceText': replace_text
        }
    }]

    result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    occurrences = result.get('replies', [{}])[0].get('replaceAllText', {}).get('occurrencesChanged', 0)
    return json.dumps({'replacements': occurrences}, indent=2)


@mcp.tool
def docs_insert_table(document_id: str, rows: int, columns: int, index: int = 1) -> str:
    """Insert a table at specified position"""
    service = _get_service()
    requests = [{'insertTable': {'rows': rows, 'columns': columns, 'location': {'index': index}}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_set_paragraph_style(
    document_id: str,
    start_index: int,
    end_index: int,
    style: str = 'NORMAL_TEXT'
) -> str:
    """Set paragraph style for a range.
    Styles: NORMAL_TEXT, HEADING_1, HEADING_2, HEADING_3, HEADING_4, HEADING_5, HEADING_6, TITLE, SUBTITLE"""
    service = _get_service()

    requests = [{
        'updateParagraphStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'paragraphStyle': {'namedStyleType': style},
            'fields': 'namedStyleType'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_set_alignment(
    document_id: str,
    start_index: int,
    end_index: int,
    alignment: str = 'START'
) -> str:
    """Set paragraph alignment.
    Alignment options: START (left), CENTER, END (right), JUSTIFIED"""
    service = _get_service()

    requests = [{
        'updateParagraphStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'paragraphStyle': {'alignment': alignment},
            'fields': 'alignment'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_set_line_spacing(
    document_id: str,
    start_index: int,
    end_index: int,
    line_spacing: float = 100.0
) -> str:
    """Set line spacing for paragraphs (percentage, e.g., 100 = single, 150 = 1.5, 200 = double)"""
    service = _get_service()

    requests = [{
        'updateParagraphStyle': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'paragraphStyle': {'lineSpacing': line_spacing},
            'fields': 'lineSpacing'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_create_list(
    document_id: str,
    start_index: int,
    end_index: int,
    list_type: str = 'bulleted'
) -> str:
    """Create a bulleted or numbered list.
    list_type options: 'bulleted' or 'numbered'"""
    service = _get_service()

    requests = [{
        'createParagraphBullets': {
            'range': {'startIndex': start_index, 'endIndex': end_index},
            'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE' if list_type == 'bulleted' else 'NUMBERED_DECIMAL_ALPHA_ROMAN'
        }
    }]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_delete_content(document_id: str, start_index: int, end_index: int) -> str:
    """Delete content range from document"""
    service = _get_service()
    requests = [{'deleteContentRange': {'range': {'startIndex': start_index, 'endIndex': end_index}}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True, 'deleted_chars': end_index - start_index}, indent=2)


@mcp.tool
def docs_insert_image(document_id: str, uri: str, index: int = 1) -> str:
    """Insert inline image from URL"""
    service = _get_service()
    requests = [{'insertInlineImage': {'location': {'index': index}, 'uri': uri}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_insert_page_break(document_id: str, index: int = 1) -> str:
    """Insert page break at position"""
    service = _get_service()
    requests = [{'insertPageBreak': {'location': {'index': index}}}]
    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_create_header(document_id: str, text: str) -> str:
    """Create document header"""
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

    return json.dumps({'success': True, 'headerId': header_id}, indent=2)


@mcp.tool
def docs_create_footer(document_id: str, text: str) -> str:
    """Create document footer"""
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

    return json.dumps({'success': True, 'footerId': footer_id}, indent=2)


@mcp.tool
def docs_insert_table_row(
    document_id: str,
    table_start_index: int,
    row_index: int,
    insert_below: bool = True
) -> str:
    """Insert row in table"""
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
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_insert_table_column(
    document_id: str,
    table_start_index: int,
    column_index: int,
    insert_right: bool = True
) -> str:
    """Insert column in table"""
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
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_delete_table_row(
    document_id: str,
    table_start_index: int,
    row_index: int
) -> str:
    """Delete table row"""
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
    return json.dumps({'success': True}, indent=2)


@mcp.tool
def docs_delete_table_column(
    document_id: str,
    table_start_index: int,
    column_index: int
) -> str:
    """Delete table column"""
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
    return json.dumps({'success': True}, indent=2)


if __name__ == "__main__":
    mcp.run()
