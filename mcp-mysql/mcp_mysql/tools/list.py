from typing import Any

from ..connection import get_connection


def list_databases(
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> dict[str, Any]:
    with get_connection(
        host=host,
        port=port,
        user=user,
        password=password,
        database=None,
        ssl_enabled=ssl_enabled,
        ssl_ca=ssl_ca,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
    ) as conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            return {
                "success": True,
                "databases": [db["Database"] for db in databases],  # type: ignore[call-overload,union-attr]
                "count": len(databases),
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }
        finally:
            cursor.close()


def list_tables(
    database: str,
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> dict[str, Any]:
    with get_connection(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl_enabled=ssl_enabled,
        ssl_ca=ssl_ca,
        ssl_cert=ssl_cert,
        ssl_key=ssl_key,
    ) as conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            table_list = [list(table.values())[0] for table in tables]  # type: ignore[attr-defined,union-attr]
            return {
                "success": True,
                "database": database,
                "tables": table_list,
                "count": len(table_list),
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }
        finally:
            cursor.close()
