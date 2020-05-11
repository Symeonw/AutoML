import pandas as pd
import numpy as np
from scipy.stats import median_absolute_deviation as MAD


class phase_one_data_prep:

    def __init__(self, data_file, user_id, user_input):
        self.df= data_file
        self.user_id = user_id
        self.user_input = user_input

    def assign_column_types(self):
        type_list = ["category" if u_input == 1 else float for u_input in self.user_input]
        self.df = self.df.astype(dict(zip(self.df.columns, type_list)))

    def handel_nans(self):
        col_nan_pct = self.df.isin([' ',np.nan]).mean() #Calculates percent of Nans
        col_names = col_nan_pct[col_nan_pct >= .1].index # Gets name of columns with over 50% Nans
        col_count = [self.df[col].count() for col in col_names for x in self.df if x == col]  #Gets length of valid values for column
        dropped_col = [col for col in zip(col_count, col_names) if col[0] <= 1000] #Gets columns names with under 1000 values
        self.dropped_due_to_nan = dropped_col
        [self.df.drop(columns=[col[1]], inplace=True) for col in dropped_col]
