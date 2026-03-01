# mcp-servers
model-context-protocol servers

## mcp inspecting

```bash
npx @modelcontextprotocol/inspector \
  uv \
  --directory {path}/mcp-servers/mcp-mysql \
  run \
  python -m mcp_mysql.server
```