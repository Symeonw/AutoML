import stats_package
from phase_one_data_prep import phase_one_data_prep as pop
from data_validation import data_validation
import pandas as pd
import numpy as np
from phase_two_data_preparation import phase_two_data_prep

pd.set_option('display.float_format', lambda x: '%.3f' % x)


import time
start = time.time()
df, labels = data_validation("test_data/cat_target/internet_usage.csv")
end = time.time()
print(end - start)


start = time.time()
user_input = [0,0,1,0,1,0,1,1]
phase_one = pop(df, "f54654", user_input, "target")
phase_one.execute_phase_one()
end = time.time()
print(end - start)

start = time.time()
test = stats_package.categorical_target(phase_one.df, phase_one.column_dtypes, phase_one.target)
test.clear_over_correlated_columns()
test.ci_test()
test.chi_test()
end = time.time()
print(end - start, " Stats") 

start = time.time()
x = phase_two_data_prep(df, test.cat_cols, test.cont_cols)
x.prep_nans()
x.prep_conts()
print(end - start, " Stats")


