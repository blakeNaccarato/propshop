"""Get material properties."""

import pandas as pd

from propshop.configs import config
from propshop.library import Mat, Prop


def get_property(material: Mat, prop: Prop, temperatures: pd.Series):
    df = pd.read_feather(
        config.tables / f"{material.name}.feather",  # type: ignore
        columns=["TEMPERATURE", prop.name],
    )
    ...
