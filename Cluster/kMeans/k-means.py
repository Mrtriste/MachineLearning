# -*- coding -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import random

MAX = 1e12

def get_multi_data():
	centers = [[-4,2],[1,3],[-3,-3]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	# trans = [[0.4,0.2],[-0.4,1.2]]
	# X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def plot_samples(X,y):
	x_start = 0
	if np.mean(X[:,0])==1:
		x_start += 1
	c_lst = ['r','g','b','y']
	y_set = np.unique(y)
	color = np.array([c_lst[0]]*y.shape[0])
	for i in range(1,y_set.shape[0]):
		color[y==y_set[i]] = c_lst[i]
	plt.figure(figsize=(8,6))
	plt.scatter(X[:,x_start],X[:,x_start+1],c = color)

class kMeans:
	def __init__(self,k,max_iter=10,tol=0.1):
		self.k = k
		self.max_iter = max_iter
		self.tol = tol

	def fit(self,X):
		centers = self._init_centers(X)
		centers_ = np.zeros_like(centers)
		min_index = np.zeros(X.shape[0],dtype=int)
		num = np.zeros(self.k)
		for it in range(self.max_iter):
			print it,centers
			# assign each sample to some class
			for i in range(X.shape[0]):
				min_dis = MAX
				for k in range(self.k):
					dis = self.distance(centers[k],X[i,:])
					if min_dis > dis:
						min_dis = dis; min_index[i] = k 

			# re-cal centers
			centers_.fill(0)
			num.fill(0)
			for i in range(X.shape[0]):
				# print centers[min_index[i]],X[i,:]
				centers_[min_index[i]] += X[i,:]
				num[min_index[i]] += 1.0
			for i in range(self.k):
				centers_[i] /= num[i]

			if np.min(np.sum((centers_- centers)**2,axis=1)) < self.tol:
				break
			centers[:,:] = centers_[:,:]

		return min_index

	def _init_centers(self,X):
		centers = np.empty([self.k,X.shape[1]],dtype=float)
		centers[0,:] = X[random.randint(0,X.shape[0]-1),:]
		min_dis = np.empty(X.shape[0])
		min_dis.fill(MAX)

		for cur in range(1,self.k):
			# cal last min_dis
			temp = centers[cur-1,:]
			max_index = -1; max_dis = 0
			for i in range(X.shape[0]):
				dis = self.distance(temp,X[i,:])
				min_dis[i] = min(min_dis[i],dis)
				# choose min_index
				if(min_dis[i]>max_dis):
					max_dis = min_dis[i]; max_index = i
			centers[cur] = X[max_index,:]

		return centers

	def distance(self,x1,x2):
		return np.dot(x1-x2,x1-x2)


if __name__ == '__main__':
	X,y = get_multi_data()
	plot_samples(X,y)
	cluster = kMeans(3,10,0)
	pred = cluster.fit(X)
	plot_samples(X,pred)
	plt.show()
