## XGBoost

### Words:

- out of core: 外存

- shrinkage: the t-th tree's weight is less than the (t-1)-th tree's.

- block: used for Parallel Learning

- advantages:

  - second-order Taylor approximation.

  - use tree's complexity to optimize objective function instead of Gini and ...

  - split finding: give scores for split of each leaf. find which value of which feather as the standard to         split.

  - Shrinkage

  - blocks, presorting for Parallel Learning.

    - 因为每一次迭代中，都要生成一个决策树，而这个决策树是残差的决策树，所以传统的不能并行

      但是陈天奇注意到，每次建立决策树，在分裂节点的时候，比如选中A特征，就要对A进行排序，再计算残差，这个花很多时间

      于是陈天奇想到，每一次残差计算好之后，全部维度预先排序，并且此排序是可以并行的，并行排序好后，对每一个维度，计算一次最佳分裂点，求出对应的残差增益

      于是只要不断选择最好的残差作为分裂点就可以。

      也就是说，虽然森林的建立是串行的没有变，但是每一颗树枝的建立就变成是并行的了，带来的好处：

      1.分裂点的计算可并行了，不需要等到一个特征的算完再下一个了

      2.每层可以并行：

      当分裂点的计算可以并行，对每一层，比如分裂了左儿子和右儿子，那么这两个儿子上分裂哪个特征及其增益也计算好了

  - sparse, missing values.

  - column-resample to prevent over-fitting

- objective [default=reg:linear]

  Regression:

  - “reg:linear” –linear regression
  - “reg:logistic” –logistic regression
  - “binary:logistic” –logistic regression for binary classification, output probability
  - “binary:logitraw” –logistic regression for binary classification, output score before logistic transformation
  - “count:poisson” –poisson regression for count data, output mean of poisson distribution
    - max_delta_step is set to 0.7 by default in poisson regression (used to safeguard optimization)
  - “reg:gamma” –gamma regression with log-link. Output is a mean of gamma distribution. It might be useful, e.g., for modeling insurance claims severity, or for any outcome that might be [gamma-distributed](https://en.wikipedia.org/wiki/Gamma_distribution#Applications)
  - “reg:tweedie” –Tweedie regression with log-link. It might be useful, e.g., for modeling total loss in insurance, or for any outcome that might be [Tweedie-distributed](https://en.wikipedia.org/wiki/Tweedie_distribution#Applications).

  Classification:

  - “multi:softmax” –set XGBoost to do multiclass classification using the softmax objective, you also need to set num_class(number of classes)
  - “multi:softprob” –same as softmax, but output a vector of ndata * nclass, which can be further reshaped to ndata, nclass matrix. The result contains predicted probability of each data point belonging to each class.

  Rank:

  - “rank:pairwise” –set XGBoost to do ranking task by minimizing the pairwise loss



### Loss Function

- Classification

  Here, XGBoost uses Softmax to calculate loss function as follows.

  We have n data samples, with each sample having m feathers, $$()$$

- Regression 



### Codes

- objective.h

  1. GetGradient()

     ​

  2. PredTransform()

- ​

### Reference

[Complete Guide to Parameter Tuning in XGBoost (with codes in Python)](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/)

[算法原理](https://www.2cto.com/kf/201610/559151.html)

[源码笔记1](http://blog.csdn.net/flydreamforever/article/details/75805924)

[源码笔记2](http://blog.csdn.net/flydreamforever/article/details/76219727)

[源码分析1:代码逻辑结构](https://cloud.tencent.com/community/article/497832)

[源码分析2:树构造之 Exact Greedy Algorithm](https://cloud.tencent.com/community/article/590891)

[XGBoost文档](https://xgboost.readthedocs.io/en/latest/)

[XGBoost参数](https://xgboost.readthedocs.io/en/latest/parameter.html)

[XGBoost安装](https://xgboost.readthedocs.io/en/latest/build.html)

[CART，回归树，GBDT，XGBoost，LightGBM](http://blog.csdn.net/a790209714/article/details/78086867)

[ID3->XGBoost](http://www.jianshu.com/p/41dac1f6b0d2)

