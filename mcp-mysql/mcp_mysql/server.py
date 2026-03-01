
from fastmcp import FastMCP

from .tools.list import list_databases, list_tables
from .tools.query import execute_query
from .tools.schema import get_table_schema

mcp = FastMCP("mcp-mysql")


@mcp.tool()
async def mysql_execute_query(
    sql: str,
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    database: str | None = None,
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> str:
    result = execute_query(
        sql=sql,
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl_enabled=ssl_enabled,
        ssl_ca=ssl_ca,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
    )
    return str(result)


@mcp.tool()
async def mysql_get_table_schema(
    table_name: str,
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    database: str | None = None,
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> str:
    result = get_table_schema(
        table_name=table_name,
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl_enabled=ssl_enabled,
        ssl_ca=ssl_ca,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
    )
    return str(result)


@mcp.tool()
async def mysql_list_databases(
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> str:
    result = list_databases(
        host=host,
        port=port,
        user=user,
        password=password,
        ssl_enabled=ssl_enabled,
        ssl_ca=ssl_ca,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
    )
    return str(result)


@mcp.tool()
async def mysql_list_tables(
    database: str,
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> str:
    result = list_tables(
        database=database,
        host=host,
        port=port,
        user=user,
        password=password,
        ssl_enabled=ssl_enabled,
        ssl_ca=ssl_ca,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
    )
    return str(result)


if __name__ == "__main__":
    mcp.run()
