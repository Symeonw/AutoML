 from scipy.stats import t, sem, chi2, chi2_contingency
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
#Documentation
    #cont_cols
    #cat_cols
    #

class statistical_package:

    def __init__(self, data_file, column_dtypes, user_target_label):
        #del phase_one.df
        self.df = data_file
        self.user_target_label = user_target_label
        self.cont_cols = list({key:value for (key,value) in column_dtypes.items() if value == "float64"}.keys())
        self.cat_cols = list({key:value for (key,value) in column_dtypes.items() if value == "category"}.keys())

    def mean_confidence_interval(df:"two column dataframe", target, confidence=0.95):
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
        self.ci_results = {}
        self.target = self.df[f"{user_target_label}"]
        for col in cont_cols:
            if len(col.count()) >= 200:
                x_len = len(x)
                maxs = []
                mins = []
                sec = []
                for i in range(len(x)):
                    maxs.append(x[i][1])
                    mins.append(x[i][0])
                    sec.append(x[i][1] - x[i][0])
                drop_col = np.array(max(maxs)) - np.array(min(mins)) < sum(sec)
                if drop_col == True:
                    self.df.drop(columns=f"{col}", inplace=True)



                





for i in range(len(df.EducationField.unique())):
    print (df.EducationField.unique()[i])


x = mean_confidence_interval(df[["DailyRate", "Attrition"]], "Attrition")

from random import shuffle

def test(x):
    loop = []
    for t in range(1000):
        shuffle(x)
        mins = []
        for i in range(1,len(x)):
            mins.append(min(np.array(max(x[0], x[i])) - np.array(min(x[0], x[i]))))
        if max(mins) > 0:
            loop.append(1)
        else:
            loop.append(0)
    return loop

l = test(x)
min(l)
mins
# Find if there are any CI's that don't overlap, if so then we keep the column, else we drop





import seaborn as sns

sns.catplot(x="Age", y="Attrition", data=df, kind="violin")