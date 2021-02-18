#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Ricardo Dominguez"
__version__ = "0.0.1"
__maintainer__ = "Ricardo Dominguez"
__email__ = "ricardo.dominguezguevara@gmail.com"
__status__ = "Development"

# -- python import
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_table(historical:bool=False, year:int=2021, period:str="weekly"):
    print(historical, year, period)