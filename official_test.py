import stats_package
from phase_one_data_prep_cls import phase_one_data_prep as pop
from data_validation import data_validation
import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.3f' % x)


import time
start = time.time()
df, labels = data_validation("test_data/zillow_data.csv")
end = time.time()
print(end - start)


start = time.time()
zillow_input = [1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1]
phase_one = pop(df, "f54654", zillow_input, "taxamount")
phase_one.execute_phase_one()
end = time.time()
print(end - start)


import time
start = time.time()
df, labels = data_validation("test_data/zillow_data.csv")
end = time.time()
print(end - start)


# df = pd.read_csv("test_data/IBM_Data.csv")
# column_dtypes = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]
# test = pop(df,"F647952", column_dtypes, "Age")
# test.execute_phase_one()
# test = continuous_target(test.df, test.column_dtypes, test.user_target_label)
# test.clear_over_correlated_columns()
# test.lin_corr_test()
# test.ci_test()
# test.dropped_cols_stats



def assign_column_types(df, zillow_input):
    """Assigns column types (either float or category) to all columns as per user_column_label"""
    type_list = ["category" if u_input == 1 else float for u_input in zillow_input]
    df = df.astype(dict(zip(df.columns, type_list)))
    return df
df = assign_column_types(df, zillow_input)

def handel_nans(df):
    """Drops all columns with over 50% Nans unless they have at least 50 values"""
    col_nan_pct = df.isin([' ',np.nan]).mean() #Calculates percent of Nans
    col_names = col_nan_pct[col_nan_pct >= .1].index # Gets name of columns with over 50% Nans
    col_count = [df[col].count() for col in col_names for x in df if x == col]  #Gets length of valid values for column
    dropped_col = [col for col in zip(col_count, col_names) if col[0] <= 1400] #Gets columns names with under 50 values
    [df.drop(columns=[col[1]], inplace=True) for col in dropped_col]
    return df

def modified_zscore(col):
    """Makes calulations for Modified Z-Score"""
    col = col.dropna()
    med_col = col.median()
    med_abs_dev = MAD(col)
    mod_z = 0.6745*((col- med_col)/med_abs_dev)
    return np.abs(mod_z)



from scipy.stats import median_absolute_deviation as MAD
cont_cols = df.select_dtypes(exclude=["category"]).columns # Gets continous columns  
for col in cont_cols:
    print(col)
    df_len = len(df)
    top_value = df[col].value_counts(normalize=True, ascending=False, dropna=True)
    top_value = top_value.head(1).reset_index().to_numpy() #Gets the top occuring value along with its percentage of occurances
    if top_value[0][1] > 0.5:#Test if the top occuring value makes up more than 50% of the data
        remaining_col = df[col][~df[col].isin([top_value[0][1]])] #Gets all values not within the 50% of single value data
        df[f"{col}_mod_z"] = modified_zscore(remaining_col) #Gets modified z-score for remaining items
    else:
        df[f"{col}_mod_z"] = modified_zscore(df[col]) #Gets modified z-score 

df[df.basementsqft_mod_z < 3]

df.taxdelinquencyyear.value_counts().sum()

import seaborn as sns

sns.distplot(df.basementsqft)
phase_one.df

len(df)

