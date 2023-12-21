"""Your one-stop shop for material properties."""

# pyright: reportImportCycles=none
# sourcery skip: no-wildcard-imports
from pandas import set_option

from propshop.api import *  # noqa: F403  # type: ignore  # Importing from api which has __all__

set_option("mode.string_storage", "pyarrow")
