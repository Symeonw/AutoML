from scipy.stats import t, sem, chi2, chi2_contingency
import pandas as pd
import numpy as np
from phase_one_data_prep_cls import phase_one_data_prep as pop
from itertools import combinations

#Documentation
    #cont_cols
    #cat_cols
    #dropped_cols_stats - [(0, Dropped at CI Test), (1, Dropped at Correlation Test), 
        #(2, Dropped due at Chi-Squared Test), 

class stats_package:

    def __init__(self, data_file, column_dtypes, user_target_label):
        self.df = data_file

class categorical_target(stats_package):
    def __init__(self, data_file, column_dtypes, user_target_label):
        super().__init__(data_file, column_dtypes, user_target_label)
        self.target = user_target_label
        self.cont_cols = list({key:value for (key,value) in column_dtypes.items() if value == "float64" if key != user_target_label}.keys())
        self.cat_cols = list({key:value for (key,value) in column_dtypes.items() if value == "category" if key != user_target_label}.keys())
        self.dropped_cols_stats = {}

    def mean_confidence_interval(df:"two column dataframe", confidence=0.95):
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

    def continuous_tests_with_cat_target(self):
        """Preforms confidence interval test on columns with greater than 100 values"""
        removed_cols = []
        for col in self.cont_cols:
            if self.df[col].count() >= 100:
                ci = categorical_target.mean_confidence_interval(self.df[[col, self.target]])
                maxs = []
                mins = []
                totals = []
                for i in range(len(ci)):
                    maxs.append(ci[i][1])
                    mins.append(ci[i][0])
                    totals.append(ci[i][1] - ci[i][0])
                drop_col = np.array(max(maxs)) - np.array(min(mins)) < sum(totals)
                if drop_col == True:
                    self.df.drop(columns=[col], inplace=True)
                    self.dropped_cols_stats.update({col:0})
                    removed_cols.append(col)
                if mins == maxs:
                    self.df.drop(columns=[col], inplace=True)
                    self.dropped_cols_stats.update({col:0})
                    removed_cols.append(col)
        [self.cont_cols.remove(item) for item in removed_cols]

    
    def clear_over_correlated_columns(self):
        """Checks if two of the continuous columns have over .90 correlation, if so one of them is removed."""
        corr_list = []
        col_list = list(combinations(self.cont_cols,2))
        for col1,col2 in col_list:
            corr_list.append(self.df[col1].corr(self.df[col2]))
        drop_list = []
        for corr, cols in zip(corr_list, col_list):
            if cols[0] in drop_list:
                continue
            if corr > .9 :
                drop_list.append(cols[0])
                self.dropped_cols_stats.update({cols[0]:1})
        self.df.drop(columns = drop_list, inplace=True)

    def create_chi_table():
        """Created chi table for scoring"""
        p = np.array([0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005])
        df = np.array(list(range(1, 30)) + list(range(30, 101, 10))).reshape(-1, 1)
        np.set_printoptions(linewidth=130, formatter=dict(float=lambda x: "%7.3f" % x))
        table = chi2.isf(p, df)
        return table


    def check_chi(self):
        removed_cols = []
        for col in self.cat_cols:
            chi_inp = pd.crosstab(self.df[col], self.df[target])
            chi2, p, dof, expected = chi2_contingency(chi_inp.values)
            if np.array(i >= 5 for i in expected).all() == False:
                removed_cols.append(col)
                self.dropped_cols_stats.update({col:2})
            if create_chi_table()[dof-1][6] > chi2 or p > .05 :
                print("These variables are independent, failed to reject H0.")
            else:
                print("These variables are dependent, H0 rejected.")
            
class continuous_target(stats_package):
    def __init__(self, data_file, column_dtypes, user_target_label):
        super().__init__(data_file, column_dtypes, user_target_label)
        self.target = user_target_label
        self.cont_cols = list({key:value for (key,value) in column_dtypes.items() if value == "float64" if key != user_target_label}.keys())
        self.cat_cols = list({key:value for (key,value) in column_dtypes.items() if value == "category" if key != user_target_label}.keys())
        self.dropped_cols_stats = {}





df = pd.read_csv("test_data/IBM_Data.csv")
column_dtypes = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]
test = pop(df,"F647952", column_dtypes, "Attrition")
test.execute_phase_one()
test = categorical_target(test.df, test.column_dtypes, test.user_target_label)
test.continuous_tests_with_cat_target()
test.dropped_cols_stats
test.clear_over_correlated_columns()


test.cont_cols
test.cat_cols


#For tomorrow:
#Find out how to drop values > 90% correlation
#Thoughts: What if all columns that corr are dropped due to its correlation with the others? is that possiable? 

