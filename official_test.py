import stats_package
from phase_one_data_prep import phase_one_data_prep as pop
from data_validation import data_validation
import pandas as pd
import numpy as np
from phase_two_data_preparation import phase_two_data_prep
from machine_learning import categorical_target

import time
start = time.time()
df_internal, labels = data_validation("test_data/cat_target/internet_usage.csv")
end = time.time()
print(end - start, "Data Validation")

start = time.time()
user_input = [0,0,1,0,1,0,1,1]
phase_one = pop(df_internal, "f54654", user_input, "target")
phase_one.execute_phase_one()
end = time.time()
print(end - start, "Phase One Data Prep")

start = time.time()
test = stats_package.categorical_target(phase_one.df, phase_one.column_dtypes, phase_one.target,phase_one.cont_cols, phase_one.cat_cols)
test.clear_over_correlated_columns()
test.ci_test()
test.chi_test()
end = time.time()
print(end - start, " Stats") 

start = time.time()
x = phase_two_data_prep(test.df, test.cat_cols, test.cont_cols, phase_one.target)
x.prep_nans()
x.prep_conts()
x.prep_cats()
x.final_clean()
print(end - start, "Phase Two Data Prep")

start = time.time()
final = categorical_target(x.df, test.target)
final.model_selection()
final.split_data()
final.build_model()
final.round_one_grid_seach()
final.round_two_grid_search()
final.final()
print(end - start, "Machine Learning")

df_internal