# -*- coding:utf-8 -*- 

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
from GBDT import *

def get_multi_data():
	n = 20
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

	clf = GBDT(1)
	# X_train = X_train[0:50,:];y_train = y_train[0:50]
	# X_train = np.array([[1],[2],[3],[4],[5],[11],[12],[13],[14],[15]])
	# y_train = np.array([0,0,0,0,0,1,1,1,1,1])
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	# print y_pred
	# print y_test
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate #,'para:',l,m

if __name__ == '__main__':
	a = np.array([[1,3,4],[5,6,7],[3,10,6],[4,6,8]],dtype=float)
	# print softmax(a)
	# for i in a[:,0]:
	# 	print i
	# t = [0 for i in range(10)]
	# print t
	# print 1e12
	# test_multi()
	a = np.array([[1],[2],[3],[4],[5],[10],[11],[12],[13],[14]])
	b = np.array([0,0,0,0,0,1,1,1,1,1])
	clf = GBDT(1)
	clf.fit(a,b)

