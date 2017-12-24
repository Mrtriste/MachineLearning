## K-Means

**step:**

1. choose k initial centers:

   1. choose one sample at random as the first center
   2. calculate the minimum distances of all the samples with the previous centers, and then choose the sample with the maximum distance as next center
   3. go back to 1. until has chosen k centers 

   ​

2. in each iterator:

   1. for each sample, calculate the distance with all the centers, and assign it to the center closest to it
   2. update the centers with the average value of the samples assigned to it
   3. if satisfying the stopping condition, break



**code:**

```python
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
```

