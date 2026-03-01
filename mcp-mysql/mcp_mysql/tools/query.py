from typing import Any

from ..connection import get_connection


def execute_query(
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
            cursor.execute(sql)
            if sql.strip().upper().startswith(("SELECT", "SHOW", "DESCRIBE", "EXPLAIN")):
                results = cursor.fetchall()
                return {
                    "success": True,
                    "rows": results,
                    "row_count": len(results),
                    "columns": list(results[0].keys()) if results else [],  # type: ignore[attr-defined]
                }
            else:
                conn.commit()
                return {
                    "success": True,
                    "affected_rows": cursor.rowcount,
                    "last_insert_id": cursor.lastrowid,
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
            }
        finally:
            cursor.close()
