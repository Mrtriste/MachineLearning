## [KNN](http://blog.csdn.net/jmydream/article/details/8644004)

KNN almost has no training process.

At the very beginning, we can classify the test samples. 

K used to be lower than sqrt(#sample), determined by CV.



## Disadvantages

1. has no statistical estimates about error; 
2. lazy-learning, requires much memory at running time;
3. computationally expensive

Therefore, KNN can just do some simple classification and handle low-dimension datasets.



## Advantages

1. simple and easy-understanding
2. easy to realize
3. no need to estimate parameters
4. no training process
5. suitable for sparse events
6. suitable for multi-label classification

KNN can be used for recommendation.

