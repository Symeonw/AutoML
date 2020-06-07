from phase_one_data_prep import phase_one_data_prep as pop
from phase_two_data_preparation import phase_two_data_prep as pop2
from data_validation import data_validation
import pandas as pd
import numpy as np


import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#TODO:
# Determine how many folds for CV in round_one_grid_search


class machine_learning():

    def __init__(self, data_file, user_target_label):
        self.df = data_file
        self.target = user_target_label
        self.score = {}

    
    def continuous_target(self):
        pass

class categorical_target(machine_learning):

    def __init__(self, data_file, user_target_label):
        super().__init__(data_file, user_target_label)
        self.target = user_target_label
        self.df = data_file

    def split_data(self):
        X = self.df.drop(columns=self.target)
        y = self.df[self.target]
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.25, random_state=123, stratify=y)
        return X_train, X_test, y_train, y_test


    def model_selection(self):
        if len(self.df[self.target].value_counts()) == 2:

            self.model = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10)
            
        else:
            self.model = xgb.XGBClassifier(objective="objective=multi:softmax", n_estimators=10)

    def build_model(self):
        self.model.fit(X_train, y_train)
        self.score.update(100,self.model.score(X_train, y_train))

    def round_one_grid_seach(self):
        params = {
            "eta" : [0.01, 0.1, 0.3],
        "max_depth":range(3, 10, 2),
        "gamma" : [0, 0.1, 0.2, 0.3],
        "min_child_weight" : [.01, .1, 1]
        }
        grid_search = GridSearchCV(self.model, params, cv = 4)
        

param_test1 = {

}

grid_search = GridSearchCV(xg_cl, param_test1, cv = 4, scoring= "accuracy")
grid_search.fit(X_train, y_train)
cvxg_cl = grid_search.best_estimator_
cvxg_cl.score(X_val, y_val)
grid_search.best_params_


xg_cl = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10, eta = 0.01, gamma = 0, max_depth = 5, min_child_weight = 1)

param_test2 = {
    "reg_lambda": [0.1,0.5,1],
    "reg_alpha": [0,0.01,0.1,1],
    "subsample": [0.7,0.8,0.9],
    "min_child_weight" : [.01, .1, 1]
}

grid_search = GridSearchCV(xg_cl, param_test2, cv = 4, scoring= "accuracy")
grid_search.fit(X_train, y_train)
cvxg_cl = grid_search.best_estimator_
cvxg_cl.score(X_val, y_val)
grid_search.best_params_