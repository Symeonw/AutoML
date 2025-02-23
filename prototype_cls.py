import numpy as np
import pandas as pd
from scipy.stats import chi2
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import median_absolute_deviation as MAD


df = pd.read_csv("test_data/IBM_Data.csv")
user_column_label = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]
for col in df.columns:
    if col == "Age":
        df.loc[df.sample(frac=0.5).index, col] = pd.np.nan #Makes fake Nan's
    if col == "Education":
        df.loc[df.sample(frac=0.7).index, col] = pd.np.nan #Makes fake Nan's

df.at[0, "Age"] = 200

class phase_one_data_prep:

    def __init__(self, data_file, user_id, user_column_label, user_target_label):
        self.df= data_file
        self.user_id = user_id
        self.user_column_label = user_column_label
        self.user_target_label = user_target_label

    def assign_column_types(self):
        """Assigns column types (either float or category) to all columns as per user_column_label"""
        type_list = ["category" if u_input == 1 else float for u_input in self.user_column_label]
        self.df = self.df.astype(dict(zip(self.df.columns, type_list)))
        df_types = pd.DataFrame(self.df.dtypes).reset_index()
        df_types.columns = ["column_name", "dtype"]
        df_types.dtype = df_types.dtype.astype(str)
        self.column_dtypes = {list(df_types.column_name)[i]: list(df_types.dtype)[i] for i in range(len(df_types))}


    def handel_nans(self):
        """Drops all columns with over 50% Nans unless they have at least 50 values"""
        col_nan_pct = self.df.isin([' ',np.nan]).mean() #Calculates percent of Nans
        col_names = col_nan_pct[col_nan_pct >= .1].index # Gets name of columns with over 50% Nans
        col_count = [self.df[col].count() for col in col_names for x in self.df if x == col]  #Gets length of valid values for column
        dropped_col = [col for col in zip(col_count, col_names) if col[0] <= 1400] #Gets columns names with under 50 values
        [self.df.drop(columns=[col[1]], inplace=True) for col in dropped_col]
        self.dropped_cols_phase_one = dropped_col
        [self.column_dtypes.pop(item[1]) for item in dropped_col]
    

    def modified_zscore(col):
        """Makes calulations for Modified Z-Score"""
        col = col.dropna()
        med_col = col.median()
        med_abs_dev = MAD(col)
        mod_z = 0.6745*((col- med_col)/med_abs_dev)
        return np.abs(mod_z)


    def identify_and_handel_outliers(self):
        """This function measures the percentange amount that a value occurs, if it occurs over 50% of a given column
        that value is removed and the remaining values are tested for outliers with any outside 3 Modified Z-Score."""
        col_list = [] # This will hold the column names created for the administration of the modified z-score test
        values_dropped = []
        cont_cols = self.df.select_dtypes(exclude=["category"]).columns # Gets continous columns  
        for col in cont_cols:
            df_len = len(self.df)
            top_value = self.df[col].value_counts(normalize=True, ascending=False, dropna=True)\
                .head(1).reset_index().to_numpy()[0] #Gets the top occuring value along with its percentage of occurances
            if top_value[1] > 0.5:#Test if the top occuring value makes up more than 50% of the data
                remaining_col = self.df[col][~self.df[col].isin([top_value[0]])] #Gets all values not within the 50% of single value data
                self.df[f"{col}_mod_z"] = phase_one_data_prep.modified_zscore(remaining_col) #Gets modified z-score for remaining items
                self.df[f"{col}_mod_z"] = self.df[f"{col}_mod_z"].fillna(0) #Fills all missing z-scores\
                    #with zero(because that 50% of data removed would be zero anyways)
                self.df = self.df[self.df[f"{col}_mod_z"] < 3] #Removed all values outside 3
                col_list.append(f"{col}_mod_z")#Appends name of column to list
                values_dropped.append((col, df_len - len(self.df)))
            else:
                self.df[f"{col}_mod_z"] = phase_one_data_prep.modified_zscore(self.df[col]) #Gets modified z-score 
                self.df = self.df[self.df[f"{col}_mod_z"] < 3] #Removed all values outside 3
                col_list.append(f"{col}_mod_z")#Appends name of column to list
                values_dropped.append((col, df_len - len(self.df)))
        self.df.drop(columns = col_list, inplace=True)#Removed columns created to test modified z-score
        self.outliers_dropped = values_dropped

    def execute_phase_one(self):
        self.assign_column_types()
        self.handel_nans()
        self.identify_and_handel_outliers()


phase_one = phase_one_data_prep(df, "AFH6G7W", user_column_label, "Age")
phase_one.execute_phase_one()
phase_one.dropped_cols_phase_one

