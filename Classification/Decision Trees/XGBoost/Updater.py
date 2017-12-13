# -*- coding=utf-8 -*-

import numpy as np 
from Tree import *

class Updater:
	def __init__(self,X,order,g,h,lamda):
		self.hold = np.ones(X.shape(0))
		self.feat_index = [i for i in range(X.shape[1])]
		self.X = X
		self.order = order
		self.g = g
		self.h = h
		self.expand = []
		self.expand.append(0)
		self.position = np.zeros(X.shape[0])
		self.tree = Tree()
		self.lamda = lamda

	def generate(self):
		max_depth = 6
		for depth in range(max_depth):
			self.find_split()
			self.reset_position()
			self.reset_expand()

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

		# calculate gain
		for nid in self.expand:
			max_gain = 0; split_v = -1; split_f = -1
			l_weight=0; r_weight = 0
			for fid in self.feat_index:
				first_id = self.order[0]
				last = X[first_id,fid]
				G_L = g[first_id]; G_R = sum_g[nid]-g[first_id]
				H_L = h[first_id]; H_R = sum_h[nid]-h[first_id]
				for rid in self.order[1:]:
					if self.hold[rid] == 1:
						new_gain = (G_L*G_L/(H_L+self.lamda))+(G_R*G_R/(H_R+self.lamda))
						if max_gain < new_gain:
							max_gain = new_gain
							split_f = fid
							split_v = (last+X[rid,fid])*0.5
							l_weight = -G_L/(H_L+self.lamda)
							r_weight = -G_R/(H_R+self.lamda)
						last = X[rid,fid]
						G_L += g[rid]; H_L += h[rid]
						G_R -= g[rid]; H_R -= h[rid]
			lst.append((max_gain,split_f,split_v,l_weight,r_weight))

		# split
		for nid in self.expand:
			gain = (sum_g[nid]*sum_g[nid])/(sum_h[nid]+self.lamda)
			if gain < lst[nid][0]:
				self.tree[nid].set_split(lst[nid][1],lst[nid][2])
				self.tree[nid].set_left(self.add_child(lst[nid][3]))
				self.tree[nid].set_right(self.add_child(lst[nid][4]))

	def reset_position(self):
		position = self.position
		for i in range(self.X.shape[0]):
			if self.hold[i] == 1:
				rid = position[i]
				for fid in self.feat_index:
					if !self.tree[nid].is_leaf() 
						and self.tree[nid].get_split_fid()==fid:
						if self.X[i,fid] < self.tree[nid].get_split_v():
							position[i] = self.tree[nid].get_left()
						else:
							position[i] = self.tree[nid].get_right()

	def reset_expand(self):
		# set not split leaf to be old leaf
		for nid in self.expand:
			if self.tree[nid].is_leaf():
				self.tree[nid].set_right(-2)

		# reset expand
		lst = []
		tree = self.tree
		for i in range(tree.size()):
			if tree[i].is_leaf() and !tree[i].is_old_leaf():
				lst.append(i)

		self.expand = lst

	def get_tree(self):
		return self.tree
