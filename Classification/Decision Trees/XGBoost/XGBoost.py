# -*- coding:utf-8 -*-
import numpy as np 
from Booster import *

def softmax(X):
	exp_X = np.exp(X)
	sum = np.sum(exp_X,axis=1)
	return np.divide(exp_X.T,sum).T

class XGBoost:
	def __init__(self,lamda=0.1):
		self.cfg = {}
		self.cfg['max_iter'] = 10
		self.cfg['n_class'] = 2
		self.cfg['lamda'] = lamda

	def fit(self,X,y):
		self.X = X; self.y = y;
		n_class = np.unique(y).shape[0]
		if n_class == 2: n_class = 1
		self.n_class = n_class
		self.cfg['n_class'] = n_class
		n = X.shape[0];m = X.shape[1]
		p = np.empty([n,n_class])
		g = np.empty([n,n_class]); h = np.empty([n,n_class])
		self.p = p; self.g = g; self.h = h
		self.Trees = []

		order = np.argsort(X,axis=1)

		booster = Booster(X,order) 

		for i in range(self.cfg['max_iter']):
			info = {
				'n_class':n_class,
				'grad':self.g,
				'hess':self.h,
				'lamda':self.cfg['lamda']
			}
			booster.train(info)
			self.Trees.append(booster.get_trees())

	def predict(self,X):
		pass

	def _predict_raw(self,X):
		p = self.p
		for i in range(X.shape[0]):
			for c in range(self.n_class):
				# trees: n_class tree
				p_sum = 0
				for trees in self.Trees:
					tree = tree[c]
					p_sum += tree.get_score(X[i,:])
				p[i,c] = p_sum

	def _get_gradient(self):
		X = self.X; y = self.y
		sm = softmax(self.p)
		print sm
		for i in range(0,X.shape[0]):
			for j in range(0,self.n_class):
				if j == y[i]: 
					g[i,j] = sm[i,j] - 1
				else: 
					g[i,j] = sm[i,j]
				h[i,j] = sm[i,j]*(1-sm[i,j]) #*2.0
		print g
		print h
