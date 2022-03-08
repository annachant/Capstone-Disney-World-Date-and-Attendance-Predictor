import os
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

pd.set_option("display.max_rows", None, "display.max_columns", None)

datapath = Path.cwd() 
print(datapath)

datasets = os.listdir(datapath)
datasets = list(sorted(datasets))
print(datasets)

for i in datasets:
    try:
        print(i)
        exec(f"{i.split('.csv')[0]} = pd.read_csv(datapath / i)")
    except:
        print(f"{i} cannot be imported automatically")