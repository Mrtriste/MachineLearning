
############### begin SGD classification class
'''
	support penality: none,l2
	support learning rate: constant,optimal,PA1,PA2
	support loss function: HingeLoss,LogisticLoss,ModifiedHuberLoss,SquaredHingeLoss
'''
class SGD:
	LOSS_FUNCTION = {
		'HingeLoss':(HingeLoss,),
		'LogisticLoss':(LogisticLoss,),
		'ModifiedHuberLoss':(ModifiedHuberLoss,),
		'SquaredHingeLoss':(SquaredHingeLoss,),
	}

	def __init__(self,iter_num=20,loss_type='HingeLoss',
				 eta0=0.1,alpha=0.0001,learning_rate='constant',penality='l2'):
		self.iter_num = iter_num
		self.loss_type = loss_type
		self.loss_function = self.LOSS_FUNCTION[loss_type][0]()
		self.eta0 = eta0
		self.alpha = alpha
		self.learning_rate = learning_rate
		self.penality = penality

	def _fit_binary(self,X,y):
		n_samples = X.shape[0];n_features = X.shape[1]
		if self.class_set.shape[0] == 2:
			y_ = np.ones(n_samples)
			y_[y==self.class_set[0]] = -1
		else:
			y_ = y
		w = np.random.rand(n_features)
		for it in range(self.iter_num):
			shuffle(self.index)
			if self.learning_rate == 'constant':
				eta = self.eta0
			elif self.learning_rate == 'PA1':
				pass
			elif self.learning_rate == 'PA2':
				pass
			elif self.learning_rate == 'optimal':
				pass
			for i in range(n_samples):
				Xi = X[self.index[i]];yi = y_[self.index[i]]
				p = np.dot(w,Xi)/(pow(np.dot(w,w),0.5))
				deriv = self.loss_function.deriv(yi,p)
				Rw = eta*self.alpha*w
				Lw = eta*deriv*Xi
				w -= (Rw+Lw)
		return w.tolist()

	def _fit_multi(self,X,y):
		n_samples = X.shape[0];n_features = X.shape[1]
		w = []
		for i in range(self.class_set.shape[0]):
			y_ = np.ones(n_samples)
			y_[y!=self.class_set[i]] = -1
			w.append(self._fit_binary(X,y_))
		return w

	def fit(self,X,y):
		self.class_set = np.unique(y)
		self.index = np.arange(X.shape[0])
		if self.class_set.shape[0] == 2:
			self.w = [self._fit_binary(X,y)]
			self.w = preprocessing.normalize(self.w, norm='l2')[0]
		else:
			self.w = self._fit_multi(X,y)
			self.w = preprocessing.normalize(self.w, norm='l2')

	def predict(self,X):
		if self.class_set.shape[0] == 2:
			pred = np.dot(X,self.w)
			y = (pred>0).astype(int)
			return self.class_set[y]
		else:
			scores = np.dot(X,self.w.T)
			y = scores.argmax(axis = 1)
			return self.class_set[y]

############### end SGD class

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
	clf = SGD()
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
	clf = SGD(eta0=0.1,alpha = 0.01)
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
	clf = SGD(eta0=0.1,alpha = 0.01)
	clf.fit(X_train,y_train)
	y_pred = clf.predict(X_test)
	correct_rate = 1-np.mean(y_test!=y_pred)
	print 'correct_rate:',correct_rate


if __name__ == '__main__':
	# test_binary()
	test_multi()
	# test_image()
	plt.show()
