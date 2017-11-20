# -*- coding:utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import preprocessing
import random
from SVM import SVM

def get_binary_data():
	centers = [[-5,3],[1,3]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_multi_data():
	centers = [[-5,3],[1,3],[-3,-3]]
	X,y = make_blobs(centers = centers,n_samples = 1000,random_state=42)
	trans = [[0.4,0.2],[-0.4,1.2]]
	X = np.dot(X,trans) + np.random.rand(1000,2)*2.5
	return X,y

def get_image_data():
	digits = datasets.load_digits()
	return digits.data,digits.target




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

def plot_line(X,w):
	x_min = X[:,0].min();x_max = X[:,0].max()
	y_min = X[:,1].min();y_max = X[:,1].max()
	def get_y(x,w):
		# w0+w1*x+w2*y=0  =>  y = (-w0-w1*x)/w2
		return (-w[0]-w[1]*x)/w[2]
	def get_x(y,w):
		# w0+w1*x+w2*y=0  =>  x = (-w0-w2*y)/w1
		return (-w[0]-w[2]*y)/w[1]
	# (x_min,x_min_y),(x_max,x_max_y); (y_min_x,y_min),(y_max_x,y_max)
	x_min_y = get_y(x_min,w);x_max_y = get_y(x_max,w)
	y_min_x = get_x(y_min,w);y_max_x = get_x(y_max,w)
	if np.fabs(x_min_y-x_max_y) < np.fabs(y_min_x-y_max_x):
		plt.plot([x_min,x_max],[x_min_y,x_max_y])
	else:
		plt.plot([y_min_x,y_max_x],[y_min,y_max])

############### test main
def test_binary():
	X,y = get_binary_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = SVM()
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate

	plot_samples(X,y)
	plot_line(X[:,1:],clf.w)

def test_multi():
	X,y = get_multi_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = SVM()
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate

	plot_samples(X,y)
	print clf.w
	for w in clf.w:
		plot_line(X[:,1:],w)

def test_image():
	X,y = get_image_data()
	X = np.column_stack([[1]*X.shape[0],X])
	X_train,X_test,y_train,y_test = \
				train_test_split(X,y,test_size=0.2,random_state = np.random.RandomState(42))
	clf = SVM()
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate


if __name__ == '__main__':
	# test_binary()
	test_multi()
	# test_image()
	plt.show()
