
# -*- coding:utf-8 -*-

import numpy as np 
import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def get_data():
	digits = datasets.load_digits()
	return digits.data, digits.target

def get_artificial_data():
	centers = [[-5,3],[4,1.5],[0,6]]
	X,y = make_blobs(n_samples=1500,centers=centers,random_state=40)
	color = np.array([''])
	transformation = [[0.4, 0.2], [-0.4, 1.2]]
	X = np.dot(X, transformation) + np.random.rand(1500,2)*2.8
	return X,y

def shuffle(X,y):
	n_samples = X.shape[0]
	for i in range(n_samples-1):
		idx = random.randint(i+1,n_samples-1)
		X[[i,idx]] = X[[idx,i]]
		y[[i,idx]] = y[[idx,i]]
	return X,y

class PerceptronMulti:
	def __init__(self,iter_num=25,alpha = 0.1):
		self.iter_num = iter_num
		self.alpha = alpha

	def _fit_binary(self,X,y):
		w = np.ones(X.shape[1])
		n_samples = X.shape[0]
		for it in range(self.iter_num):
			X,y = shuffle(X,y)
			for i in range(n_samples):
				z = np.dot(w,X[i])*y[i]
				if z < 0: # mis-classify driven!!!
					w += self.alpha*X[i]*y[i] 
		return w.tolist()

	def fit(self,X,y):
		self.class_set = np.unique(y)
		w = []
		for i in range(self.class_set.shape[0]):
			yi = np.ones(X.shape[0])
			yi[y!=self.class_set[i]] = -1
			w.append(self._fit_binary(X.copy(),yi))
		# self.w = np.array(w)
		self.w = preprocessing.normalize(w, norm='l2')

	def predict(self,X):
		scores = np.dot(X,self.w.T)
		y = scores.argmax(axis=1)
		return self.class_set[y]

def plot_figure(X,y,w):
	c = np.array(['r']*y.shape[0])
	c[y==0] = 'b'
	c[y==1] = 'g'

	plt.figure(figsize=(8,6))
	plt.scatter(X[:,1],X[:,2],c = c)
	############
	x_min = -1.5;x_max = 0.5
	def line(x0,w0):
		# w0+w1*x+w2*y=0  =>  y = (-w0-w1*x)/w2
		return (-w0[0]-w0[1]*x0)/w0[2]
	plt.plot([x_min,x_max],[line(x_min,w[0]),line(x_max,w[0])])
	plt.plot([x_min,x_max],[line(x_min,w[2]),line(x_max,w[2])])
	############
	y_min = -1;y_max = 1
	def line1(y0,w0):
		# w0+w1*x+w2*y=0  =>  x = (-w0-w2*y)/w1
		return (-w0[0]-w0[2]*y0)/w0[1]
	plt.plot([line1(y_min,w[1]),line1(y_max,w[1])],[y_min,y_max])

def exp1():
	X,y = get_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train, X_test, y_train, y_test = \
                train_test_split(X, y, test_size=0.5, random_state=np.random.RandomState(42))
	clf = PerceptronMulti(iter_num = 15,alpha = 0.01)
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1 - np.mean(y_pred!=y_test)
	print 'correct rate:',correct_rate

def exp2():
	X,y = get_artificial_data()
	X = preprocessing.scale(X)
	X = np.column_stack([[1]*X.shape[0],X])
	clf = PerceptronMulti(iter_num = 20)
	clf.fit(X,y)
	plot_figure(X,y,clf.w)
	plt.show()

if __name__ == '__main__':
	# exp1()
	exp2()
	
	
