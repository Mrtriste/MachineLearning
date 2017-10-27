# -*- coding:utf-8 -*-  

import numpy as np
import csv

def load_data(filename):
	file = open(filename)
	csv_file = csv.reader(file)
	temp = next(csv_file)
	n_samples = int(temp[0]); n_features = int(temp[1])
	datamat = np.empty((n_samples,n_features),dtype = np.float64)
	labelmat = np.empty((n_samples,),dtype = np.int)
	for i,line in enumerate(csv_file):
		datamat[i,:] = line[:-1]
		labelmat[i] = line[-1]
	return datamat,labelmat
	

if __name__ == '__main__':
	datamat,labelmat = load_data('../../datasets/data/iris.csv')


