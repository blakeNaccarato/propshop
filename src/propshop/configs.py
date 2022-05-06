from pathlib import Path

from dynaconf import Dynaconf
from pydantic.dataclasses import dataclass

import propshop

DEFAULT_CONFIG_FILENAME = "defaults.toml"
USER_CONFIG_FILENAME = "propshop.toml"
default_path = Path(propshop.__path__[0]) / DEFAULT_CONFIG_FILENAME  # type: ignore
user_path = Path(USER_CONFIG_FILENAME)
raw_config = Dynaconf(settings_files=[default_path, user_path])


def parse_tilde_in_path(path: str) -> Path:
    return Path.home() / path.lstrip("~/") if path.startswith("~/") else Path(path)


@dataclass
class Config:
    """A validated configuration."""

    app_folder: Path = parse_tilde_in_path(raw_config.app_folder)

    def __post_init_post_parse__(self):

        self.tables = self.app_folder / "tables"

        for folder in [self.app_folder, self.tables]:
            folder.mkdir(parents=False, exist_ok=True)


config = Config()
