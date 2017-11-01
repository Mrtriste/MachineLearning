# -*- coding:utf-8 -*-

import numpy as np 
from sklearn import datasets
from sklearn.model_selection import train_test_split

def get_data():
	digits = datasets.load_digits()
	return digits.data, digits.target

def fit(X,t):
	X = np.mat(X);t = np.mat(t).T
	w = np.mat(np.zeros(X.shape[0])).T
	return w

def predit(X,w):
	pass

if __name__ == '__main__':
	X,y = get_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train, X_test, y_train, y_test = \
                train_test_split(X, y, test_size=0.2, random_state=np.random.RandomState(42))
	w = fit(X_train,y_train)
	y_pred = predit(X_test,w)
	error_rate = 1 - np.mean(y_pred==y_test)
	print error_rate

