# -*- coding=utf-8 -*-

import numpy as np 
from Tree import *

class Entry:
	def __init__(self):
		self.split_v = -1
		self.split_f = -1
		self.max_gain = 0
		self.l_weight = 0
		self.r_weight = 0

class Updater:
	def __init__(self,X,order,g,h,lamda,min_weight):
		self.hold = np.ones(X.shape[0])
		self.feat_index = [i for i in range(X.shape[1])]
		self.X = X
		self.order = order
		self.g = g
		self.h = h
		self.expand = []
		self.expand.append(0)
		self.position = np.zeros(X.shape[0],dtype=int)
		self.tree = Tree()
		self.lamda = lamda
		self.min_weight = min_weight

	def generate(self):
		max_depth = 6
		for depth in range(max_depth):
			self.find_split()
			self.reset_position()
			self.reset_expand()
			if len(self.expand)==0:
				break

	def find_split(self):
		position = self.position
		sum_g = np.zeros(self.tree.size())
		sum_h = np.zeros(self.tree.size())
		lst = []
		# calculate sum_g sum_h
		for i in range(position.shape[0]):
			if self.hold[i] == 1:
				nid = position[i]
				sum_g[nid] += self.g[i]
				sum_h[nid] += self.h[i]

		X = self.X; g =self.g; h = self.h

		entries = []
		for i in range(self.tree.size()):
			entries.append(Entry())

		# calculate gain
		for fid in range(X.shape[1]):
			last = []; G_L = []; G_R = []; H_L = []; H_R = []
			for i in range(self.tree.size()):
				last.append(None)
				G_L.append(0); G_R.append(sum_g[i])
				H_L.append(0); H_R.append(sum_h[i])
			for rid in self.order[:,fid]:
				nid = position[rid]
				if last[nid] == None:
					last[nid] = X[rid,fid]
					G_L[nid] = g[rid]; G_R[nid] -= g[rid]
					H_L[nid] = h[rid]; H_R[nid] -= g[rid]
				elif last[nid] != X[rid,fid]:
					new_gain = 0
					if H_L[nid] >= self.min_weight and H_R[nid] >=self.min_weight:
						gain_L = G_L[nid]*G_L[nid]/(H_L[nid]+self.lamda)
						gain_R = G_R[nid]*G_R[nid]/(H_R[nid]+self.lamda)
						new_gain = gain_L+gain_R

					if entries[nid].max_gain < new_gain:
						entries[nid].max_gain = new_gain
						entries[nid].split_f = fid 
						entries[nid].split_v = (last[nid]+X[rid,fid])*0.5
						entries[nid].l_weight = -G_L[nid]/(H_L[nid]+self.lamda)
						entries[nid].r_weight = -G_R[nid]/(H_R[nid]+self.lamda)
					last[nid] = X[rid,fid]
					G_L[nid] += g[rid]; H_L[nid] += h[rid]
					G_R[nid] -= g[rid]; H_R[nid] -= h[rid]

		# split
		for nid in self.expand:
			gain = (sum_g[nid]*sum_g[nid])/(sum_h[nid]+self.lamda)
			# print lst[i][0],gain,'score:',lst[i][3]
			if gain < entries[nid].max_gain:
				# print 'split:',lst[i][1],lst[i][2]
				self.tree[nid].set_split(entries[nid].split_f,entries[nid].split_v)
				self.tree[nid].set_left(self.tree.add_child(entries[nid].l_weight))
				self.tree[nid].set_right(self.tree.add_child(entries[nid].r_weight))
				# print 'child:',nid,self.tree[nid].get_left(),self.tree[nid].get_right()

	def reset_position(self):
		position = self.position
		for i in range(self.X.shape[0]):
			if self.hold[i] == 1:
				nid = position[i]
				for fid in self.feat_index:
					if (not self.tree[nid].is_leaf()) and self.tree[nid].get_split_fid()==fid:
						if self.X[i,fid] < self.tree[nid].get_split_v():
							position[i] = self.tree[nid].get_left()
						else:
							position[i] = self.tree[nid].get_right()

	def reset_expand(self):
		# set not split leaf to be old leaf
		lst = []
		for nid in self.expand:
			if not self.tree[nid].is_leaf():
				lst.append(self.tree[nid].get_left())
				lst.append(self.tree[nid].get_right())

		self.expand = lst

	def get_tree(self):
		return self.tree
