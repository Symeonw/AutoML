import stats_package
from phase_one_data_prep import phase_one_data_prep as pop
from data_validation import data_validation
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler




class phase_two_data_prep:

    def __init__(self, data_file, cat_cols, cont_cols, target):
        self.df = data_file
        self.cat_cols = cat_cols
        self.cont_cols = cont_cols
        self.target = target

    def prep_nans(self):
        self.df = self.df.loc[:,self.df.isnull().mean() < .5]
        x = [index for boolean, index in zip((self.df.isnull().sum(axis=1) < len(self.df.columns)/2),self.df.index) if boolean == True] # Collects all rows with
        #  more than 50% of data missing for removal. 
        self.df = self.df.loc[x,:]
        self.cat_cols = list(set(self.df.columns).intersection(self.cat_cols))
        self.cont_cols = list(set(self.df.columns).intersection(self.cont_cols))

    def prep_cats(self):
        cat = self.df[[self.cat_cols]]# Gets dataframe with all categorial columns
        cols = pd.get_dummies(cat)# Does OneHotEncoding
        self.df.drop(columns=self.cat_cols, inplace=True)# Drops non-encoded columns from dataframe
        self.df = pd.concat([self.df, cols], axis=1)# Replaces dropped cols with encoded ones

    def prep_conts(self):
        cont = self.df[[self.cont_cols]]# Gets dataframe with all continuous columns
        scaler = MinMaxScaler()# Initiates MinMaxScaler
        cols = scaler.fit_transform(cont)# Scales columns
        cols = pd.DataFrame(cols)
        cols.columns = self.cont_cols # Reassign column names
        self.df.drop(columns = self.cont_cols, inplace=True)# Removes non-scaled columns
        self.df = pd.concat([self.df, cols], axis=1)# Replaces non-scaled columns with scaled columns

    def final_clean(self):
        self.df.dropna(subset=[self.target], inplace=True)



#TODO:
# Test if continuous vaiables that passed CI testing should be classified as Categorical variabels and be encoded as such!!!!


# x = phase_two_data_prep(df, test.cat_cols, test.cont_cols, "dog")
# x.prep_nans()
# x.prep_cats()
# x.prep_conts()

