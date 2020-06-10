from scipy.stats import t, sem, chi2, chi2_contingency
import pandas as pd
import numpy as np
from phase_one_data_prep import phase_one_data_prep as pop
from itertools import combinations

#Documentation
    #cont_cols
    #cat_cols
    #dropped_cols_stats - [(0, Dropped at CI Test), (1, Dropped at Correlation Test), 
        #(2, Dropped due at Chi-Squared Test), (3, Dropped at Linear Correlation test)

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

    def mean_confidence_interval(df:"two column dataframe", confidence=0.90):
        """Takes in two columns: target(Category) and test column (continous)."""
        target_len = len(df.iloc[:,1].unique())
        ci = []
        for i in range(target_len): #Accessing all unique categories in target, running all groupings of contious variables though test.
            data = df[df.iloc[:,1] == df.iloc[:,1].unique()[i]].iloc[:,0]#Gets i'th unique value from target unique values. 
            a = 1.0 * np.array(data)
            n = len(a)
            m, se = np.mean(a), sem(a)
            h = se * t.ppf((1 + confidence) / 2., n-1)
            ci.append([m-h,m+h])
        return ci

    def ci_test(self):
        """Preforms confidence interval test on columns with greater than 100 values"""
        removed_cols = []
        for col in self.cont_cols:
            print(f"CI TEST FOR {col}")
            ci = continuous_target.mean_confidence_interval(self.df[[self.target, col]])
            if ci != []:
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
            else:
                removed_cols.append(col)
        self.df.drop(columns=removed_cols, inplace=True)
        [self.cat_cols.remove(item) for item in removed_cols]
    
    def clear_over_correlated_columns(self):
        """Checks if two of the continuous columns have over .90 correlation, if so one of them is removed."""
        removed_cols = []
        corr_list = []
        col_list = list(combinations(self.cont_cols,2))
        for col1,col2 in col_list:
            print(f"OVER CORR TEST FOR {col1} {col2}")
            corr_list.append(self.df[col1].corr(self.df[col2]))
        for corr, cols in zip(corr_list, col_list):
            if cols[0] in removed_cols:
                continue
            if corr > .9 :
                removed_cols.append(cols[0])
                self.dropped_cols_stats.update({cols[0]:1})
        self.df.drop(columns = removed_cols, inplace=True)
        [self.cont_cols.remove(item) for item in removed_cols]

    def create_chi_table():
        """Created chi table for scoring"""
        p = np.array([0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005])
        df = np.array(list(range(1, 30)) + list(range(30, 101, 10))).reshape(-1, 1)
        np.set_printoptions(linewidth=130, formatter=dict(float=lambda x: "%7.3f" % x))
        table = chi2.isf(p, df)
        return table


    def chi_test(self):
        removed_cols = []
        for col in self.cat_cols:
            print(f"CHI TEST FOR {col}")
            chi_inp = pd.crosstab(self.df[col], self.df[self.target])
            chi2, p, dof, expected = chi2_contingency(chi_inp.values)
            if np.array(i >= 5 for i in expected).all() == False:
                continue
            if categorical_target.create_chi_table()[dof-1][6] > chi2 or p > .05 :
                removed_cols.append(col)
                self.dropped_cols_stats.update({col:2})
        [self.cat_cols.remove(item) for item in removed_cols]
        self.df.drop(columns=removed_cols,inplace=True)
            
class continuous_target(stats_package):
    def __init__(self, data_file, column_dtypes, user_target_label):
        super().__init__(data_file, column_dtypes, user_target_label)
        self.target = user_target_label
        self.cont_cols = list({key:value for (key,value) in column_dtypes.items() if value == "float64" if key != user_target_label}.keys())
        self.cat_cols = list({key:value for (key,value) in column_dtypes.items() if value == "category" if key != user_target_label}.keys())
        self.dropped_cols_stats = {}

    def clear_over_correlated_columns(self):
        """Checks if two of the continuous columns have over .90 correlation, if so one of them is removed."""
        removed_cols = []
        corr_list = []
        col_list = list(combinations(self.cont_cols,2))#Gets all combinations of all continuous columns in group sizes of two
        for col1,col2 in col_list:
            print(f"OVER CORR TEST FOR {col1} {col2}")
            corr_list.append(self.df[col1].corr(self.df[col2]))
        for corr, cols in zip(corr_list, col_list):
            if cols[0] in removed_cols:
                continue
            if corr > .9 :
                removed_cols.append(cols[0])
                self.dropped_cols_stats.update({cols[0]:1})
        self.df.drop(columns = removed_cols, inplace=True)
        [self.cont_cols.remove(item) for item in removed_cols]


    def lin_corr_test(self):
        """Checks if contious columns have at least +/- .20  correlation with the target column."""
        removed_cols = []
        for col in self.cont_cols:
            print(f"LINCORR TEST FOR {col}")
            if (self.df[col].corr(self.df[self.target]) < .2) | (self.df[col].corr(self.df[self.target]) < -.2):#testing linear corr, drops if greater than .2 or lower than -.2
                if self.df[col].count() >= 120:#this section preforms a CI test on those dropped columns
                    ci = continuous_target.mean_confidence_interval(self.df[[col, self.target]], .99, 0.005)
                    if len(ci) > 1:
                        maxs = []
                        mins = []
                        totals = []
                        for i in range(len(ci)):
                            maxs.append(ci[i][1])
                            mins.append(ci[i][0])
                            totals.append(ci[i][1] - ci[i][0])
                        drop_col = np.array(max(maxs)) - np.array(min(mins)) < sum(totals)
                        if drop_col == True:
                            self.dropped_cols_stats.update({col:3})
                            removed_cols.append(col)
                        if mins == maxs:
                            self.dropped_cols_stats.update({col:3})
                            removed_cols.append(col)
                    else:
                        removed_cols.append(col)
                        self.dropped_cols_stats.update({col:3})
                        
                else:
                    removed_cols.append(col)
                    self.dropped_cols_stats.update({col:3})
        self.df.drop(columns=removed_cols, inplace=True)
        [self.cont_cols.remove(item) for item in removed_cols]


    def mean_confidence_interval(df:"two column dataframe", confidence=0.90, occurance=0.001):
        """Takes in two columns: test(Category) and target (continous)."""
        ci = []
        col_list = pd.DataFrame(df.iloc[:,0].value_counts(normalize=True)>occurance).reset_index()#Get only cat values that occur at least 1% of the time
        col_list = col_list[col_list.iloc[:,1] == True].iloc[:,0]
        print(len(col_list))
        if len(col_list) < 1:
            return ci
        for cat in col_list: #Accessing all unique categories, running all groupings of contious variables though test.
            data = df[df.iloc[:0] == cat].iloc[:,1]
            a = 1.0 * np.array(data)
            n = len(a)
            m, se = np.mean(a), sem(a)
            h = se * t.ppf((1 + confidence) / 2., n-1)
            ci.append([m-h,m+h])
        return ci

    def ci_test(self):
        """Preforms confidence interval test on columns with greater than 120 values"""
        removed_cols = []
        for col in self.cat_cols:
            print(f"CI TEST FOR {col}")
            if self.df[col].count() >= 120:# 130 was chosen because you need at least 30 values per cat and at least 100 values per column. 
                ci = continuous_target.mean_confidence_interval(self.df[[col, self.target]])
                if len(ci) > 1:
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
                else:
                    removed_cols.append(col)
                    self.dropped_cols_stats.update({col:0})

        self.df.drop(columns=removed_cols, inplace=True)
        [self.cat_cols.remove(item) for item in removed_cols]




    

# #Categorical Testing
# df = pd.read_csv("test_data/internet_usage.csv")
# column_dtypes = [0,0,1,0,1,0,1,1]
# test = pop(df,"F647952", column_dtypes, "target")
# test.execute_phase_one()
# test = categorical_target(test.df, test.column_dtypes, test.user_target_label)
# test.ci_test()
# test.clear_over_correlated_columns()
# test.chi_test()
# test.dropped_cols_stats


# #Continuous Testing
# df = pd.read_csv("test_data/IBM_Data.csv")
# column_dtypes = [0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0]
# test = pop(df,"F647952", column_dtypes, "Age")
# test.execute_phase_one()
# test = continuous_target(test.df, test.column_dtypes, test.user_target_label)
# test.clear_over_correlated_columns()
# test.lin_corr_test()
# test.ci_test()
# test.dropped_cols_stats

