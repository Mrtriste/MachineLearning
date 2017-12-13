# -*- coding=utf-8 -*-

import numpy as np 
from Tree import *
from Updater import *

class Booster:
	def __init__(self,X,order):
		self.X= X
		self.order = order

	def train(self,info):
		n_class = info['n_class']
		g = info['grad']
		h = info['hess']
		lamda = info['lamda']
		min_weight = info['min_weight']
		self.Trees = []
		# every loop geranerates a tree
		for i in range(n_class):
			updater = Updater(self.X,self.order,g[:,i],h[:,i],lamda,min_weight)
			updater.generate()
			self.Trees.append(updater.get_tree())

	def get_trees(self):
		return self.Trees
