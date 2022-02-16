"""Your one-stop shop for material properties."""

__version__ = "0.0.0"

from pathlib import Path
from propshop.api import *  # type: ignore

(Path.home() / ".propshop").mkdir(parents=False, exist_ok=True)
