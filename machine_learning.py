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

#To define
#self.
#   rogs, score, model, rtgs, type

#score
#   100,200

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


    def model_selection(self):
        if len(self.df[self.target].value_counts()) == 2:
            self.model = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10)
            self.type = 0
        else:
            self.model = xgb.XGBClassifier(objective="objective=multi:softmax", n_estimators=10)
            self.type = 1

    def build_model(self):
        self.model.fit(X_train, y_train)
        mscore = self.model.score(X_train, y_train)
        self.score.update({100: mscore})

    def round_one_grid_seach(self):
        params = {
            "eta" : [0.01, 0.1, 0.3],
        "max_depth":range(3, 10, 2),
        "gamma" : [0, 0.1, 0.2, 0.3],
        "min_child_weight" : [.01, .1, 1]
        }
        grid_search = GridSearchCV(self.model, params, cv = 4, scoring="accuracy")
        grid_search.fit(X_train, y_train)
        estimators = grid_search.best_estimator_
        escore = estimators.score(X_train, y_train)
        self.score.update({200: escore})
        self.rogs = grid_search.best_params_
        if self.type == 0:
            self.model = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10, eta = self.rogs.get("eta"), gamma = \
                self.rogs.get("gamma"), max_depth = self.rogs.get("max_depth"), min_child_weight = self.rogs.get("min_child_weight"))
        else:
            self.model = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10, eta = self.rogs.get("eta"), gamma = \
                self.rogs.get("gamma"), max_depth = self.rogs.get("max_depth"), min_child_weight = self.rogs.get("min_child_weight"))

    def round_two_grid_search(self):

        params = {
        "reg_lambda": [0.1,0.5,1],
        "reg_alpha": [0,0.01,0.1,1],
        "subsample": [0.7,0.8,0.9],
        "min_child_weight" : [.01, .1, 1]
                    }
        grid_search = GridSearchCV(self.model, params, cv = 4, scoring="accuracy")
        grid_search.fit(X_train, y_train)
        estimators = grid_search.best_estimator_
        escore = estimators.score(X_train, y_train)
        self.score.update({300: escore})
        self.rtgs = grid_search.best_params_
        if self.type == 0:
            self.model = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10, eta = self.rogs.get("eta"), gamma = \
                self.rogs.get("gamma"), max_depth = self.rogs.get("max_depth"),\
                    reg_lambda = self.rtgs.get("reg_lambda"), reg_alpha = self.rtgs.get("reg_alpha"), subsample = self.rtgs.get("subsample"),\
                        min_child_weight=self.rtgs.get("min_child_weight"))
        else:
            self.model = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10, eta = self.rogs.get("eta"), gamma = \
                self.rogs.get("gamma"), max_depth = self.rogs.get("max_depth"),\
                    reg_lambda = self.rtgs.get("reg_lambda"), reg_alpha = self.rtgs.get("reg_alpha"), subsample = self.rtgs.get("subsample"),\
                        min_child_weight=self.rtgs.get("min_child_weight"))

    def final(self):
        score = self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        print(score)


final = categorical_target(x.df, test.target)
final.split_data()
final.model_selection()
final.build_model()
final.round_one_grid_seach()
final.round_two_grid_search()
final.final()

