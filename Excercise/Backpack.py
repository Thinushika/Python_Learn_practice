#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy import misc


# In[2]:


pwd


# In[3]:


backpack = pd.read_csv(r'C:\Users\TJ\Desktop\Smart Backpack\Code Practices\Project ML\datasets\backpack.csv')


# In[4]:


backpack.head()


# In[5]:


print(backpack.describe())


# In[6]:


print((backpack.groupby('Status')).size())


# In[7]:


plt.rcParams['figure.figsize']=[15,12]


# In[8]:


backpack.plot(kind = 'box',
          subplots = True,
          layout = (4,4),
          sharex = False,
          sharey = False)
plt.show()


# In[9]:


backpack.hist()
plt.show()


# In[10]:


from pandas.plotting import scatter_matrix
scatter_matrix(backpack)
plt.show()


# In[18]:


from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


# In[20]:


import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))


# In[12]:


y = backpack['Status']
X = backpack.drop('Status', axis = 1)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                   test_size = 0.25,
                                                                   random_state = 0)
print(X.head())
print('')
print(y.head())


# In[14]:


from sklearn.model_selection import GridSearchCV

algorithms = []
scores = []
names =[]

algorithms.append(('Logistic Regression', LogisticRegression()))
algorithms.append(('K-Nearest Neighbors', KNeighborsClassifier()))
algorithms.append(('Decision Tree Classifier', DecisionTreeClassifier()))

for name, algo in algorithms:
    k_fold = model_selection.KFold(n_splits=10,
                                   random_state=0)
    
    #applying k-cross validation
    cvResults = model_selection.cross_val_score(algo, 
                                                X_train, 
                                                y_train,
                                                cv = k_fold,
                                                scoring = 'accuracy')
    
    scores.append(cvResults)
    names.append(name)
    print(str(name)+':'+str(cvResults.mean()))


# In[15]:


fig = plt.figure() 
fig.suptitle('Algorithm Comparison') 
ax = fig.add_subplot(111) 
plt.boxplot(scores) 
ax.set_xticklabels(names) 
plt.show()


# In[16]:


for name, algo in algorithms: 
    clf = algo 
    clf.fit(X_train, y_train) 
    y_pred = clf.predict(X_test) 
    pred_score = accuracy_score(y_test, y_pred) 
  
    print(str(name)+' : '+str(pred_score)) 
    print('') 
    print('Confusion Matrix: '+str(confusion_matrix(y_test, y_pred))) 
    print(classification_report(y_test, y_pred)) 


# In[ ]:




