import pandas as pd
import propshop
from propshop.library import Mat, Prop

propshop.get_thermal_conductivity(
    Mat.COPPER, Prop.THERMAL_CONDUCTIVITY, pd.Series([300, 350, 400])
)
...
