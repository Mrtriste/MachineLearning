# -*- coding:utf-8 -*-

import numpy as np 
from RegTree import *
import math

def loss(y,p):
	return (y-p)*(y-p)

MAX = 1e12

class Entry:
	def __init__(self):
		self.split_f = -1
		self.split_v = -1
		self.min_loss = MAX
		self.l_value = 0
		self.r_value = 0

class Updater:
	def __init__(self,order,max_depth,eps):
		self.order = order
		self.max_depth = max_depth
		self.eps = eps

	def fit(self,X,y):
		tree = RegTree()
		self.tree = tree
		tree[0].set_value(np.mean(y))
		self.pos = np.zeros(X.shape[0],dtype=int)
		self.expand = [0]
		for depth in range(self.max_depth):
			# print '------------depth:',depth,self.expand
			self.split(X,y)
			self.reset_position(X)
			self.reset_expand(X)
			if len(self.expand)==0:
				break
		return tree

	def split(self,X,y):
		pos = self.pos; expand = self.expand
		order = self.order; tree = self.tree

		sum_loss = [0 for i in range(self.tree.size())]
		num = [0 for i in range(self.tree.size())]

		entries = [Entry() for i in range(tree.size())]

		for i in range(X.shape[0]):
			nid = pos[i]
			sum_loss[nid] += loss(tree[nid].get_value(),y[i])
			num[nid] += 1

		# print 'sumloss:',sum_loss,num

		_r_sum = [0 for i in range(tree.size())]
		for i in range(X.shape[0]):
			_r_sum[pos[i]] += y[i]

		# calculate split loss
		for fid in range(X.shape[1]):
			# init helper array
			l_sum = [0 for i in range(tree.size())]
			r_sum = [_r_sum[i] for i in range(tree.size())]

			l_loss = [0 for i in range(tree.size())]
			r_loss = [sum_loss[i] for i in range(tree.size())]

			l_num = [0 for i in range(tree.size())]
			r_num = [num[i] for i in range(tree.size())]

			last = [None for i in range(tree.size())]

			for rid in order[:,fid]:
				nid = pos[rid]
				x = X[rid,fid]
				xx = y[rid]
				if last[nid] == None:
					l_loss[nid] = self._add_to_left(l_loss[nid],xx,0,xx,0,0)
					r_mean = r_sum[nid]/r_num[nid]
					r_mean_ = (r_sum[nid]-xx)/(r_num[nid]-1)
					r_loss[nid] = self._del_fr_right(r_loss[nid],xx,r_mean,r_mean_,r_sum[nid],r_num[nid])
				else:
					if last[nid] != x:
						new_loss = l_loss[nid] + r_loss[nid]
						if new_loss < entries[nid].min_loss:
							entries[nid].min_loss = new_loss
							entries[nid].split_f = fid
							entries[nid].split_v = (x+last[nid])*0.5
							entries[nid].l_value = l_sum[nid]/l_num[nid]
							entries[nid].r_value = r_sum[nid]/r_num[nid]

					l_mean = l_sum[nid]/l_num[nid]
					l_mean_ = (l_sum[nid]+xx)/(l_num[nid]+1)
					l_loss[nid] = self._add_to_left(l_loss[nid],xx,l_mean,l_mean_,l_sum[nid],l_num[nid])
					r_mean = r_sum[nid]/r_num[nid]
					try:
						if r_num[nid] == 1:r_mean_ = 0.0
						else: r_mean_ = (r_sum[nid]-xx)/(r_num[nid]-1)
					except RuntimeWarning,e:
						print r_sum[nid],xx,r_num[nid]
					r_loss[nid] = self._del_fr_right(r_loss[nid],xx,r_mean,r_mean_,r_sum[nid],r_num[nid])
			
				l_sum[nid] += xx; r_sum[nid] -= xx
				l_num[nid] += 1; r_num[nid] -= 1
				last[nid] = x

		# split
		for nid in expand:
			# print 'minloss',entries[nid].min_loss,sum_loss[nid]
			if entries[nid].min_loss < sum_loss[nid]:
				tree[nid].set_split(entries[nid].split_f,entries[nid].split_v)
				tree[nid].set_left(tree.add_child(entries[nid].l_value))
				tree[nid].set_right(tree.add_child(entries[nid].r_value))
				tree[nid].set_loss(entries[nid].min_loss if entries[nid].min_loss>1e-6 else 0)

	def reset_position(self,X):
		pos = self.pos; expand = self.expand
		tree = self.tree
		for i in range(X.shape[0]):
			nid = pos[i]
			if not tree[nid].is_leaf():
				fid = tree[nid].get_split_f()
				if X[i,fid] < tree[nid].get_split_v():
					pos[i] = tree[nid].get_left()
				else:
					pos[i] = tree[nid].get_right()

	def reset_expand(self,X):
		# reset 
		lst = []
		for nid in self.expand:
			e = math.sqrt(self.tree[nid].get_loss()/X.shape[0])
			if not self.tree[nid].is_leaf() and e>self.eps:
				lst.append(self.tree[nid].get_left())
				lst.append(self.tree[nid].get_right())
		self.expand = lst


	def _add_to_left(self,l_loss,x,l_mean,l_mean_,l_sum,l_num):
		return l_loss + x*x -2*(l_mean_- l_mean)*l_sum - 2*x*l_mean_+(l_num+1)*l_mean_*l_mean_- l_num*l_mean*l_mean

	def _del_fr_right(self,r_loss,x,r_mean,r_mean_,r_sum,r_num):
		return r_loss - x*x -2*(r_mean_- r_mean)*(r_sum-x)+2*x*r_mean- r_num*r_mean*r_mean+(r_num-1)*r_mean_*r_mean_
