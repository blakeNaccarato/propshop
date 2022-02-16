import pandas as pd
import propshop
from propshop import config
from propshop.library import Mat, Prop

propshop.get_property(Mat.COPPER, Prop.THERMAL_CONDUCTIVITY, pd.Series([300, 350, 400]))
...
