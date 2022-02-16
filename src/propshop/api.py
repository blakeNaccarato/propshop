"""Get material properties."""

import pandas as pd

from propshop.configs import config
from propshop.library import Mat, Prop


def get_thermal_conductivity(material: Mat, prop: Prop, temperatures: pd.Series):
    get_property(material, prop)


def get_property(material: Mat, prop: Prop):
    df = pd.read_feather(config.tables / f"{material.name}.feather")
