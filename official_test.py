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

#TODO: Is there anything we could do to make the CI test faster ASAP?