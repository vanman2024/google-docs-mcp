---
name: fastmcp-docs-reference
description: 'FastMCP documentation lookup skill. Use when you need FastMCP API references, implementation guidance, or page discovery from the official llms.txt index.'
---

## Documentation Index

> Fetch the complete documentation index at: https://gofastmcp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FastMCP Docs Reference

> Build, debug, and ship FastMCP servers and clients using the official docs index included below.

This skill packages the full FastMCP llms.txt index so Claude can answer with grounded links and discoverability.

## How to Use This Skill

1. Start from the documentation index section below to find the most relevant page.
2. Prefer official docs links over memory when giving implementation guidance.
3. For coding tasks, cite the exact relevant page(s) from the index before proposing code changes.
4. If multiple pages apply, prioritize quickstart, then concept pages, then Python SDK API pages.

## Scope

- FastMCP apps, servers, clients, deployment, auth, transforms, and integrations.
- Python SDK module/page lookup.
- FastMCP CLI and installation workflows.

## Source

- Original URL: https://gofastmcp.com/llms.txt
- Snapshot date: 2026-04-28

## Full Documentation Index (Categorized)

This section reorganizes the complete FastMCP llms.txt link set into FastMCP-aligned categories for easier navigation.

- Total unique links: 357

### Getting Started

- [Installation](https://gofastmcp.com/getting-started/installation.md)
- [Quickstart](https://gofastmcp.com/getting-started/quickstart.md)
- [Upgrading from FastMCP 2](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2.md)
- [Upgrading from the MCP Low-Level SDK](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk.md)
- [Upgrading from the MCP SDK](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk.md)
- [Welcome to FastMCP](https://gofastmcp.com/getting-started/welcome.md)

### Apps - Core

- [App Architecture](https://gofastmcp.com/apps/architecture.md)
- [Apps](https://gofastmcp.com/apps/overview.md)
- [Custom HTML Apps](https://gofastmcp.com/apps/low-level.md)
- [Development](https://gofastmcp.com/apps/development.md)
- [Examples](https://gofastmcp.com/apps/examples.md)
- [FastMCPApp](https://gofastmcp.com/apps/interactive-apps.md)
- [Generative UI](https://gofastmcp.com/apps/generative.md)
- [Patterns](https://gofastmcp.com/apps/patterns.md)
- [Prefab UI](https://gofastmcp.com/apps/prefab.md)
- [Quickstart](https://gofastmcp.com/apps/quickstart.md)

### Apps - Providers

- [Approval](https://gofastmcp.com/apps/providers/approval.md)
- [Choice](https://gofastmcp.com/apps/providers/choice.md)
- [File Upload](https://gofastmcp.com/apps/providers/file-upload.md)
- [Form Input](https://gofastmcp.com/apps/providers/form.md)
- [Generative UI](https://gofastmcp.com/apps/providers/generative.md)

### Servers - Core

- [Authorization](https://gofastmcp.com/servers/authorization.md)
- [Background Tasks](https://gofastmcp.com/servers/tasks.md)
- [Client Logging](https://gofastmcp.com/servers/logging.md)
- [Component Visibility](https://gofastmcp.com/servers/visibility.md)
- [Composing Servers](https://gofastmcp.com/servers/composition.md)
- [Dependency Injection](https://gofastmcp.com/servers/dependency-injection.md)
- [Icons](https://gofastmcp.com/servers/icons.md)
- [Lifespans](https://gofastmcp.com/servers/lifespan.md)
- [MCP Context](https://gofastmcp.com/servers/context.md)
- [Middleware](https://gofastmcp.com/servers/middleware.md)
- [OpenTelemetry](https://gofastmcp.com/servers/telemetry.md)
- [Pagination](https://gofastmcp.com/servers/pagination.md)
- [Progress Reporting](https://gofastmcp.com/servers/progress.md)
- [Prompts](https://gofastmcp.com/servers/prompts.md)
- [Resources & Templates](https://gofastmcp.com/servers/resources.md)
- [Sampling](https://gofastmcp.com/servers/sampling.md)
- [Storage Backends](https://gofastmcp.com/servers/storage-backends.md)
- [Testing your FastMCP Server](https://gofastmcp.com/servers/testing.md)
- [The FastMCP Server](https://gofastmcp.com/servers/server.md)
- [Tools](https://gofastmcp.com/servers/tools.md)
- [User Elicitation](https://gofastmcp.com/servers/elicitation.md)
- [Versioning](https://gofastmcp.com/servers/versioning.md)

### Servers - Auth

- [Authentication](https://gofastmcp.com/servers/auth/authentication.md)
- [Full OAuth Server](https://gofastmcp.com/servers/auth/full-oauth-server.md)
- [Multiple Auth Sources](https://gofastmcp.com/servers/auth/multi-auth.md)
- [OAuth Proxy](https://gofastmcp.com/servers/auth/oauth-proxy.md)
- [OIDC Proxy](https://gofastmcp.com/servers/auth/oidc-proxy.md)
- [Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth.md)
- [Token Verification](https://gofastmcp.com/servers/auth/token-verification.md)

### Servers - Providers

- [Custom Providers](https://gofastmcp.com/servers/providers/custom.md)
- [Filesystem Provider](https://gofastmcp.com/servers/providers/filesystem.md)
- [Local Provider](https://gofastmcp.com/servers/providers/local.md)
- [MCP Proxy Provider](https://gofastmcp.com/servers/providers/proxy.md)
- [Providers](https://gofastmcp.com/servers/providers/overview.md)
- [Skills Provider](https://gofastmcp.com/servers/providers/skills.md)

### Servers - Transforms

- [Code Mode](https://gofastmcp.com/servers/transforms/code-mode.md)
- [Namespace Transform](https://gofastmcp.com/servers/transforms/namespace.md)
- [Prompts as Tools](https://gofastmcp.com/servers/transforms/prompts-as-tools.md)
- [Resources as Tools](https://gofastmcp.com/servers/transforms/resources-as-tools.md)
- [Tool Search](https://gofastmcp.com/servers/transforms/tool-search.md)
- [Tool Transformation](https://gofastmcp.com/servers/transforms/tool-transformation.md)
- [Transforms Overview](https://gofastmcp.com/servers/transforms/transforms.md)

### Clients - Core

- [Background Tasks](https://gofastmcp.com/clients/tasks.md)
- [Calling Tools](https://gofastmcp.com/clients/tools.md)
- [Client Roots](https://gofastmcp.com/clients/roots.md)
- [Client Transports](https://gofastmcp.com/clients/transports.md)
- [Getting Prompts](https://gofastmcp.com/clients/prompts.md)
- [LLM Sampling](https://gofastmcp.com/clients/sampling.md)
- [Notifications](https://gofastmcp.com/clients/notifications.md)
- [Progress Monitoring](https://gofastmcp.com/clients/progress.md)
- [Reading Resources](https://gofastmcp.com/clients/resources.md)
- [Server Logging](https://gofastmcp.com/clients/logging.md)
- [The FastMCP Client](https://gofastmcp.com/clients/client.md)
- [User Elicitation](https://gofastmcp.com/clients/elicitation.md)

### Clients - Authentication

- [Bearer Token Authentication](https://gofastmcp.com/clients/auth/bearer.md)
- [CIMD Authentication](https://gofastmcp.com/clients/auth/cimd.md)
- [OAuth Authentication](https://gofastmcp.com/clients/auth/oauth.md)

### CLI

- [Auth Utilities](https://gofastmcp.com/cli/auth.md)
- [CLI](https://gofastmcp.com/cli/overview.md)
- [Client Commands](https://gofastmcp.com/cli/client.md)
- [Generate CLI](https://gofastmcp.com/cli/generate-cli.md)
- [Inspecting Servers](https://gofastmcp.com/cli/inspecting.md)
- [Install MCP Servers](https://gofastmcp.com/cli/install-mcp.md)
- [Running Servers](https://gofastmcp.com/cli/running.md)

### Deployment

- [HTTP Deployment](https://gofastmcp.com/deployment/http.md)
- [Prefect Horizon](https://gofastmcp.com/deployment/prefect-horizon.md)
- [Project Configuration](https://gofastmcp.com/deployment/server-configuration.md)
- [Running Your Server](https://gofastmcp.com/deployment/running-server.md)

### Integrations - Auth

- [Auth0 OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/auth0.md)
- [AuthKit 🤝 FastMCP](https://gofastmcp.com/integrations/authkit.md)
- [AWS Cognito OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/aws-cognito.md)
- [Azure (Microsoft Entra ID) OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/azure.md)
- [Descope 🤝 FastMCP](https://gofastmcp.com/integrations/descope.md)
- [Discord OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/discord.md)
- [Eunomia Authorization 🤝 FastMCP](https://gofastmcp.com/integrations/eunomia-authorization.md)
- [GitHub OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/github.md)
- [Google OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/google.md)
- [OCI IAM OAuth 🤝 FastMCP](https://gofastmcp.com/integrations/oci.md)
- [PropelAuth 🤝 FastMCP](https://gofastmcp.com/integrations/propelauth.md)
- [Scalekit 🤝 FastMCP](https://gofastmcp.com/integrations/scalekit.md)
- [Supabase 🤝 FastMCP](https://gofastmcp.com/integrations/supabase.md)
- [WorkOS 🤝 FastMCP](https://gofastmcp.com/integrations/workos.md)

### Integrations - AI Assistants

- [ChatGPT 🤝 FastMCP](https://gofastmcp.com/integrations/chatgpt.md)
- [Claude Code 🤝 FastMCP](https://gofastmcp.com/integrations/claude-code.md)
- [Claude Desktop 🤝 FastMCP](https://gofastmcp.com/integrations/claude-desktop.md)
- [Cursor 🤝 FastMCP](https://gofastmcp.com/integrations/cursor.md)
- [Gemini CLI 🤝 FastMCP](https://gofastmcp.com/integrations/gemini-cli.md)
- [Goose 🤝 FastMCP](https://gofastmcp.com/integrations/goose.md)

### Integrations - AI SDKs and MCP Config

- [Anthropic API 🤝 FastMCP](https://gofastmcp.com/integrations/anthropic.md)
- [Gemini SDK 🤝 FastMCP](https://gofastmcp.com/integrations/gemini.md)
- [MCP JSON Configuration 🤝 FastMCP](https://gofastmcp.com/integrations/mcp-json-configuration.md)
- [OpenAI API 🤝 FastMCP](https://gofastmcp.com/integrations/openai.md)
- [OpenAPI 🤝 FastMCP](https://gofastmcp.com/integrations/openapi.md)

### Integrations - Web Frameworks

- [FastAPI 🤝 FastMCP](https://gofastmcp.com/integrations/fastapi.md)

### Integrations - Other

- [Permit.io Authorization 🤝 FastMCP](https://gofastmcp.com/integrations/permit.md)

### Development

- [Contributing](https://gofastmcp.com/development/contributing.md)
- [Releases](https://gofastmcp.com/development/releases.md)
- [Tests](https://gofastmcp.com/development/tests.md)

### Patterns

- [Contrib Modules](https://gofastmcp.com/patterns/contrib.md)

### More

- [Settings](https://gofastmcp.com/more/settings.md)

### Top-Level Pages

- [Changelog](https://gofastmcp.com/changelog.md)
- [FastMCP Updates](https://gofastmcp.com/updates.md)

## Python SDK (Categorized by Module Family)

### Python SDK - apps

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-apps-__init__.md)
- [app](https://gofastmcp.com/python-sdk/fastmcp-apps-app.md)
- [approval](https://gofastmcp.com/python-sdk/fastmcp-apps-approval.md)
- [choice](https://gofastmcp.com/python-sdk/fastmcp-apps-choice.md)
- [config](https://gofastmcp.com/python-sdk/fastmcp-apps-config.md)
- [file_upload](https://gofastmcp.com/python-sdk/fastmcp-apps-file_upload.md)
- [form](https://gofastmcp.com/python-sdk/fastmcp-apps-form.md)
- [generative](https://gofastmcp.com/python-sdk/fastmcp-apps-generative.md)

### Python SDK - cli

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-cli-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-cli-install-__init__.md)
- [apps_dev](https://gofastmcp.com/python-sdk/fastmcp-cli-apps_dev.md)
- [auth](https://gofastmcp.com/python-sdk/fastmcp-cli-auth.md)
- [cimd](https://gofastmcp.com/python-sdk/fastmcp-cli-cimd.md)
- [claude_code](https://gofastmcp.com/python-sdk/fastmcp-cli-install-claude_code.md)
- [claude_desktop](https://gofastmcp.com/python-sdk/fastmcp-cli-install-claude_desktop.md)
- [cli](https://gofastmcp.com/python-sdk/fastmcp-cli-cli.md)
- [client](https://gofastmcp.com/python-sdk/fastmcp-cli-client.md)
- [cursor](https://gofastmcp.com/python-sdk/fastmcp-cli-install-cursor.md)
- [discovery](https://gofastmcp.com/python-sdk/fastmcp-cli-discovery.md)
- [gemini_cli](https://gofastmcp.com/python-sdk/fastmcp-cli-install-gemini_cli.md)
- [generate](https://gofastmcp.com/python-sdk/fastmcp-cli-generate.md)
- [goose](https://gofastmcp.com/python-sdk/fastmcp-cli-install-goose.md)
- [mcp_json](https://gofastmcp.com/python-sdk/fastmcp-cli-install-mcp_json.md)
- [run](https://gofastmcp.com/python-sdk/fastmcp-cli-run.md)
- [shared](https://gofastmcp.com/python-sdk/fastmcp-cli-install-shared.md)
- [stdio](https://gofastmcp.com/python-sdk/fastmcp-cli-install-stdio.md)
- [tasks](https://gofastmcp.com/python-sdk/fastmcp-cli-tasks.md)

### Python SDK - client

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-client-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-client-auth-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-client-mixins-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-client-sampling-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-client-sampling-handlers-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-client-transports-__init__.md)
- [anthropic](https://gofastmcp.com/python-sdk/fastmcp-client-sampling-handlers-anthropic.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-client-transports-base.md)
- [bearer](https://gofastmcp.com/python-sdk/fastmcp-client-auth-bearer.md)
- [client](https://gofastmcp.com/python-sdk/fastmcp-client-client.md)
- [config](https://gofastmcp.com/python-sdk/fastmcp-client-transports-config.md)
- [elicitation](https://gofastmcp.com/python-sdk/fastmcp-client-elicitation.md)
- [google_genai](https://gofastmcp.com/python-sdk/fastmcp-client-sampling-handlers-google_genai.md)
- [http](https://gofastmcp.com/python-sdk/fastmcp-client-transports-http.md)
- [inference](https://gofastmcp.com/python-sdk/fastmcp-client-transports-inference.md)
- [logging](https://gofastmcp.com/python-sdk/fastmcp-client-logging.md)
- [memory](https://gofastmcp.com/python-sdk/fastmcp-client-transports-memory.md)
- [messages](https://gofastmcp.com/python-sdk/fastmcp-client-messages.md)
- [oauth](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth.md)
- [oauth_callback](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback.md)
- [openai](https://gofastmcp.com/python-sdk/fastmcp-client-sampling-handlers-openai.md)
- [progress](https://gofastmcp.com/python-sdk/fastmcp-client-progress.md)
- [prompts](https://gofastmcp.com/python-sdk/fastmcp-client-mixins-prompts.md)
- [resources](https://gofastmcp.com/python-sdk/fastmcp-client-mixins-resources.md)
- [roots](https://gofastmcp.com/python-sdk/fastmcp-client-roots.md)
- [sse](https://gofastmcp.com/python-sdk/fastmcp-client-transports-sse.md)
- [stdio](https://gofastmcp.com/python-sdk/fastmcp-client-transports-stdio.md)
- [task_management](https://gofastmcp.com/python-sdk/fastmcp-client-mixins-task_management.md)
- [tasks](https://gofastmcp.com/python-sdk/fastmcp-client-tasks.md)
- [telemetry](https://gofastmcp.com/python-sdk/fastmcp-client-telemetry.md)
- [tools](https://gofastmcp.com/python-sdk/fastmcp-client-mixins-tools.md)

### Python SDK - decorators

- [decorators](https://gofastmcp.com/python-sdk/fastmcp-decorators.md)

### Python SDK - dependencies

- [dependencies](https://gofastmcp.com/python-sdk/fastmcp-dependencies.md)

### Python SDK - exceptions

- [exceptions](https://gofastmcp.com/python-sdk/fastmcp-exceptions.md)

### Python SDK - experimental

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-experimental-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-experimental-sampling-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-experimental-transforms-__init__.md)
- [code_mode](https://gofastmcp.com/python-sdk/fastmcp-experimental-transforms-code_mode.md)
- [handlers](https://gofastmcp.com/python-sdk/fastmcp-experimental-sampling-handlers.md)

### Python SDK - mcp_config

- [mcp_config](https://gofastmcp.com/python-sdk/fastmcp-mcp_config.md)

### Python SDK - prompts

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-prompts-__init__.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-prompts-base.md)
- [function_prompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-function_prompt.md)

### Python SDK - resources

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-resources-__init__.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-resources-base.md)
- [function_resource](https://gofastmcp.com/python-sdk/fastmcp-resources-function_resource.md)
- [template](https://gofastmcp.com/python-sdk/fastmcp-resources-template.md)
- [types](https://gofastmcp.com/python-sdk/fastmcp-resources-types.md)

### Python SDK - server

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-auth-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-auth-oauth_proxy-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-mixins-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-openapi-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-providers-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-providers-local_provider-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-providers-local_provider-decorators-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-providers-openapi-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-providers-skills-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-sampling-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-search-__init__.md)
- [aggregate](https://gofastmcp.com/python-sdk/fastmcp-server-providers-aggregate.md)
- [app](https://gofastmcp.com/python-sdk/fastmcp-server-app.md)
- [apps](https://gofastmcp.com/python-sdk/fastmcp-server-apps.md)
- [auth](https://gofastmcp.com/python-sdk/fastmcp-server-auth-auth.md)
- [auth0](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-auth0.md)
- [authorization](https://gofastmcp.com/python-sdk/fastmcp-server-auth-authorization.md)
- [authorization](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-authorization.md)
- [aws](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-aws.md)
- [azure](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-azure.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-server-providers-base.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-search-base.md)
- [bm25](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-search-bm25.md)
- [caching](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-caching.md)
- [capabilities](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-capabilities.md)
- [catalog](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-catalog.md)
- [cimd](https://gofastmcp.com/python-sdk/fastmcp-server-auth-cimd.md)
- [claude_provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-skills-claude_provider.md)
- [clerk](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-clerk.md)
- [components](https://gofastmcp.com/python-sdk/fastmcp-server-openapi-components.md)
- [components](https://gofastmcp.com/python-sdk/fastmcp-server-providers-openapi-components.md)
- [config](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-config.md)
- [consent](https://gofastmcp.com/python-sdk/fastmcp-server-auth-oauth_proxy-consent.md)
- [context](https://gofastmcp.com/python-sdk/fastmcp-server-context.md)
- [debug](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-debug.md)
- [dependencies](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies.md)
- [dereference](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-dereference.md)
- [descope](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-descope.md)
- [directory_provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-skills-directory_provider.md)
- [discord](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-discord.md)
- [elicitation](https://gofastmcp.com/python-sdk/fastmcp-server-elicitation.md)
- [elicitation](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-elicitation.md)
- [error_handling](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling.md)
- [event_store](https://gofastmcp.com/python-sdk/fastmcp-server-event_store.md)
- [fastmcp_provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-fastmcp_provider.md)
- [filesystem](https://gofastmcp.com/python-sdk/fastmcp-server-providers-filesystem.md)
- [filesystem_discovery](https://gofastmcp.com/python-sdk/fastmcp-server-providers-filesystem_discovery.md)
- [github](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-github.md)
- [google](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-google.md)
- [handlers](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-handlers.md)
- [http](https://gofastmcp.com/python-sdk/fastmcp-server-http.md)
- [in_memory](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-in_memory.md)
- [introspection](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-introspection.md)
- [jwt](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-jwt.md)
- [jwt_issuer](https://gofastmcp.com/python-sdk/fastmcp-server-auth-jwt_issuer.md)
- [keys](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-keys.md)
- [lifespan](https://gofastmcp.com/python-sdk/fastmcp-server-lifespan.md)
- [lifespan](https://gofastmcp.com/python-sdk/fastmcp-server-mixins-lifespan.md)
- [local_provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-local_provider-local_provider.md)
- [logging](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-logging.md)
- [low_level](https://gofastmcp.com/python-sdk/fastmcp-server-low_level.md)
- [mcp_operations](https://gofastmcp.com/python-sdk/fastmcp-server-mixins-mcp_operations.md)
- [middleware](https://gofastmcp.com/python-sdk/fastmcp-server-auth-middleware.md)
- [middleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware.md)
- [models](https://gofastmcp.com/python-sdk/fastmcp-server-auth-oauth_proxy-models.md)
- [namespace](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-namespace.md)
- [notifications](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-notifications.md)
- [oci](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-oci.md)
- [oidc_proxy](https://gofastmcp.com/python-sdk/fastmcp-server-auth-oidc_proxy.md)
- [ping](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-ping.md)
- [prompts](https://gofastmcp.com/python-sdk/fastmcp-server-providers-local_provider-decorators-prompts.md)
- [prompts_as_tools](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-prompts_as_tools.md)
- [propelauth](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-propelauth.md)
- [provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-openapi-provider.md)
- [proxy](https://gofastmcp.com/python-sdk/fastmcp-server-auth-oauth_proxy-proxy.md)
- [proxy](https://gofastmcp.com/python-sdk/fastmcp-server-providers-proxy.md)
- [proxy](https://gofastmcp.com/python-sdk/fastmcp-server-proxy.md)
- [rate_limiting](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting.md)
- [redirect_validation](https://gofastmcp.com/python-sdk/fastmcp-server-auth-redirect_validation.md)
- [regex](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-search-regex.md)
- [requests](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-requests.md)
- [resources](https://gofastmcp.com/python-sdk/fastmcp-server-providers-local_provider-decorators-resources.md)
- [resources_as_tools](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-resources_as_tools.md)
- [response_limiting](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-response_limiting.md)
- [routing](https://gofastmcp.com/python-sdk/fastmcp-server-openapi-routing.md)
- [routing](https://gofastmcp.com/python-sdk/fastmcp-server-providers-openapi-routing.md)
- [routing](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-routing.md)
- [run](https://gofastmcp.com/python-sdk/fastmcp-server-sampling-run.md)
- [sampling_tool](https://gofastmcp.com/python-sdk/fastmcp-server-sampling-sampling_tool.md)
- [scalekit](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-scalekit.md)
- [server](https://gofastmcp.com/python-sdk/fastmcp-server-openapi-server.md)
- [server](https://gofastmcp.com/python-sdk/fastmcp-server-server.md)
- [skill_provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-skills-skill_provider.md)
- [ssrf](https://gofastmcp.com/python-sdk/fastmcp-server-auth-ssrf.md)
- [subscriptions](https://gofastmcp.com/python-sdk/fastmcp-server-tasks-subscriptions.md)
- [supabase](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-supabase.md)
- [telemetry](https://gofastmcp.com/python-sdk/fastmcp-server-telemetry.md)
- [timing](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-timing.md)
- [tool_injection](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-tool_injection.md)
- [tool_transform](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-tool_transform.md)
- [tools](https://gofastmcp.com/python-sdk/fastmcp-server-providers-local_provider-decorators-tools.md)
- [transport](https://gofastmcp.com/python-sdk/fastmcp-server-mixins-transport.md)
- [ui](https://gofastmcp.com/python-sdk/fastmcp-server-auth-oauth_proxy-ui.md)
- [vendor_providers](https://gofastmcp.com/python-sdk/fastmcp-server-providers-skills-vendor_providers.md)
- [version_filter](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-version_filter.md)
- [visibility](https://gofastmcp.com/python-sdk/fastmcp-server-transforms-visibility.md)
- [workos](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-workos.md)
- [wrapped_provider](https://gofastmcp.com/python-sdk/fastmcp-server-providers-wrapped_provider.md)

### Python SDK - settings

- [settings](https://gofastmcp.com/python-sdk/fastmcp-settings.md)

### Python SDK - telemetry

- [telemetry](https://gofastmcp.com/python-sdk/fastmcp-telemetry.md)

### Python SDK - tools

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-tools-__init__.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-tools-base.md)
- [function_parsing](https://gofastmcp.com/python-sdk/fastmcp-tools-function_parsing.md)
- [function_tool](https://gofastmcp.com/python-sdk/fastmcp-tools-function_tool.md)
- [tool_transform](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform.md)

### Python SDK - types

- [types](https://gofastmcp.com/python-sdk/fastmcp-types.md)

### Python SDK - utilities

- [**init**](https://gofastmcp.com/python-sdk/fastmcp-utilities-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-__init__.md)
- [**init**](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-__init__.md)
- [async_utils](https://gofastmcp.com/python-sdk/fastmcp-utilities-async_utils.md)
- [auth](https://gofastmcp.com/python-sdk/fastmcp-utilities-auth.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-base.md)
- [base](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-base.md)
- [cli](https://gofastmcp.com/python-sdk/fastmcp-utilities-cli.md)
- [components](https://gofastmcp.com/python-sdk/fastmcp-utilities-components.md)
- [director](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-director.md)
- [exceptions](https://gofastmcp.com/python-sdk/fastmcp-utilities-exceptions.md)
- [filesystem](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem.md)
- [formatters](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-formatters.md)
- [http](https://gofastmcp.com/python-sdk/fastmcp-utilities-http.md)
- [inspect](https://gofastmcp.com/python-sdk/fastmcp-utilities-inspect.md)
- [json_schema](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema.md)
- [json_schema_converter](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-json_schema_converter.md)
- [json_schema_type](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema_type.md)
- [lifespan](https://gofastmcp.com/python-sdk/fastmcp-utilities-lifespan.md)
- [logging](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging.md)
- [mcp_server_config](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-mcp_server_config.md)
- [mime](https://gofastmcp.com/python-sdk/fastmcp-utilities-mime.md)
- [models](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-models.md)
- [pagination](https://gofastmcp.com/python-sdk/fastmcp-utilities-pagination.md)
- [parser](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-parser.md)
- [schemas](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi-schemas.md)
- [skills](https://gofastmcp.com/python-sdk/fastmcp-utilities-skills.md)
- [tests](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests.md)
- [timeout](https://gofastmcp.com/python-sdk/fastmcp-utilities-timeout.md)
- [token_cache](https://gofastmcp.com/python-sdk/fastmcp-utilities-token_cache.md)
- [types](https://gofastmcp.com/python-sdk/fastmcp-utilities-types.md)
- [ui](https://gofastmcp.com/python-sdk/fastmcp-utilities-ui.md)
- [uv](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-uv.md)
- [version_check](https://gofastmcp.com/python-sdk/fastmcp-utilities-version_check.md)
- [versions](https://gofastmcp.com/python-sdk/fastmcp-utilities-versions.md)

