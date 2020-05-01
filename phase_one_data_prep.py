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




def phase_one_data_preparation(data_file: "CSV File", user_input: "Python List", event_record_path:"Relative Path") -> "CSV File":
    """Drops columns with >= 50% of values missing unless column has >= 1000 rows,
    identifies and handels outliers using modified z-socring and assigns categorical variables
    as per customer specification.  
    """
    # Changes column types to category and float based off of user input
    df = data_file.copy()
    for column_type, col in zip(user_input,df.columns):
        if column_type == 1:
            df[col] = df[col].astype("category")
        else:
            df[col] = df[col].astype(float)
    #-------------------------------------------------
    # Drops columns with over 50% of data missing, adds event to record.
    col_nan_pct = df.isin([' ',np.nan]).mean() #Calculates percent of Nans
    col_names = col_nan_pct[col_nan_pct >= .1].index # Gets name of columns with over 50% Nans
    col_count = [df[col].count() for col in col_names for x in df if x == col]  #Gets length of valid values for column
    dropped_col = [col for col in zip(col_count, col_names) if col[0] <= 1000] #Gets columns names with under 1000 values
    record = open(event_record_path, "a+")
    [record.write(f"{col[1]} dropped due to more than 50% of data missing and less than 1000 rows of data: actual data consisted of {col[0]} values.\r") for col in dropped_col]
    record.close() #closes record
    [df.drop(columns=[col[1]], inplace=True) for col in dropped_col]
    #----------------------------------------------------------------------
    #Identifies and handels outliers
    cont_cols = df.select_dtypes(exclude=["category"]).columns # Gets continous columns
    cont_cols
    x = df.DailyRate.value_counts(normalize=True, ascending=False, dropna=True).head(1).reset_index().to_numpy()[0]
    for col in cont_cols:
        x = df[col].value_counts(normaized=True, ascending=False, dropna=True).head(1).reset_index().to_numpy()[0]
        if x[1] > 0.5:
            testset = df.[col][~df.[col].isin([x[0]])]


 
    def modified_zscore(col: pd.Series) -> pd.Series:
        med_col = col.median()
        med_abs_dev = MAD(col)
        mod_z = 0.6745*((col- med_col)/med_abs_dev)
        return np.abs(mod_z)
df2 = df.copy()
    def identify_and_handel_outliers():
        for cols in cont_cols:
            df2[f"{col}_mod_ z"] = modified_zscore(df[col])
            df2[df2[f"{col}_mod_z"] < 3]

        mod_z = (MAD(df.DailyRate) - df.DailyRate.median())/(1.486*MAD(df.DailyRate))
        mod_z = 0.6745*((df.DailyRate - df.DailyRate.median())/MAD(df.DailyRate))
        df["mod_z"] = mod_z
        df[np.abs(df.mod_z) < .5]

    return df


mod_z.__annotations__

df = phase_one_data_preparation(df, user_input,"test_data/user_record.txt")
        .to_parqet("test_data/Phase_one.csv", index=False)****
print("--- %s seconds ---" % (time.time() - start_time))

