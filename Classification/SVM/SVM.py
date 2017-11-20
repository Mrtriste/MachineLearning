# -*- coding:utf-8 -*-
import Q
from Solver import Solver

############### SVM class
class SVM:
	def __init__(self,kernel_type='Linear',degree=3,gamma,coef0,epsilon,C):
		self.param =  Q.SVM_Param(kernel_type,degree,gamma,coef0,epsilon,C)

	def fit(self,X,y):
		solver = Solver(self.param)
		model = solver.solve(X,y)

	def predict(self,X):
		pass
