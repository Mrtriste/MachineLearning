# -*- coding:utf-8 -*-  

import numpy as np
import csv

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

def cal_deriv(X,y,w):
	pass
	

if __name__ == '__main__':
	X,y = load_data('../../datasets/data/LRSet.csv')
	X = np.mat(X)
	n_feature = X.shape[1];n_samples = X.shape[0]
	w = np.zeros((n_feature,1))
	for i in range(50):
		pred = sigmoid(X*w)
		print pred
		R = np.eye(n_samples)
	
