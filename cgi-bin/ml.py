#!/usr/bin/python36
print("content-type: html/text")
print()

# coding: utf-8

# In[18]:

#import cgi
import subprocess as sp
from keras.models import Sequential
from keras.layers import Dense

# optimizer: change the value of weight and biases: to looking for minimum cost
from keras.optimizers import Adam, SGD



#f=cgi.FieldStorage()
#a=f.getvalue('f')

#print(a)
model = Sequential()


# In[3]:


# units: how many output value
# input_shape: how many input value
# Dense: as its core do linear function, means if we dont apply any activation function, so it is linear activation function
model.add(Dense(units = 1, input_shape=(1,)))


# In[4]:


#model.summary()

# here we have to 2 parameter, that is  "weight and bias"


# In[5]:


model.compile(optimizer = Adam(lr=0.8), loss='mean_squared_error')


# In[6]:


import pandas as pd
df = pd.read_csv('/root/Desktop/weight-height.csv')


# In[7]:


X = df[['Height']].values
y_true = df['Weight'].values


# In[8]:


# find value w and b, to have minimum loss
model.fit(X, y_true, epochs=40,verbose=0)


#b In[9]:


y_pred = model.predict(X)


# In[10]:


W, B = model.get_weights()


# In[11]:


# Evaluating Model Performance
from sklearn.metrics import r2_score
print("The R2 score is {:0.3f}".format(r2_score(y_true, y_pred)))


# In[12]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y_true,
                                                    test_size=0.2)


# In[13]:


# reset the weight to again train, detraining 

W[0, 0] = 0.0
B[0] = 0.0
model.set_weights((W, B))


# In[14]:


model.fit(X_train, y_train, epochs=50, verbose=0)


# In[15]:


y_train_pred = model.predict(X_train).ravel()
y_test_pred = model.predict(X_test).ravel()


# In[16]:


from sklearn.metrics import mean_squared_error as mse


# In[17]:


print("The Mean Squared Error on the Train set is:\t{:0.1f}".format(mse(y_train, y_train_pred)))
print("The Mean Squared Error on the Test set is:\t{:0.1f}".format(mse(y_test, y_test_pred)))

