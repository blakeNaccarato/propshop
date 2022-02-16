"""Mats with an associated lookup table. Mat type subsets for convenience."""

from enum import Enum, auto


class Prop(Enum):
    THERMAL_CONDUCTIVITY = auto()


class Mat(Enum):
    COPPER = auto()
