# -*- coding:utf-8 -*-  

import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn import preprocessing

def load_data(filename,add_one = True):
	file = open(filename)
	csv_file = csv.reader(file)
	temp = next(csv_file)
	n_samples = int(temp[0]); n_features = int(temp[1])
	add = 1
	if not add_one:
		add = 0
	datamat = np.empty((n_samples,n_features+add),dtype = np.float64)
	labelmat = np.empty((n_samples,),dtype = np.int)
	if add_one:
		datamat[:,0] = 1
	for i,line in enumerate(csv_file):
		datamat[i,add:] = line[:-1]
		labelmat[i] = line[-1]
	return datamat,labelmat

def sigmoid(inX):
	return 1.0/(1+np.exp(-inX))

def fit(X,t):
	n_samples = X.shape[0];n_feature = X.shape[1]
	X = np.mat(X);t = t.reshape(n_samples,1)
	w = np.zeros((n_feature,1))
	iter_num = 50
	for i in range(iter_num):
		y = sigmoid(X*w)
		R = np.mat(np.eye(n_samples))
		for j in range(n_samples):
			R[j,j] = y[j]*(1-y[j])
		z = X*w - R.I*(y-t)
		w = (X.T*R*X).I*X.T*R*z
	return w

if __name__ == '__main__':
	X,y = load_data('../../datasets/data/LRSet.csv')
	X[:,1:] = preprocessing.scale(X[:,1:])
	plt.figure(1, figsize=(8,6))
	color = np.array(['b']*X.shape[0])
	color[y==1] = 'r'
	plt.scatter(X[:,1],X[:,2],c=color)

	w = fit(X,y)
	x_min = X[:,1].min()-0.5;x_max = X[:,1].max()+0.5
	print x_min,x_max

	def line(x0):
		# w0+w1*x+w2*y=0  =>  y = (-w0-w1*x)/w2
		return (-w[0,0]-w[1,0]*x0)/w[2,0]
	print line(x_min)
	plt.plot([x_min,x_max],[line(x_min),line(x_max)])

	plt.show()


	
