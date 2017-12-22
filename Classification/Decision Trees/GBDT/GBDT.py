# -*- coding:utf-8 -*-

import numpy as np 
from Updater import *

def softmax(X):
	X_ = X.T - np.max(X,axis=1)
	X_exp = np.exp(X_)
	X_sum = np.sum(np.exp(X_),axis=0) 
	return (X_exp/X_sum).T

class GBDT:
	def __init__(self,max_iter=10,max_depth=6,eps=1.0):
		self.max_iter = max_iter
		self.max_depth = max_depth
		self.eps = eps

	def fit(self,X,y):
		self.X = X; self.y = y
		n = X.shape[0]; m = X.shape[1]
		n_class = np.unique(y).shape[0]
		self.n_class = n_class
		self.n = n; self.m = m 
		p = np.zeros((n,n_class))
		g = np.empty([n,n_class])
		self.g = g
		Trees = []
		self.Trees = Trees
		order = np.argsort(X,axis=0)
		updater = Updater(order,self.max_depth,self.eps)
		for it in range(self.max_iter):
			print 'iter:',it
			self.get_grad(p)
			trees = []
			for j in range(n_class):
				# print g[:,j]
				tree = updater.fit(X,g[:,j])
				trees.append(tree)
			Trees.append(trees)
			self.predict_raw(X,p)
	

	def predict(self,X):
		p = np.zeros((X.shape[0],self.n_class))
		self.predict_raw(X,p)
		sm = softmax(p)
		return sm.argmax(axis=1)

	def predict_raw(self,X,p):
		Trees = self.Trees 
		it_num = len(Trees)
		for i in range(X.shape[0]):
			for k in range(self.n_class):
				sum_v = 0
				for it in range(it_num):
					tree = Trees[it][k]
					sum_v += tree.get_score(X[i,:])
				p[i,k] = sum_v

	def get_grad(self,p):
		sm = softmax(p)
		for j in range(self.n_class):
			for i in range(self.n):
				if j == self.y[i]:
					self.g[i,j] = sm[i,j] - 1
				else:
					self.g[i,j] = sm[i,j]
