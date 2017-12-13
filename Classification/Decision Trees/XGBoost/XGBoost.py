# -*- coding:utf-8 -*-
import numpy as np 
from Booster import *

def softmax(X):
	X_ = (X.T - np.max(X,axis=1)).T
	exp_X = np.exp(X_)
	sum = np.sum(exp_X,axis=1)
	return np.divide(exp_X.T,sum).T

class XGBoost:
	def __init__(self,lamda=0.1,min_weight = 1.0,max_iter = 10):
		self.cfg = {}
		self.cfg['max_iter'] = max_iter
		self.cfg['n_class'] = 2
		self.cfg['lamda'] = lamda
		self.cfg['min_weight'] = min_weight
 
	def fit(self,X,y):
		self.X = X; self.y = y;
		n_class = np.unique(y).shape[0]
		self.n_class = n_class
		self.cfg['n_class'] = n_class
		n = X.shape[0];m = X.shape[1]
		p = np.empty([n,n_class])
		g = np.empty([n,n_class]); h = np.empty([n,n_class])
		self.p = p; self.g = g; self.h = h
		self.Trees = []

		order = np.argsort(X,axis=0)
		booster = Booster(X,order) 

		for i in range(self.cfg['max_iter']):
			print 'iter:',i
			self._predict_raw(X)
			self._get_gradient()
			info = {
				'n_class':n_class,
				'grad':self.g,
				'hess':self.h,
				'lamda':self.cfg['lamda'],
				'min_weight':self.cfg['min_weight']
			}
			booster.train(info)
			self.Trees.append(booster.get_trees())

	def predict(self,X):
		self._predict_raw(X)
		sm = softmax(self.p[0:X.shape[0],:])
		return sm.argmax(axis = 1)

	def _predict_raw(self,X):
		p = self.p
		p.fill(0.5)
		if len(self.Trees) == 0:
			return
		for i in range(X.shape[0]):
			for c in range(self.n_class):
				# trees: n_class tree
				p_sum = p[i,c]
				for trees in self.Trees:
					tree = trees[c]
					p_sum += tree.get_score(X[i,:])
				p[i,c] = p_sum

	def _get_gradient(self):
		X = self.X; y = self.y
		g = self.g; h = self.h
		sm = softmax(self.p)
		for i in range(0,X.shape[0]):
			for j in range(0,self.n_class):
				if j == y[i]: 
					g[i,j] = sm[i,j] - 1
				else: 
					g[i,j] = sm[i,j]
				h[i,j] = sm[i,j]*(1-sm[i,j]) #*2.0
