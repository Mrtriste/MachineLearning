# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
import random
from sklearn import svm

def get_binary_data():
	# centers = [[-5,3],[1,3]]
	centers = [[-2,6],[1,3]]
	n = 1000
	X,y = make_blobs(centers = centers,n_samples = n,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(n,2)*2.5
	return X,y


X,y = get_binary_data()
y[y==0] = -1
# X = np.column_stack([[1]*X.shape[0],X])
X_train,X_test,y_train,y_test = \
			train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))

C = [0.0001,0.0003,0.001,0.003,0.01,0.03,0.1,0.3,1,3]
for c in C:
	model = svm.SVC(kernel='linear', C=c)
	model.fit(X_train,y_train)
	y_p = model.predict(X_test)
	print np.mean((y_p==y_test).astype(int))