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
zillow_input = [2,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1]
phase_one = pop(df, "f54654", zillow_input, "taxamount")
phase_one.execute_phase_one()
end = time.time()
print(end - start)




start = time.time()
test = stats_package.continuous_target(phase_one.df, phase_one.column_dtypes, phase_one.target)
test.clear_over_correlated_columns()
test.lin_corr_test()
test.ci_test()
test.dropped_cols_stats
end = time.time()
print(end - start, " Stats")



# #Continuous Testing
# df = pd.read_csv("test_data/IBM_Data.csv")
# column_dtypes = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]


df.propertyzoningdesc.nunique()
df.propertyzoningdesc.value_counts(normalize=True)
df.rawcensustractandblock.isnull().sum()


#TODO: Is there anything we could do to make the CI test faster ASAP?
df = pd.read_csv("test_data/zillow_data.csv")

def mean_confidence_interval(df:"two column dataframe", confidence=0.90):
    """Takes in two columns: target(Category) and test column (continous)."""
    target_len = len(df.iloc[:,1].unique())
    ci = []
    for i in range(target_len): #Accessing all unique categories in target, running all groupings of contious variables though test.
        data = df[df.iloc[:,1] == df.iloc[:,1].unique()[i]].iloc[:,0]
        if data < 30:
            continue
        a = 1.0 * np.array(data)
        n = len(a)
        m, se = np.mean(a), sem(a)
        h = se * t.ppf((1 + confidence) / 2., n-1)
        ci.append([m-h,m+h])
    return ci

start = time.time()
x = mean_confidence_interval(df[["decktypeid", "taxamount"]])
end = time.time()
print(end - start, " Stats")

df.decktypeid.nunique()

df2=df[["rawcensustractandblock", "taxamount"]]

df2.iloc[:,0].unique()
df.decktypeid.unique()

df = phase_one.df[["rawcensustractandblock", "taxamount"]]

data = df[df.iloc[:,1]==df.iloc[:,1].unique()[1]]
data.count() > 30

df.taxamount.isnull().sum()/len(df.taxamount)

df.taxamount.dropna(inplace=True)
(df.propertyzoningdesc.value_counts() > 30).sum()

from scipy.stats import t

1.0 * np.array(data)


phase_one.df.censustractandblock.unique()

df = pd.read_csv("test_data/IBM_Data.csv")

df.EducationField.value_counts(normalized=True)