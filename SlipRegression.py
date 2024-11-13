# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 11:07:54 2023

@author: Ashton.Eaves
"""

##### LANDSLIP ANALYSIS VERSION #########

import numpy as np
import pandas as pd

data = pd.read_csv('./RegressionInput.csv')
print(data)

# Replace NaN, infinity and too large values with 0
data = data.replace([np.inf, -np.inf, np.nan], 0)

#variable_names = [
#    "LCDB5_Class_2018",  # Spatial join on Land Cover Database
#    "RainGridcode",  # Spatial join on rainfall
#    "landslide",  # Spatial join on SedNet landslide susceptibility
#    "ESC2018",  # Spatial join on erosion susceptibility
#]

variable_names = [
#    "Shape_Area",
    "LCDB5Lookup",
    "lcorrclass",
    "SoilLookup",
    "slope_class",
  #  "GEOLOGY_",
    "RainGridcode"
]

from pysal.model import spreg

# Fit OLS model
m1 = spreg.OLS(
    # Dependent variable
    data[["Size_Area"]].values,
    # Independent variables
    data[variable_names].values,
    # Dependent variable name
    name_y="Size_Area",
    # Independent variable name
    name_x=variable_names,
)

print(m1.summary)