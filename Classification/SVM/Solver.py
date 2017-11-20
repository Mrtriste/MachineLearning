# -*- coding:utf-8 -*-

import numpy as np
from Q import Q

class SVM_Model:
	def __init__(self,alpha,rho):
		pass

class Solver:
	def __init__(self,param):
		self.param = param
		self.MAX_ITER = 100000
		self.TAU = 1e-12

	def setC(self):
		self.Cn = self.Cp = self.C

	def getC(self,i):
		return self.Cn if self.y[i]<0 else self.Cp

	def select_elements(self,G):
		INF = 1e12
		y = self.y
		select_i = -1; select_j = -1
		m = -INF; M = INF
		n = y.shape[0]
		# I_up: calculate m and select i
		for i in range(n):
			if y[i] == 1:
				if alpha[i] < self.Cp:
					if -G[i] >= m:
						m = -G[i]; select_i = i # calculate m and select i
			else:
				if alpha[i] > 0:
					if G[i] >= m:
						m = G[i]; select_i = i # calculate m and select i

		if select_i != -1:
			Qi = self.Q.getQ(select_i)

		select_j_min = INF
		#  I_low: calcute M and select j
		for t in range(n):
			if y[t] == 1:
				if alpha[t] > 0:
					if -G[t] < M:
						M = -G[t]; # calculate M
					# select j:
					# b_it = G[t] - yi*G[i] = G[t] + m
					b_it = G[t] + m
					if b_it > 0:
						aij = self.Q.get_Kii(select_i) + self.Q.get_Kii(t) - 2*y[i]*Qi[t]
						if aij > 0:
							res = -b_it*b_it/aij
						else:
							res = -b_it*b_it/self.TAU
						if res < select_j_min:
							select_j_min = res; select_j = t
			else:
				if alpha[t] < self.Cn:
					if G[t] < M:
						M = G[t] # calculate M
					# select j:
					# b_it = -G[t] - yi*G[i] = -G[t] + m
					b_it = -G[t] + m
					if b_it > 0:
						aij = self.Q.get_Kii(select_i) + self.Q.get_Kii(t) + 2*y[i]*Qi[t]
						if aij > 0:
							res = -b_it*b_it/aij
						else:
							res = -b_it*b_it/self.TAU
						if res < select_j_min:
							select_j_min = res; select_j = t
		if m -M < self.param.epsilon or select_j == -1:
			return (-1,-1)
		else:
			return (select_i,select_j)

	def cal_rho(self,alpha):
		pass

	def solve(self):
		X = self.X; y = self.y
		model = SVM_Model()
		n = y.shape[0]
		self.setC()
		# init
		p = np.full(n,-1)
		alpha = np.zeros(n)
		G = p.copy()
		self.Q = Q(X,y,self.param)
		Q = self.Q
		for i in range(n):
			row = Q.getQ(i)
			G += np.dot(row,alpha)

		max_iter = self.MAX_ITER
		for iter_cnt in range(max_iter):
			i,j = self.select_elements(G)
			if i == -1:
				break
			Qi = Q.getQ(i);Qj = Q.getQ(j)
			Ci = self.getC(i);Cj = self.getC(j)
			old_alpha_i = alpha[i]; old_alpha_j = alpha[j]

			# update alpha
			# --------------- yi!=yj
			if y[i]!=y[j]:
				aij = Q.get_Kii(i) + Q.get_Kii(j) + 2*Qi[j] # Q[i,j] = - K[i,j]
				if aij < 0:
					aij = self.TAU
				delta = (-G[i]-G[j])/aij
				diff = alpha[i] - alpha[j]
				alpha[i] += delta;alpha[j] += delta

				if delta > 0:
					if alpha[j] < 0:
						alpha[j] = 0; alpha[i] = diff
				else:
					if alpha[i] < 0:
						alpha[i] = 0; alpha[j] = -diff
				if diff > Ci - Cj:
					if alpha[i] > Ci:
						alpha[i] = Ci; alpha[j] = Ci - diff
				else:
					if alpha[j] > Cj:
						alpha[j] = Cj; alpha[i] = Cj + diff
			# --------------- yi == yj
			else:
				aij = Q.get_Kii(i) + Q.get_Kii(j) - 2*Qi[j]
				if aij < 0:
					aij = self.TAU
				delta = (G[i] - G[j])/aij
				add = alpha[i] + alpha[j]
				alpha[i] -= delta; alpha[j] += delta

				if add < Ci:
					if alpha[j] < 0:
						alpha[j] = 0; alpha[i] = add
				else:
					if alpha[i] > Ci:
						alpha[i] = Ci; alpha[j] = add - Ci
				if add < Cj:
					if alpha[i] < 0:
						alpha[i] = 0; alpha[j] = add
				else:
					if alpha[j] > Cj:
						alpha[j] = Cj; alpha[i] = add - Cj

			# update Gradient
			Q_NB = np.column_stack([Q.getQ(i),Q.getQ(j)])
			alpha_B = np.array([alpha[i]-old_alpha_j, alpha[j]-old_alpha_j])
			G += np.dot(Q_NB,alpha_B)

		rho = self.cal_rho(alpha)

		return SVM_Model(alpha,rho)
