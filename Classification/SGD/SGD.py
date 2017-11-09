# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
import random

def get_binary_data():
	centers = [[-5,3],[1,3]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_multi_data():
	centers = [[-5,3],[1,3],[-3,-3]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_image_data():
	digits = datasets.load_digits()
	return digits.data,digits.target

def shuffle(index):
	n = index.shape[0]
	for i in range(n-1):
		idx = random.randint(i+1,n-1)
		index[[i,idx]] = index[[idx,i]]

############### begin LossFunction
#http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.58.7377
#Section 4
class LossFunction:
	def deriv(self,y,p):
		# loss' is deriv about p, that's w*x
		return 0.0
		
class HingeLoss(LossFunction):
	def deriv(self,y,p):
		# loss = 1 - py if py < 1 else 0
		# loss' = -y
		z = p*y
		if z < 1.0:
			return -y
		return 0.0

class LogisticLoss(LossFunction):
	def deriv(self,y,p):
		# loss = ln(1+exp(-py))
		# loss' = (-y)*[exp(-py)/(1+exp(-py))] = (-y)/(1+exp(z))
		z = y*p
		if z > 18.0:
			return -y * np.exp(-z)
		if z < -18.0:
			return -y
		return -y / (1.0 + np.exp(z))

class ModifiedHuberLoss(LossFunction):
	def deriv(self,y,p):
		# 1. if py>1, loss = 0; 2. if -1<=py<=1, loss = (1-py)^2; 3.if py<-1,loss = -4py
		# 1. loss'=0; 2. loss' = 2(1-py)*(-y) 3. loss' = -4y
		z = p * y
		if z > 1:
			return 0.0
		if z <-1:
			return -4*y
		return 2*(1-z)*(-y)

class SquaredHingeLoss(LossFunction):
	def deriv(self,y,p):
		# 1. if py>1, loss = 0; 2. if py < 1, loss = (1-py)^2
		# 1. loss' = 0; 2. loss' = 2(1-py)*(-y)
		z = p * y
		if z > 1:
			return 0.0
		return 2 * (1 - z) * (-y)


############### end LossFunction
