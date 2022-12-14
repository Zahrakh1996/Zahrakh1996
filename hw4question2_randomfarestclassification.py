# -*- coding: utf-8 -*-
"""HW4Q2-RandomFarestClassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYkYpJ-kbre_LN6bxtL1z1cq0BvojXL2
"""

#Q2

pip install numpy

pip install pandas

pip install scikit-learn

import numpy as np
import pandas as pd
import sklearn

from google.colab import files
data_to_load = files.upload()

import io
df = pd.read_csv(io.BytesIO(data_to_load['census.csv']))

df.head()

df.columns

from sklearn.preprocessing import LabelEncoder

#transforming string to numerical data
le=LabelEncoder()
i=[1,2,3,4,5,6,7,11,12]
for i in df:
    df[i]=le.fit_transform(df[i])

df.head()

from sklearn.model_selection import train_test_split

X=df.iloc[:,0:12].values
y=df.iloc[:,12].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40,random_state=101)

#i)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

print(model.predict([[22	,7	,9,	4,1	,1,	4,	1	,25,	0	,39	,38]]))

#ii)

model.score(X_test,y_test)

