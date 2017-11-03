# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
import random

def get_binary_data():
	centers = [[-5,3],[1,-2]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_multi_data():
	centers = [[-5,2],[-1.5,-1],[-1,5]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_image_data():
	digits = datasets.load_digits()
	return digits.data,digits.target

def shuffle(index):
	n = index.shape[0]
	for i in range(n):
		idx = i+random.randint(1,n-1)
		index[[i,idx]] = index[[idx,i]]

############### begin LossFunction
class LossFunction:
	def deriv(self,y,p):
		pass
		
class HingeLoss(LossFunction):
	def deriv(self,y,p):
		pass

class SquareLoss(LossFunction):
	def deriv(self,y,p):
		pass

############### end LossFunction

############### begin SGD classification class
'''
	support penality: none,l2
	support learning rate: constant,optimal,PA1,PA2
	support loss function: hinge,square_loss
'''
class SGD:
	LOSS_FUNCTION = {
		'hinge':(HingeLoss,),
		'squareloss':(SquareLoss,)
	}

	def __init__(self,iter_num=20,loss_type='squareloss',
				 eta0=0.1,learning_rate='constant',penality='l2'):
		self.iter_num = iter_num
		self.loss_type = loss_type
		self.loss_function = self.LOSS_FUNCTION[loss_type][0]()
		self.eta0 = eta0
		self.learning_rate = learning_rate
		self.penality = penality

	def _fit_binary(self,X,y):
		n_samples = X.shape[0];n_features = X.shape[1]
		self.w = np.random.rand(n_features)
		for it in range(iter_num):
			shuffle(self.index)
			for i in range(n_samples):
				Xi = X[self.index[i]];yi = y[self.next[i]]
				pass

	def _fit_multi(self,X,y):
		pass

	def fit(self,X,y):
		self.class_set = np.unique(y)
		self.index = np.arange(X.shape[0])
		if self.class_set.shape[0] == 2:
			_fit_binary(X,y)
		else:
			_fit_multi(X,y)

	def predict(self,X):
		pass

############### end SGD class

def plot_samples(X,y):
	x_start = 0
	if np.mean(X[:,0])==1:
		x_start += 1
	c_lst = ['r','g','b','y']
	y_set = np.unique(y)
	color = np.array([c_lst[0]]*y.shape[0])
	for i in range(1,y_set.shape[0]):
		color[y==y_set[i]] = c_lst[i]
	plt.figure(figsize=(8,6))
	plt.scatter(X[:,x_start],X[:,x_start+1],c = color)

def test_binary():
	X,y = get_binary_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train,y_train,X_test,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = SGD()
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate

	plot_samples(X,y)


def test_multi():
	X,y = get_multi_data()
	plot_samples(X,y)

def test_image():
	X,y = get_image_data()

if __name__ == '__main__':
	# test_binary()
	# plt.show()
	b = SGD()
