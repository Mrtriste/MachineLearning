- ### Perceptron_bin_class :

  binary-class classification

  update w with w += alpha\*X[i]\*y[i], where (X[i],y[i]) is a mis-classified instance!!!

- ### Perceptron_multi_class :

  multi-class classification

  use the one-vs-rest method, have current class labeled 1, the rest labeled -1, then use binary classification

  update w with w += alpha\*X[i]\*y[i], where (X[i],y[i]) is a mis-classified instance!!!

The loss function here is one part of SGD's loss functions

**What's important is that we update w with mis-classified instance!!**

Core Code:

```py
for it in range(self.iter_num):
	X,y = shuffle(X,y)
	for i in range(n_samples):
		z = np.dot(X[i],self.w)*y[i]
		if z < 0: # mis-classify driven!!!
			self.w += self.alpha*X[i]*y[i] 
```

