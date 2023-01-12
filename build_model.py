
import streamlit as st

lib = '''from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor 
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import numpy as np
import pickle 
import time
'''
data = '''# load dataset 
iron = pd.read_csv('MiningProcess_Flotation_Plant_Database.csv')
iron = iron.drop(['% Silica Feed','date','% Silica Concentrate'],
                 axis=1)
'''
ironinfo ='''# dataset observations are of 'object' dtype
iron.info()
'''

iii = '''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 737453 entries, 0 to 737452
Data columns (total 21 columns):
 #   Column                        Non-Null Count   Dtype 
---  ------                        --------------   ----- 
 0   % Iron Feed                   737453 non-null  object
 1   Starch Flow                   737453 non-null  object
 2   Amina Flow                    737453 non-null  object
 3   Ore Pulp Flow                 737453 non-null  object
 4   Ore Pulp pH                   737453 non-null  object
 5   Ore Pulp Density              737453 non-null  object
 6   Flotation Column 01 Air Flow  737453 non-null  object
 7   Flotation Column 02 Air Flow  737453 non-null  object
 8   Flotation Column 03 Air Flow  737453 non-null  object
 9   Flotation Column 04 Air Flow  737453 non-null  object
 10  Flotation Column 05 Air Flow  737453 non-null  object
 11  Flotation Column 06 Air Flow  737453 non-null  object
 12  Flotation Column 07 Air Flow  737453 non-null  object
 13  Flotation Column 01 Level     737453 non-null  object
 14  Flotation Column 02 Level     737453 non-null  object
 15  Flotation Column 03 Level     737453 non-null  object
 16  Flotation Column 04 Level     737453 non-null  object
 17  Flotation Column 05 Level     737453 non-null  object
 18  Flotation Column 06 Level     737453 non-null  object
 19  Flotation Column 07 Level     737453 non-null  object
 20  % Iron Concentrate            737453 non-null  object
dtypes: object(21)
memory usage: 118.2+ MB
'''

chgdtype = '''# replace ',' by '.' 
# use 'regex=True'
numIron = iron.replace(',','.',regex=True)
'''

floatchg = '''# converting dtype of observations
# from  'object' to 'float'
numIron = numIron.astype('float')
numIron.info()'''

fff = '''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 737453 entries, 0 to 737452
Data columns (total 21 columns):
 #   Column                        Non-Null Count   Dtype  
---  ------                        --------------   -----  
 0   % Iron Feed                   737453 non-null  float64
 1   Starch Flow                   737453 non-null  float64
 2   Amina Flow                    737453 non-null  float64
 3   Ore Pulp Flow                 737453 non-null  float64
 4   Ore Pulp pH                   737453 non-null  float64
 5   Ore Pulp Density              737453 non-null  float64
 6   Flotation Column 01 Air Flow  737453 non-null  float64
 7   Flotation Column 02 Air Flow  737453 non-null  float64
 8   Flotation Column 03 Air Flow  737453 non-null  float64
 9   Flotation Column 04 Air Flow  737453 non-null  float64
 10  Flotation Column 05 Air Flow  737453 non-null  float64
 11  Flotation Column 06 Air Flow  737453 non-null  float64
 12  Flotation Column 07 Air Flow  737453 non-null  float64
 13  Flotation Column 01 Level     737453 non-null  float64
 14  Flotation Column 02 Level     737453 non-null  float64
 15  Flotation Column 03 Level     737453 non-null  float64
 16  Flotation Column 04 Level     737453 non-null  float64
 17  Flotation Column 05 Level     737453 non-null  float64
 18  Flotation Column 06 Level     737453 non-null  float64
 19  Flotation Column 07 Level     737453 non-null  float64
 20  % Iron Concentrate            737453 non-null  float64
dtypes: float64(21)
memory usage: 118.2 MB'''
sep = '''X = numIron.iloc[:,:-1]
Y = numIron[['% Iron Concentrate']]'''
targetplot = '''# plot target data
plt.figure(figsize=(20,7))
plt.plot(Y)
plt.ylabel('% Iron Concentration')
plt.suptitle('% Iron Concentration in froth',fontsize=30)
plt.show()'''
gridcode='''baseModel = XGBRegressor(random_state=42)
alpha = [0.1, 0.2]
max_depth = [10,15]
n_estimators = [100,200]
param_grid = dict(alpha=alpha,
                  max_depth=max_depth,
                  n_estimators=n_estimators)
param_grid'''
gridsearch = '''grid = GridSearchCV(estimator=baseModel,
                    param_grid=param_grid,
                    cv=2,verbose=10,
                    scoring='neg_mean_squared_error')
grid_result= grid.fit(X_train,Y_train)
# best params 
results = grid_result.best_params_
results'''
bReg = '''# initialize xgbregressor with best params 

xgbReg = XGBRegressor(n_estimators=200,
                      alpha=0.2,
                      max_depth=15,
                      random_state=42)
# train XGBRegressor on training regressor 
start = time.time()
xgbReg.fit(X_train,Y_train)
end = time.time()
print(f'XGBoost regressor training time : {round(end-start,2)}')'''
score = '''# training r2score
print(f'Testing r2score : {xgbReg.score(X_train,Y_train)}')
# testing r2score
print(f'Testing r2score : {xgbReg.score(X_test,Y_test)}')'''
regLine = '''plt.figure(figsize=(20,7))
plt.plot(Y[30000:40000].values,alpha=0.85,color='black',
         label='Actual values')
plt.plot(xgbReg.predict(X[30000:40000]).ravel(),
         color='red',label='Predicted values')
plt.legend()
score = r2_score(Y[30000:40000].values,
                 xgbReg.predict(X[30000:40000]).ravel())
plt.ylabel('% Iron Concentration')
plt.suptitle(f'linear regressor score : {score}',fontsize=30)
plt.show()'''

exp = '''with open('iron_concentrate','wb') as file:
    pickle.dump(xgbReg,file)'''

posDev = '''pos = np.where(actual-pred == max(actual-pred))[0][0]
a = actual[pos]
p = pred[pos]
print(f'+ve deviation : {max(actual-pred)}')
print(f'Actual : {a}\nPredicted : {p}')
print(f'Max +ve deviation : {(a-p)*100/a}')'''

negDev = '''pos = np.where(actual-pred == min(actual-pred))[0][0]
a = actual[pos]
p = pred[pos]
print(f'-ve deviation : {min(actual-pred)}')
print(f'Actual : {a}\nPredicted : {p}')
print(f'Max -ve deviation : {(a-p)*100/a}')'''

def buildModel():
    st.header('Importing required libraries')
    st.code(lib,language='python')
    st.header('Load results obtained from experiment')
    st.code(data,language='python')
    st.header('overview of data')
    st.code(ironinfo,language='python')
    st.code(iii,language=None)
    st.header('Perform required manipulation')
    st.code(chgdtype,language='python')
    st.code(floatchg,language='python')
    st.code(fff,language=None)
    st.header('separate features and target')
    st.code(sep,language='python')
    st.header('target \'% Iron Concentrate in froth\'')
    st.code(targetplot,language='python')
    st.image('targetplot.png')
    st.header('XGBRegressor Model')
    st.code(gridcode,language='python')
    st.write("{'alpha': [0.1, 0.2], 'max_depth': [10, 15], 'n_estimators': [100, 200]}")
    st.code(gridsearch,language='python')
    st.write("{'alpha': 0.2, 'max_depth': 15, 'n_estimators': 200}")
    st.code("print(f'XGBRegressor with best params give MSE -> {-grid_result.best_score_}')",language='python')
    st.write('XGBRegressor with best params give MSE -> 0.129079359973713')
    st.header('Initialize XGBRegressor with best params')
    st.code(bReg,language='python')
    st.write("XGBoost regressor training time : 677.4")
    st.code(score,language='python')
    st.code('''Testing r2score : 0.9970130925484375
Testing r2score : 0.9329263868329568''',language=None)
    st.header('Regression Line')
    st.code(regLine,language='python')
    st.image('regplot.png')
    st.header('Highest deviation from Actual values')
    st.code('''actual = Y.values.ravel()
pred = xgbReg.predict(X)''',language='python')
    st.code(posDev,language='python')
    st.code('''+ve dir deviation : 4.264281921386726
Actual : 66.68
Predicted : 62.41571807861328
Max +ve dir deviation : 6.395143853309426''',language=None)
    st.code(negDev,language='python')
    st.code('''-ve dir deviation : -3.4249346923828057
Actual : 64.18
Predicted : 67.60493469238281
Max -ve dir deviation : -5.336451686479909''',language=None)
    st.header('Analysing Homoscedasticity')
    st.image('hsce.png')
    st.header('Analysing distribution of residuals')
    st.image('resdist.png')
    st.header('Exporting ML model')
    st.code(exp,language='python')
    















    
    
