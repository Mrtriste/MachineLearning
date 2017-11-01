# -*- coding:utf-8 -*-
# http://www.cnblogs.com/darkknightzh/p/6117528.html color

import numpy as np 
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

def sigmoid(inX):
	return 1.0/(1+np.exp(-inX))

def fit(X,t):
	n_samples = X.shape[0]; n_features = X.shape[1]
	X = np.mat(X);t = t.reshape((t.shape[0],1))
	w = np.mat(np.zeros((n_features,1)))
	iter_num = 50; alpha = 0.05
	for i in range(iter_num):
		y = np.mat(sigmoid(X*w))
		w -= X.T*(y-t)
	return w

if __name__ == '__main__':
	X,y = get_data()
	X = preprocessing.scale(X)
	color = np.array(['r']*y.shape[0])
	color[y==1] = 'g'
	plt.figure(1,figsize=(8,6))
	plt.scatter(X[:,1],X[:,2],c=color)

	w = fit(X,y)
	y_min = X[:,2].min();y_max = X[:,2].max()

	def line(y0):
		# w0+w1*x+w2*y=0  =>  x = (-w0-w2*y)/w1
		return (-w[0,0]-w[2,0]*y0)/w[1,0]
	
	plt.plot([line(y_min),line(y_max)],[y_min,y_max])

	plt.show()
