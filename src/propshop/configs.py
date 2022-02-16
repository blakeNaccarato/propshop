from pathlib import Path

from dynaconf import Dynaconf
from pydantic import DirectoryPath
from pydantic.dataclasses import dataclass

import propshop

DEFAULT_CONFIG_FILENAME = "defaults.toml"
USER_CONFIG_FILENAME = "propshop.toml"
default_path = Path(propshop.__path__[0]) / DEFAULT_CONFIG_FILENAME  # type: ignore
user_path = next(Path().rglob(USER_CONFIG_FILENAME), Path(USER_CONFIG_FILENAME))
raw_config = Dynaconf(settings_files=[default_path, user_path])


def parse_tilde_in_path(path: str) -> Path:
    if path.startswith("~/"):
        return Path.home() / raw_config.tables.lstrip("~/")
    else:
        return Path(path)


@dataclass
class Config:
    """A validated configuration."""

    tables: DirectoryPath = parse_tilde_in_path(raw_config.tables)


config = Config()
