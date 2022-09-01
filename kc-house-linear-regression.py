#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn import metrics

import statsmodels.api as sm


# In[14]:



df = pd.read_csv('../Downloads/kc_house_data.csv')
df


# In[15]:


df.corr(method='pearson') # check the correlation matrix


# In[16]:


# Scikit Learn
x = df['price'].values.reshape(-1,1)
y = df['sqft_living'].values

lr = LinearRegression(fit_intercept = True)
lr.fit(x, y)
y_pred = lr.predict(x)


# In[17]:


print('Coefficients = ', lr.coef_)
print('Intercept = ', lr.intercept_)
print('R^2 = ', lr.score(x, y))
print('Root MSE = ', math.sqrt(metrics.mean_squared_error(y, y_pred)))


# In[18]:


x = df['price']
y = df['sqft_living']

x2 = sm.add_constant(x)
ols = sm.OLS(y, x2)
est = ols.fit()
est.summary()


# In[19]:


plt.figure(0)
plt.title('Linear Regression Line')
plt.xlabel('price')
plt.ylabel('sqft_living')
plt.scatter(x, y,  color='black')
plt.plot(x, y_pred, color='blue', linewidth=3)


# In[ ]:


#Square feet of living has the highest R^2 and coefficient of determination 
#Square feet of lving has the least RMSE value 

