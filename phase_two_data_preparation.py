import stats_package
from phase_one_data_prep import phase_one_data_prep as pop
from data_validation import data_validation
import pandas as pd
import numpy as np




class phase_two_data_prep:

    def __init__(self, data_file, cont_cols, cat_cols, user_target_metadata):
        self.df = data_file


df.loc[:,df.isnull().mean() < .3]
x = [index for boolean, index in zip((df.isnull().sum(axis=1) < len(df.columns)/2),df.index) if boolean == True] # Collects all rows with
#   more than 50% of data missing for removal. 
df.loc[x,:]