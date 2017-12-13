# -*- coding=utf-8 -*-

import numpy as np 
from Tree import *

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

		# calculate gain
		for nid in self.expand:
			X = self.X; g =self.g; h = self.h
			max_gain = 0; split_v = -1; split_f = -1
			l_weight=0; r_weight = 0
			for fid in self.feat_index:
				first_id = self.order[0,fid]
				last = X[first_id,fid]
				G_L = g[first_id]; G_R = sum_g[nid]-g[first_id]
				H_L = h[first_id]; H_R = sum_h[nid]-h[first_id]
				for rid in self.order[1:,fid]:
					if self.hold[rid] == 1 and last != X[rid,fid]:
						new_gain = 0
						if H_L >= self.min_weight and H_R >=self.min_weight:
							gain_L = G_L*G_L/(H_L+self.lamda)
							gain_R = G_R*G_R/(H_R+self.lamda)
							new_gain = gain_L+gain_R

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
		# print sum_h,sum_g
		# split
		for i,nid in enumerate(self.expand):
			gain = (sum_g[nid]*sum_g[nid])/(sum_h[nid]+self.lamda)
			# print lst[i][0],gain,'score:',lst[i][3]
			if gain < lst[i][0]:
				# print 'split:',lst[i][1],lst[i][2]
				self.tree[nid].set_split(lst[i][1],lst[i][2])
				self.tree[nid].set_left(self.tree.add_child(lst[i][3]))
				self.tree[nid].set_right(self.tree.add_child(lst[i][4]))
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
		for nid in self.expand:
			if self.tree[nid].is_leaf():
				self.tree[nid].set_right(-2)

		# reset expand
		lst = []
		tree = self.tree
		for i in range(tree.size()):
			if tree[i].is_leaf() and (not tree[i].is_old_leaf()):
				lst.append(i)

		self.expand = lst

	def get_tree(self):
		return self.tree
