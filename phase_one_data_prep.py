# import time
# start_time = time.time()
import pandas as pd
import numpy as np
from scipy.stats import median_absolute_deviation as MAD

df = pd.read_csv("test_data/IBM_Data.csv")
user_input = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]
for col in df.columns:
    if col == "Age":
        df.loc[df.sample(frac=0.5).index, col] = pd.np.nan #Makes fake Nan's
    if col == "Education":
        df.loc[df.sample(frac=0.7).index, col] = pd.np.nan #Makes fake Nan's




def phase_one_data_preparation(data_file: pd.DataFrame , user_input: list, event_record_path:"Relative Path") -> "Parquet File":
    """Drops columns with >= 50% of values missing unless column has >= 1000 rows,
    identifies and handels outliers using modified z-socring and assigns categorical variables
    as per customer specification.  
    """
    # Changes column types to category and float based off of user input
    df = data_file
    [df[col].astype("category") if columnn_type == 1 else df[col].astype(float)\
         for col, column_type in zip(user_input, df.columns) ]
    #-------------------------------------------------
    # Drops columns with over 50% of data missing, adds event to record.
    col_nan_pct = df.isin([' ',np.nan]).mean() #Calculates percent of Nans
    col_names = col_nan_pct[col_nan_pct >= .1].index # Gets name of columns with over 50% Nans
    col_count = [df[col].count() for col in col_names for x in df if x == col]  #Gets length of valid values for column
    dropped_col = [col for col in zip(col_count, col_names) if col[0] <= 1000] #Gets columns names with under 1000 values
    record = open(event_record_path, "a+")
    [record.write(f"{col[1]} dropped due to more than 50% of data missing and less than 1000 rows of data: actual data consisted of {col[0]} values.\r") for col in dropped_col]
    [df.drop(columns=[col[1]], inplace=True) for col in dropped_col]
    #----------------------------------------------------------------------
    #Identifies and handels outliers
    cont_cols = df.select_dtypes(exclude=["category"]).columns # Gets continous columns    

    def modified_zscore(col: pd.Series) -> pd.Series:
        """Makes calulations for Modified Z-Score"""
        med_col = col.median()
        med_abs_dev = MAD(col)
        mod_z = 0.6745*((col- med_col)/med_abs_dev)
        return np.abs(mod_z)
    def identify_and_handel_outliers():
        """This function measures the percentange amount that a value occurs, if it occurs over 50% of a given column
        that value is removed and the remaining values are tested for outliars with any outside 3 MAD being dropped."""
        col_list = []
        df_len = len(df)
        for col in cont_cols:
            top_value = df[col].value_counts(normalized=True, ascending=False, dropna=True)\
                .head(1).reset_index().to_numpy()[0] #Gets the top occuring value along with its percentage of occurances
                if top_value[1] > 0.5:#Test if the top occuring value makes up more than 50% of the data
                    col = df.[col][~df.[col].isin([x[0]])] #Gets all values not within the 50% of single value data
            df[f"{col}_mod_z"] = modified_zscore(df[col])
            df[df[f"{col}_mod_z"] > 3]
            col_list.append(f"{col}_mod_z")
        df.drop(columns = col_list, inplace=True)

    record.close() #closes record
    return df


mod_z.__annotations__

df = phase_one_data_preparation(df, user_input,"test_data/user_record.txt")
        .to_parqet("test_data/Phase_one.csv", index=False)****



import time
start_time = time.time()
col_list = []
for col in cont_cols:
    df[f"{col}_mod_z"] = modified_zscore(df[col])
    df[df[f"{col}_mod_z"] > 3]
    col_list.append(f"{col}_mod_z")
    df.drop(columns = col_list, inplace=True)
print("--- %s seconds ---" % (time.time() - start_time))


