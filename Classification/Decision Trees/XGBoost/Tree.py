# -*- coding=utf-8 -*-

class Node:
	def __init__(self):
		self.left = -1
		self.right = -1
		self.gain = 0
		self.split_fid = -1
		self.split_v = 0
		self.weight = 0

	def set_left(self,left):
		self.left = left

	def set_right(self,right):
		self.right = right

	def set_split(self,fid,v):
		self.split_fid = fid
		self.split_v = v

	def set_weight(self,weight):
		self.weight = weight

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def get_split_fid(self):
		return self.split_fid

	def get_split_v(self):
		return self.split_v

	def get_score(self):
		return self.weight

	def is_leaf(self):
		return self.left == -1


class Tree:
	def __init__(self):
		self.node_num = 1
		self.nodes = []
		self.nodes.append(Node())

	def __getitem__(self,index):
		return self.nodes[index]

	def get_score(self,data):
		node = self.nodes[0]
		while(not node.is_leaf()):
			fid = node.get_split_fid()
			v = node.get_split_v()
			if data[fid]<v:
				node = self.nodes[node.get_left()]
			else:
				node = self.nodes[node.get_right()]
		return node.get_score()

	def add_child(self,weight):
		node = Node()
		node.set_weight(weight)
		self.nodes.append(node)
		self.node_num += 1
		return self.node_num-1

	def size(self):
		return len(self.nodes)


