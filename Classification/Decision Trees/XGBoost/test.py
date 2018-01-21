# -*- coding:utf-8 -*- 

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
from XGBoost import *

def get_multi_data():
	n = 10000
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
	# lamda = [0.01,0.03,0.1,0.3,1,3]
	lamda = [10,30,60,100]
	min_w = [0.1,0.3,1]
	# lamda = [3]
	# min_w = [0.1]
	for l in lamda:
		for m in min_w:
			clf = XGBoost(l,m,13)
			# X_train = np.array([[1],[2],[3],[4],[5],[11],[12],[13],[14],[15]])
			# y_train = np.array([0,0,0,0,0,1,1,1,1,1])
			clf.fit(X_train,y_train)
			y_pred = clf.predict(X_test)
			# print y_pred
			# print y_test
			correct_rate = 1-np.mean(y_test!=y_pred)
			print 'correct_rate:',correct_rate,'para:',l,m

def test_image():
	X,y = get_image_data()
	# X = np.column_stack([[1]*X.shape[0],X])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = XGBoost(10,1)
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate


if __name__=='__main__':
	test_multi()
	# not work on image
	# test_image()
