# -*- coding:utf-8 -*-

class Node:
	def __init__(self):
		self.left = -1
		self.right = -1
		self.value = 0
		self.split_f = -1
		self.split_v = -1
		self.loss = 1e12
		self.num = 1

	def set_left(self,l):
		self.left = l 

	def set_right(self,r):
		self.right = r 

	def set_value(self,v):
		self.value = v

	def set_split(self,f,v):
		self.split_f = f
		self.split_v = v

	def set_left(self,l):
		self.left = l

	def set_right(self,r):
		self.right = r

	def get_value(self):
		return self.value

	def get_split_f(self):
		return self.split_f

	def get_split_v(self):
		return self.split_v

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def is_leaf(self):
		return self.left == -1

	def is_old(self):
		return self.right == -2

	def set_loss(self,l):
		self.loss = l 

	def get_loss(self):
		return self.loss


class RegTree:
	def __init__(self):
		self.nodes = []
		self.nodes.append(Node())
		self.node_num = 1

	def __getitem__(self,index):
		return self.nodes[index]

	def add_child(self,v):
		node = Node()
		node.value = v 
		self.nodes.append(node)
		self.node_num += 1
		return self.node_num - 1

	def get_score(self,x):
		node = self.nodes[0]
		while (not node.is_leaf()):
			split_v = node.get_split_v()
			split_f = node.get_split_f()
			if x[split_f] < split_v:
				node = self.nodes[node.get_left()]
			else:
				node = self.nodes[node.get_right()]
		return node.get_value()

	def size(self):
		return self.node_num
