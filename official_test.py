import stats_package
from phase_one_data_prep import phase_one_data_prep as pop
from data_validation import data_validation
import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.3f' % x)


import time
start = time.time()
df, labels = data_validation("test_data/cont_target/zillow_2016.csv")
end = time.time()
print(end - start)


start = time.time()
zillow_input = [2,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1]
phase_one = pop(df, "f54654", zillow_input, "logerror")
phase_one.execute_phase_one()
end = time.time()
print(end - start)




start = time.time()
test = stats_package.continuous_target(phase_one.df, phase_one.column_dtypes, phase_one.target)
test.clear_over_correlated_columns()
test.lin_corr_test()
test.ci_test()
end = time.time()
print(end - start, " Stats")


test.dropped_cols_stats
df.columns
df2 = test.df
df.assessmentyear.value_counts()

t = []
for col in df2.columns:
    if (df2[col].dtype != float) & (df2[col].dtype != int):
        t.append(col)

df3 = pd.get_dummies(df2, columns=t)



import seaborn as sns
df.dtypes
sns.regplot(df.censustractandblock, df.logerror)

df.logerror.corr(df.bedroomcnt)
df.columns

df2.tail(20)

import xgboost as xgb
X,y = df.drop(columns="logerror"), df.logerror
for col in X.columns:
    if X[col].dtype == "O":
        t = pd.get_dummies(X[col])
        X = pd.concat([t,X])
        X.drop(columns=[col], inplace=True)

X = pd.get_dummies(X)
t = pd.get_dummies(X.fips)

o = pd.DataFrame()

o.insert(t)

pd.concat([t,o])