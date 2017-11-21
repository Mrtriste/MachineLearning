# -*- coding:utf-8 -*-
import Q
import numpy as np
from Solver import Solver

############### SVM class
class SVM:
	def __init__(self,kernel_type='Linear',degree=3,gamma='auto',coef0=0.0,epsilon=0.1,C=1.0):
		self.param =  Q.SVM_Param(kernel_type,degree,gamma,coef0,epsilon,C)

	def fit(self,X,y):
		solver = Solver(self.param,X,y)
		model = solver.solve()
		self.alpha = model.alpha
		self.b = -model.rho
		if self.param.kernel_type is 'Linear':
			m = X.shape[1]; n = X.shape[0]
			self.w = np.ones(m)
			for i in range(m):
				sum_ = 0
				for j in range(n):
					sum_ += y[j]*self.alpha[j]*X[j,i]
				self.w[i] = sum_

	def predict(self,X):
		pass
