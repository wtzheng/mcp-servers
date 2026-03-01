# mcp-mysql

MySQL MCP server for Model Context Protocol.

## Features

- Execute SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Get table schema (columns, indexes)
- List databases
- List tables in a database
- Password authentication
- Optional SSL/TLS encryption

## Requirements

- Python 3.10+
- MySQL 5.7 or 8.0+

## Installation

```bash
cd mcp-mysql
uv sync
```

## Configuration

Create a `config.yaml` or `config.json` file in the project root:

### YAML Example

```yaml
mysql:
  host: localhost
  port: 3306
  user: root
  password: your_password
  database: your_database
  ssl:
    enabled: false
    ca_cert: /path/to/ca.pem
    client_cert: /path/to/client-cert.pem
    client_key: /path/to/client-key.pem
```

### JSON Example

```json
{
  "mysql": {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "your_password",
    "database": "your_database",
    "ssl": {
      "enabled": false,
      "ca_cert": "/path/to/ca.pem",
      "client_cert": "/path/to/client-cert.pem",
      "client_key": "/path/to/client-key.pem"
    }
  }
}
```

## Usage

### Run the MCP Server

```bash
python -m mcp_mysql.server
```

Or use the FastMCP CLI:

```bash
fastmcp run mcp_mysql.server
```

### MCP Tools

The server provides the following tools:

| Tool | Description |
|------|-------------|
| `mysql_execute_query` | Execute SQL queries |
| `mysql_get_table_schema` | Get table structure |
| `mysql_list_databases` | List all databases |
| `mysql_list_tables` | List tables in a database |

### Example Usage

```python
from mcp_mysql.server import mysql_execute_query, mysql_list_databases

# List databases
result = await mysql_list_databases(
    host="localhost",
    port=3306,
    user="root",
    password="password"
)

# Execute a query
result = await mysql_execute_query(
    sql="SELECT * FROM users LIMIT 10",
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database="myapp"
)
```

## Development

```bash
# Install dev dependencies
uv sync --extra dev

# Run tests
pytest

# Run with type checking
uv run --extra dev ruff check mcp_mysql
uv run --extra dev mypy mcp_mysql
```
