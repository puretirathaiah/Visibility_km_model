# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:40:00 2021

@author: Pureti
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

import pickle

# data preperation
# drop the rows if they contain single NaN value
# drop the columns that do not contain any useful information
# 'Day', 'SLP', 'PP', 'RA', 'SN', 'TS', 'FG'
# remove the rows if they have missed data    

data = pd.read_csv(f'weather_data.csv')
data = data.dropna(how='any', axis=0)    
data = data.drop(columns=['Day', 'SLP', 'PP', 'RA', 'SN', 'TS', 'FG'])
for col in data.columns:
    data = data[~data[col].isin(['-'])]
    
# Independent features
X = data.loc[:, ['T', 'TM', 'Tm', 'H', 'V', 'VM', 'VG']]
for col in X.columns:
    X[col] = pd.to_numeric(X[col])

# Dependent feature (average visibility (km))
y = pd.to_numeric(data['VV'])

seed = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.20, 
                                                    random_state=seed)

# define the number of folds for the cross-validation
n_folds = 5
kfold = KFold(n_splits=n_folds, random_state=seed, shuffle=True)

# values for hyper parameters tuning
params = {'n_estimators':[100, 150, 200, 250, 300, 500],
          'max_depth':[1,2,4,6]}

score = 'neg_mean_squared_error'
grid = GridSearchCV(GradientBoostingRegressor(), param_grid=params, 
                    scoring=score, cv=kfold, n_jobs=-1, verbose=1)

# train the model
grid_result = grid.fit(X_train, y_train)

print(f'Randomised search CV best params: {grid_result.best_params_}')
print(f'Randomised search CV best score: {grid_result.best_score_}')
print(f'Randomised search CV best estimator: {grid_result.best_estimator_}')

# choose the best estimator
gbr = grid_result.best_estimator_

# fit the model
gbr.fit(X_train, y_train)


# Save the model to disk
pickle.dump(gbr, open('visibility_model.pkl','wb'))

# Loading the model to use to predict
model = pickle.load(open('visibility_model.pkl','rb'))

#print(model.predict([[-5.8, 4, -7.5, 92, 5.7, 13, 25.2]])) """



    
