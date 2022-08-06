"""Your one-stop shop for material properties."""

__version__ = "0.0.8"

import pandas as pd
from numpy import typing as npt
from scipy.interpolate import interp1d

from propshop.configs import config
from propshop.library import Mat, Prop

TEMP = "TEMPERATURE"


def get_prop(mat: Mat, prop: Prop, temperatures: npt.ArrayLike):
    interp = get_interp(mat, prop)
    return interp(temperatures)


def get_interp(mat: Mat, prop: Prop):
    df = get_relationship_from_table(mat, prop)
    return interp1d(df.loc[:, TEMP], df.loc[:, prop.name])


def get_relationship_from_table(mat: Mat, prop: Prop) -> pd.DataFrame:
    return pd.read_feather(
        config.tables / f"{mat.name}.feather",
        columns=[TEMP, prop.name],
    ).dropna()
