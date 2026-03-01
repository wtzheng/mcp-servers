from collections.abc import Generator
from contextlib import contextmanager

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection

from .config import MySQLConfig, SSLConfig


def build_ssl_config(ssl_settings: SSLConfig) -> dict[str, str | bool] | None:
    if not ssl_settings.enabled:
        return None

    ssl_config: dict[str, str | bool] = {
        "ssl_disabled": False,
    }

    if ssl_settings.ca_cert:
        ssl_config["ssl_ca"] = ssl_settings.ca_cert
    if ssl_settings.client_cert:
        ssl_config["ssl_cert"] = ssl_settings.client_cert
    if ssl_settings.client_key:
        ssl_config["ssl_key"] = ssl_settings.client_key

    return ssl_config


def create_connection(config: MySQLConfig) -> MySQLConnection:
    ssl_config = build_ssl_config(config.ssl)

    connection_params: dict[str, str | int | None] = {
        "host": config.host,
        "port": config.port,
        "user": config.user,
        "password": config.password,
        "database": config.database,
    }

    if ssl_config:
        connection_params.update(ssl_config)

    return mysql.connector.connect(**connection_params)  # type: ignore[return-value]


def create_connection_from_params(
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    database: str | None = None,
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> MySQLConnection:
    ssl_config = SSLConfig(
        enabled=ssl_enabled,
        ca_cert=ssl_ca,
        client_cert=ssl_cert,
        client_key=ssl_key,
    )

    mysql_config = MySQLConfig(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        ssl=ssl_config,
    )

    return create_connection(mysql_config)


@contextmanager
def get_connection(
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    database: str | None = None,
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> Generator[MySQLConnection, None, None]:
    conn = None
    try:
        conn = create_connection_from_params(
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
        yield conn
    finally:
        if conn and conn.is_connected():
            conn.close()


def test_connection(
    host: str = "localhost",
    port: int = 3306,
    user: str = "root",
    password: str = "",
    database: str | None = None,
    ssl_enabled: bool = False,
    ssl_ca: str | None = None,
    ssl_cert: str | None = None,
    ssl_key: str | None = None,
) -> tuple[bool, str]:
    try:
        conn = create_connection_from_params(
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
        conn.close()
        return True, "Connection successful"
    except Error as e:
        return False, str(e)
