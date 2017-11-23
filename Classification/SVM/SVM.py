# -*- coding:utf-8 -*-
import Q
import numpy as np
from Solver import Solver

############### SVM class
class SVM:
	def __init__(self,kernel_type='Linear',degree=3,gamma='auto',coef0=0.0,epsilon=1e-4,C=0.03):
		self.param =  Q.SVM_Param(kernel_type,degree,gamma,coef0,epsilon,C)

	def fit(self,X,y):
		solver = Solver(self.param,X,y)
		model = solver.solve()
		self.alpha = model.alpha
		self.b = -model.rho
		if self.param.kernel_type is 'Linear':
			self.w = np.dot(X.T,self.alpha*y)

	def predict(self,X):
		return np.sign(np.dot(X,self.w) + self.b).astype(int)
