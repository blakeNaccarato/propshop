from pathlib import Path

from dynaconf import Dynaconf
from pydantic import FilePath, validator
from pydantic.dataclasses import dataclass

import propshop

DEFAULT_CONFIG_FILENAME = "defaults.toml"
USER_CONFIG_FILENAME = "propshop.toml"
default_path = Path(propshop.__path__[0]) / DEFAULT_CONFIG_FILENAME  # type: ignore
user_path = next(Path().rglob(USER_CONFIG_FILENAME), Path(USER_CONFIG_FILENAME))
raw_config = Dynaconf(settings_files=[default_path, user_path])


@dataclass
class Config:
    """A validated configuration."""

    ees: FilePath

    @validator("ees")
    def validate_ees(cls, ees):
        if ees.name != "EES.exe":
            raise ValueError("Filename must be 'EES.exe'.")
        return ees

    def __post_init_post_parse__(self):
        self.ees_root = self.ees.parent


config = Config(ees=raw_config.ees)
