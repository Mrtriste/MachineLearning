# -*- coding:utf-8 -*-

import numpy as np
from Q import Q

class SVM_Model:
	def __init__(self,alpha,rho):
		self.alpha = alpha
		self.rho = rho

class Solver:
	def __init__(self,param,X,y):
		self.param = param
		self.MAX_ITER = 1000000
		self.TAU = 1e-12
		self.X =X
		self.y = y

	def setC(self):
		self.Cn = self.param.C
		self.Cp = self.param.C

	def getC(self,i):
		return self.Cn if self.y[i]<0 else self.Cp

	def select_elements(self,alpha,G):
		INF = 1e12
		y = self.y
		select_i = -1; select_j = -1
		m = -INF; M = INF
		n = y.shape[0]
		# I_up: calculate m and select i
		for i in range(n):
			if y[i] == 1:
				if alpha[i] < self.getC(i):
					if -G[i] >= m:
						m = -G[i]; select_i = i # calculate m and select i
			else:
				if alpha[i] > 0:
					if G[i] >= m:
						m = G[i]; select_i = i # calculate m and select i

		if select_i != -1:
			Qi = self.Q_.getQ(select_i)

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
						aij = self.Q_.get_Kii(select_i) + self.Q_.get_Kii(t) - 2*y[i]*Qi[t]
						if aij > 0:
							res = -b_it*b_it/aij
						else:
							res = -b_it*b_it/self.TAU
						if res <= select_j_min:
							select_j_min = res; select_j = t
			else:
				if alpha[t] < self.Cn:
					if G[t] < M:
						M = G[t] # calculate M
					# select j:
					# b_it = -G[t] - yi*G[i] = -G[t] + m
					b_it = -G[t] + m
					if b_it > 0:
						aij = self.Q_.get_Kii(select_i) + self.Q_.get_Kii(t) + 2*y[i]*Qi[t]
						if aij > 0:
							res = -b_it*b_it/aij
						else:
							res = -b_it*b_it/self.TAU
						if res <= select_j_min:
							select_j_min = res; select_j = t
		# print m- M
		if m -M < self.param.epsilon or select_j == -1:
			print select_i, select_j
			return (-1,-1)
		else:
			return (select_i,select_j)

	def cal_rho(self,alpha,G):
		n = G.shape[0]
		INF = 1e12
		y = self.y
		neg_M = -INF; neg_m = INF
		sum_ = 0; cnt = 0
		sum_1 = 0; cnt1 = 0
		for i in range(n):
			res = y[i]*G[i]
			if alpha[i]>0 and alpha[i]<self.getC(i):
				cnt += 1
				sum_ += res

			if alpha[i]>0:
				cnt1+=1
				sum_1 += res

			if y[i] == 1:
				if alpha[i] == self.getC(i):
					if neg_M < res:
						neg_M = res
				if alpha[i] == 0:
					if neg_m > res:
						neg_m = res
			else:
				if alpha[i] == 0:
					if neg_M < res:
						neg_M = res
				if alpha[i] == self.getC(i):
					if neg_m > res:
						neg_m = res
		print 'rho:',(sum_1/cnt1),' ',(neg_m+neg_M)/2.0,' ',neg_M,' ',neg_m
		if cnt > 0:
			print '*********'
			return sum_/cnt
		return (neg_m+neg_M)/2.0
			
	def solve(self):
		X = self.X; y = self.y
		n = y.shape[0]
		self.setC()
		# init
		p = np.full(n,-1,dtype=np.float64)
		alpha = np.zeros(n,)
		G = p.copy()
		self.Q_ = Q(X,y,self.param)
		Q_ = self.Q_
		for i in range(n):
			row = Q_.getQ(i)
			G[i] += np.dot(row,alpha)

		max_iter = self.MAX_ITER
		for iter_cnt in range(max_iter):
			if (iter_cnt+1)%10000 == 0:
				print (iter_cnt+1)/10000
			i,j = self.select_elements(alpha,G)
			if i == -1:
				break
			Qi = Q_.getQ(i);Qj = Q_.getQ(j)
			Ci = self.getC(i);Cj = self.getC(j)
			old_alpha_i = alpha[i]; old_alpha_j = alpha[j]

			# update alpha
			# --------------- yi!=yj
			if y[i]!=y[j]:
				aij = Q_.get_Kii(i) + Q_.get_Kii(j) + 2*Qi[j] # Q[i,j] = - K[i,j]
				if aij <= 0:
					aij = self.TAU
				delta = (-G[i]-G[j])/aij
				diff = alpha[i] - alpha[j]
				alpha[i] += delta;alpha[j] += delta

				if diff > 0:
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
				aij = Q_.get_Kii(i) + Q_.get_Kii(j) - 2*Qi[j]
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

			# print alpha
			# update Gradient
			Q_NB = np.column_stack([Q_.getQ(i),Q_.getQ(j)])
			alpha_B = np.array([alpha[i]-old_alpha_i, alpha[j]-old_alpha_j])
			# print Q_NB.shape,alpha_B.shape,G.shape
			G += np.dot(Q_NB,alpha_B)

		# print alpha
		rho = self.cal_rho(alpha,G)

		return SVM_Model(alpha,rho)
