# Model Context Protocol (MCP) Servers

Configured in config.yaml under `mcp_servers`:

## Active MCP Servers

### docling
- **Command**: `docling-mcp-server`
- **Transport**: stdio
- **Timeout**: 900s
- **Purpose**: Document parsing and conversion

### filesystem
- **Command**: `npx -y @modelcontextprotocol/server-filesystem`
- **Paths**: /home/lin/Documents, /home/lin/Downloads, /mnt/development1
- **Timeout**: 60s
- **Purpose**: File system access

### markitdown
- **Command**: `markitdown-mcp`
- **Timeout**: 600s
- **Tools**: convert_to_markdown only
- **Purpose**: Document-to-markdown conversion

### nexus-memory
- **Command**: `python3 /home/lin/.hermes/scripts/adapters/nexus_mcp_stdio.py`
- **Timeout**: unspecified
- **Env**: NEXUS_URL=http://100.68.0.96:7777, NEXUS_AGENT_ID=hermes, NEXUS_DEVICE=lin-hp, NEXUS_SOURCE=hermes
- **Purpose**: Nexus memory bridge (Synapse)

### codegraph
- **Command**: `codegraph serve --mcp`
- **Timeout**: 120s, connect_timeout 60s
- **Purpose**: Code symbol exploration and indexing

### airis-gateway
- **URL**: http://localhost:9400/mcp/
- **Timeout**: 180s
- **Purpose**: Airis gateway bridge

## Disabled
- **synapse** — disabled in config
