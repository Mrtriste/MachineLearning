# -*- coding:utf-8 -*-

import numpy as np
from Q import Q

class SVM_Model:
	def __init__(self):
		pass

class Solver:
	def __init__(self,param):
		self.param = param
		self.MAX_ITER = 100000
		self.TAU = 1e-12

	def select_elements(self):
		pass

	def solve(self,X,y):
		model = SVM_Model()
		n = y.shape[0]
		# init
		p = np.full(n,-1)
		alpha = np.zeros(n)
		G = p.copy()
		Q = Q(X,y,self.param)
		for i in range(n):
			row = Q.getQ(i)
			G += np.dot(row,alpha)

		max_iter = self.MAX_ITER
		for iter_cnt in range(max_iter):
			i,j = self.select_elements()
			Qi = Q.getQ(i);Qj = Q.getQ(j)

			# update alpha
			# --------------- yi!=yj
			if y[i]!=y[j]:
				aij = Q.get_Kii(i) + Q.get_Kii(j) + 2*Qi[j]
				if aij < 0:
					aij = self.TAU
				delta = (-G[i]-G[j])/aij
				diff = alpha[i] - alpha[j]
				alpha[i] += delta;alpha[j] += delta
				if delta > 0:
					pass
				else:
					pass
				if diff > 
			else:
				pass




		return model
