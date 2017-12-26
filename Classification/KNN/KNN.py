# -*- coding -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import random
import math

def get_multi_data():
	n = 2000
	centers = [[-5,3],[1,3],[-3,-3]]
	X,y = make_blobs(centers = centers,n_samples = n,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(n,2)*2.5
	return X,y

class KNN:
	def __init__(self,max_iter=10):
		self.max_iter = max_iter+0.0

	def fit(self,X,y,test_size=0.2):
		self.k = None
		self.vote_res = np.empty(np.unique(y).shape[0])
		upper = int(math.sqrt(X.shape[0]))
		step = upper/self.max_iter
		if abs(step-int(step)) > 0.01:
			step = int(upper/self.max_iter)+1
		else:
			step = int(step)
		max_corr = 0.0; max_k = 0;
		for k in range(1,upper,step):
			print '------------- k =',k,' ------------'
			corr = self._fit_one(X,y,k,test_size)
			if max_corr < corr:
				max_corr = corr; max_k = k 
		print 'best k is ',max_k
		self.k = max_k

	def _fit_one(self,X,y,k,test_size):
		self.kk = k
		p = 0.0
		for i in range(0,int(1.0/test_size)):
			X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=test_size,random_state = np.random.RandomState(42))
			pred = self.predict(X_test,X_train,y_train)
			p += (1-np.mean(y_test!=pred))
		print p/int(1.0/test_size)
		return p/int(1.0/test_size)

	# predict X's class with training data
	def predict(self,X,X_,y_):
		k = self.k if self.k != None else self.kk
		# when training: choose [1,k+1], because dis[0]=0
		offset = 1 if self.k !=None else 0 
		dis = np.empty(X_.shape[0])
		pred = np.empty(X.shape[0])
		for i in range(X.shape[0]):
			x = X[i,:]
			for j in range(X_.shape[0]):
				dis[j] = self.cal_dis(x,X_[j,:])
			index = np.argsort(dis)[offset:k+offset]
			pred[i] = self.vote(y_[index])
		return pred


	def vote(self,res):
		self.vote_res.fill(0)
		for i in res:
			self.vote_res[i] += 1
		max_cnt = 0; max_index = -1
		for i in range(self.vote_res.shape[0]):
			if max_cnt < self.vote_res[i]:
				max_cnt = self.vote_res[i]
				max_index = i 
		return max_index


	def cal_dis(self,x1,x2):
		x = x1-x2
		return np.dot(x,x)

############### plot
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


if __name__ == '__main__':
	X,y = get_multi_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = KNN(10)
	clf.fit(X_train,y_train,0.25)
	y_pred = clf.predict(X_train,X_train,y_train)
	correct_rate = 1-np.mean(y_train!=y_pred)
	print 'train correct_rate:',correct_rate

	y_pred1 = clf.predict(X_test,X_train,y_train)
	correct_rate = 1-np.mean(y_test!=y_pred1)
	print 'test correct_rate:',correct_rate

	plot_samples(X_train,y_train)
	plot_samples(X_train,y_pred)
	plot_samples(X_test,y_test)
	plot_samples(X_test,y_pred1)
	plt.show()
