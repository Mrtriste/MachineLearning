# -*- coding:utf-8 -*-

import random
import numpy as np 
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import preprocessing

def get_data():
	centers = [[-5,3],[4,1.5]]
	X,y = make_blobs(n_samples=1000,centers=centers,random_state=40)
	color = np.array([''])
	transformation = [[0.4, 0.2], [-0.4, 1.2]]
	X = np.dot(X, transformation) + np.random.rand(1000,2)*2.8
	return X,y

def shuffle(X,y):
	n_samples = X.shape[0]
	for i in range(n_samples-1):
		idx = random.randint(i+1,n_samples-1)
		X[[i,idx]] = X[[idx,i]]
		y[[i,idx]] = y[[idx,i]]
	return X,y

class PerceptionBin:
	def __init__(self,iter_num=25,alpha=0.1):
		self.iter_num = iter_num
		self.alpha = alpha

	def fit(self,X,y):
		X = np.mat(X);
		self.w = np.mat(np.zeros(X.shape[1])).T
		self.class_set = np.unique(y)
		y[y==self.class_set[0]] = -1;y[y==self.class_set[1]] = 1
		n_samples = X.shape[0]
		for it in range(self.iter_num):
			X,y = shuffle(X,y)
			for i in range(n_samples):
				self.w += self.alpha*X[i].T*y[i]

	def predit(self,X):
		scores = np.dot(X,self.w)
		y = (scores>0).astype(int)
		return self.class_set[y].ravel()

def plot_figure(X,y,w):
	plt.figure(figsize=(8,6))
	color = np.array(['b']*X.shape[0])
	color[y==1] = 'r'
	plt.scatter(X[:,1],X[:,2],c=color)
	y_min = X[:,2].min();y_max = X[:,2].max()

	def line(y0):
		# w0+w1*x+w2*y=0  =>  x = (-w0-w2*y)/w1
		return (-w[0,0]-w[2,0]*y0)/w[1,0]
	
	plt.plot([line(y_min),line(y_max)],[y_min,y_max])

if __name__ == '__main__':
	X,y = get_data()
	X = preprocessing.scale(X)
	X = np.column_stack([[1]*X.shape[0],X])
	X_train, X_test, y_train, y_test = \
                train_test_split(X, y, test_size=0.2, random_state=np.random.RandomState(42))
	clf = PerceptionBin()
	clf.fit(X_train,y_train)
	y_pred = clf.predit(X_test)
	correct_rate = 1 - np.mean(y_pred!=y_test)
	print 'error rate:',correct_rate
	plot_figure(X_train,y_train,clf.w)
	plot_figure(X_test,y_test,clf.w)
	plot_figure(X_test,y_pred,clf.w)
	plt.show()

