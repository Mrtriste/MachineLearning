# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
import math

def get_data():
	n = 100; scale = 1000
	a = -3; b = 18
	x = np.random.rand(n,1)*scale
	y = a * x + b + (np.random.rand(n,1)-0.5)*(scale/10)
	return x,np.ravel(y)

def plot_data(x,y):
	plt.figure(figsize=(8,6))
	plt.scatter(x,y,c = 'b')


def plot_line(X,w):
	x_min = X.min();x_max = X.max()
	x_min_y = w[0] + w[1]*x_min
	x_max_y = w[0] + w[1]*x_max
	plt.plot([x_min,x_max],[x_min_y,x_max_y])

class Ridge:
	def __init__(self,alpha=1.0):
		self.alpha = alpha

	def fit(self,X,y):
		inv = np.array((np.mat(X.T)*np.mat(X) + self.alpha*np.eye(X.shape[1])).I)
		self.w = np.dot(np.dot(inv,X.T),y)

	def predict(self,X):
		return np.dot(X,self.w)


if __name__ == '__main__':
	X,y = get_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X[:,1:] = preprocessing.scale(X[:,1:])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	alpha = [0.01,0.03,0.1,0.3,0,1,3,10]
	for a in alpha:
		clf = Ridge(a)
		clf.fit(X_train,y_train)
		y_pred = clf.predict(X_test)
		e = y_pred - y_test
		print 'avr error:',math.sqrt(np.dot(e,e)/y_test.shape[0]),' parameter:',a
	# plot_data(X_train[:,1],y_train)
	# plot_line(X_train[:,1],clf.w)
	# plt.show()