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
test = stats_package.continuous_target(phase_one.df, phase_one.column_dtypes, phase_one.user_target_label)
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




def mean_confidence_interval(df:"two column dataframe", confidence=0.90):
    """Takes in two columns: target(Category) and test column (continous)."""
    target_len = len(df.iloc[:,1].unique())
    ci = []
    for i in range(target_len): #Accessing all unique categories in target, running all groupings of contious variables though test.
        data = df[df.iloc[:,1] == df.iloc[:,1].unique()[i]].iloc[:,0]
        a = 1.0 * np.array(data)
        n = len(a)
        m, se = np.mean(a), sem(a)
        h = se * t.ppf((1 + confidence) / 2., n-1)
        ci.append([m-h,m+h])
    return ci



def ci_test(self):
    """Preforms confidence interval test on columns with greater than 100 values"""
    removed_cols = []
    for col in self.cat_cols:
        print(f"CI TEST FOR {col}")
        if self.df[col].count() >= 100:
            ci = continuous_target.mean_confidence_interval(self.df[[self.target, col]])
            maxs = []
            mins = []
            totals = []
            for i in range(len(ci)):
                maxs.append(ci[i][1])
                mins.append(ci[i][0])
                totals.append(ci[i][1] - ci[i][0])
            drop_col = np.array(max(maxs)) - np.array(min(mins)) < sum(totals)
            if drop_col == True:
                self.dropped_cols_stats.update({col:0})
                removed_cols.append(col)
            if mins == maxs:
                self.dropped_cols_stats.update({col:0})
                removed_cols.append(col)
    self.df.drop(columns=removed_cols, inplace=True)
    [self.cat_cols.remove(item) for item in removed_cols]
