import os
import pandas as pd
import numpy as np

# data files
unformal_file = "unformal.csv"
fnormal_file = "fnormal.csv"

unformal_data = pd.read_csv(unformal_file, sep=',', header=None, skiprows=1)
fnormal_file = pd.read_csv(fnormal_file, sep=',', header=None, skiprows=1)