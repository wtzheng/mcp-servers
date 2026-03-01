import json
from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class SSLConfig(BaseModel):
    enabled: bool = False
    ca_cert: str | None = None
    client_cert: str | None = None
    client_key: str | None = None


class MySQLConfig(BaseModel):
    host: str = "localhost"
    port: int = 3306
    user: str = "root"
    password: str = ""
    database: str | None = None
    ssl: SSLConfig = Field(default_factory=SSLConfig)


class Config(BaseModel):
    mysql: MySQLConfig = Field(default_factory=MySQLConfig)


def load_config(config_path: str | Path) -> Config:
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        if config_path.suffix in (".yaml", ".yml"):
            data = yaml.safe_load(f)
        elif config_path.suffix == ".json":
            data = json.load(f)
        else:
            raise ValueError(f"Unsupported config file format: {config_path.suffix}")

    return Config(**data)


def get_default_config_path() -> Path:
    current_dir = Path(__file__).parent.parent
    for filename in ["config.yaml", "config.json", "config.yml"]:
        path = current_dir / filename
        if path.exists():
            return path
    return current_dir / "config.yaml"
