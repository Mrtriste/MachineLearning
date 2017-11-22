# -*- coding:utf-8 -*-

import numpy as np
import math

KERNEL_TYPE=['Linear','Poly','RBF']

class SVM_Param:
	def __init__(self,kernel_type,degree,gamma,coef0,epsilon,C):
		self.kernel_type = kernel_type
		self.degree = degree
		self.gamma = gamma
		self.coef0 = coef0
		self.epsilon = epsilon
		self.C = C

class Kernel:
	def __init__(self,X,y,param):
		self.X = X
		self.y = y
		self.param = param
		if param.gamma is 'auto':
			self.param.gamma = 1.0/self.X.shape[1]
		self.kernels = {
			'Linear':self.LinearKernel,
			'Poly':self.PolyKernel,
			'RBF':self.RBFKernel
		}
		self.kernel_function = self.kernels[param.kernel_type]
		n = y.shape[0]
		self.K = np.zeros(n)
		for i in range(n):
			self.K[i] = self.kernel_function(i,i)
		# print self.K

	def LinearKernel(self,i,j):
		return np.dot(self.X[i],self.X[j])

	def PolyKernel(self,i,j):
		return math.pow(self.param.gamma*np.dot(self.X[i],self.X[j])+self.param.coef0,self.param.degree)

	def RBFKernel(self,i,j):
		return np.exp(-self.param.gamma*np.dot(self.X[i]-self.X[j],self.X[i]-self.X[j]))

	def k_function(self,xi,x):
		pass

class Q(Kernel):
	def get_Kii(self,i):
		return self.K[i]

	def getQ(self,i):
		n = self.y.shape[0]
		data = np.zeros(n)
		for j in range(n):
			data[j] = self.y[i]*self.y[j]*self.kernel_function(i,j)
		return data



	
