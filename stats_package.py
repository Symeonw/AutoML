from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import pandas as pd
import numpy as np


def create_chi_table():
    p = np.array([0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005])
    df = np.array(list(range(1, 30)) + list(range(30, 101, 10))).reshape(-1, 1)
    np.set_printoptions(linewidth=130, formatter=dict(float=lambda x: "%7.3f" % x))
    table = chi2.isf(p, df)
    return table


def check_chi(var1,var2):
    chi_inp = pd.crosstab(var1, var2)
    chi2, p, dof, expected = chi2_contingency(chi_inp.values)
    if np.array(i >= 5 for i in expected).all() == False:
        raise ValueError("""Expected frequency did not render expected value beyond 5,
        please gather additional data or use different variables.""")
    if create_chi_table()[dof-1][6] > chi2 or p > .05 :
        print("These variables are independent, failed to reject H0.")
    else:
        print("These variables are dependent, H0 rejected.")

df = pd.read_csv("test_data/IBM_Data.csv")
user_column_label = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]

class statistical_package:

    def __init__(self, data_file, column_dtypes, user_target_label):
        del phase_one.df
        self.df = data_file
        self.column_dtypes = column_dtypes
        del phase_one.column_dtypes
        self.user_target_label = user_target_label

        
    def continuous_tests(self):
        


test = statistical_package(phase_one.df, user_column_label, "Attrition")
phase_one.column_dtypes