# -*- coding:utf-8 -*- 

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
from GBDT import *

def get_multi_data():
	n = 1000
	centers = [[-5,3],[1,3],[-3,-3]]
	X,y = make_blobs(centers = centers,n_samples = n,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(n,2)*2.5
	return X,y

def get_image_data():
	digits = datasets.load_digits()
	return digits.data,digits.target

def test_multi():
	X,y = get_multi_data()
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))

	eps = [0.01,0.03,0.1,0.3,1]
	for e in eps:
		clf = GBDT(11,6,e)
		clf.fit(X_train,y_train)
		y_pred = clf.predict(X_test)
		correct_rate = 1-np.mean(y_test!=y_pred)
		print 'correct_rate:',correct_rate ,'para:',e

def test_image():
	X,y = get_image_data()
	# X = np.column_stack([[1]*X.shape[0],X])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = GBDT()
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate

if __name__ == '__main__':
	# test_multi()
	test_image()
	# a = np.array([[1],[2],[3],[4],[5],[10],[11],[12],[13],[14]])
	# # a = np.array([[1],[2],[10],[11]])
	# # b = np.array([0,0,1,1])
	# b = np.array([0,0,0,0,0,1,1,1,1,1])
	# clf = GBDT(6)
	# clf.fit(a,b)


