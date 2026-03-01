from typing import Any

from ..connection import get_connection


def get_table_schema(
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
            cursor.execute(f"DESCRIBE `{table_name}`")
            columns = cursor.fetchall()

            cursor.execute(f"SHOW INDEX FROM `{table_name}`")
            indexes = cursor.fetchall()

            return {
                "success": True,
                "table_name": table_name,
                "columns": columns,
                "indexes": indexes,
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }
        finally:
            cursor.close()
