# -*- coding:utf-8 -*- 

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
from XGBoost import *

def get_multi_data():
	centers = [[-5,3],[1,3],[-3,-3]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_image_data():
	digits = datasets.load_digits()
	return digits.data,digits.target

def test_multi():
	X,y = get_multi_data()
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = XGBoost()
	clf.fit(X_train[0:20,:],y_train[0:20])
	# y_pred = clf.predict(X_test)
	# correct_rate = 1-np.mean(y_test!=y_pred)
	# print 'correct_rate:',correct_rate

def test(X):
	X=100

if __name__=='__main__':
	# test_multi()
	# a = np.array([[2,3],[4,8],[1,7]],dtype=float)
	# b = np.array([1,10,100])
	# c=1
	# test(c)
	# print c
	# print np.sum(np.exp(a),axis=1)
	# print softmax(a)
	a = np.array([[5,2,3,8,6],[7,9,2,5,6]])
	print  np.argsort(a,axis=1)
	print max(1,2)
