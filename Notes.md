- [为什么说bagging是减少variance，而boosting是减少bias?](https://www.zhihu.com/question/26760839)

  Bagging 是 Bootstrap Aggregating 的简称，意思就是再取样 (Bootstrap) 然后在每个样本上训练出来的模型取平均，所以是降低模型的 variance. Bagging 比如 Random Forest 这种先天并行的算法都有这个效果。

  Boosting 则是迭代算法，每一次迭代都根据上一次迭代的预测结果对样本进行加权，所以随着迭代不断进行，误差会越来越小，所以模型的 bias 会不断降低。

  High variance 是model过于复杂overfit，记住太多细节noise，受outlier影响很大；high bias是underfit，model过于简单，cost function不够好。

  通常来说boosting是在优化loss function，在降低loss，那么很显然，这在很大程度上是减少bias。
  而bagging，之所以进行bagging，是希望模型能够具有更好的鲁棒性，也就是稳定性，希望避免过拟合，显然这就是在减少variance。

  ​

- [为什么xgboost/gbdt在调参时为什么树的深度很少就能达到很高的精度？](https://www.zhihu.com/question/45487317)

  https://www.zhihu.com/question/45487317/answer/99153174

  Boosting主要关注降低偏差，因此Boosting能基于泛化性能相当弱的学习器构建出很强的集成；Bagging主要关注降低方差，因此它在不剪枝的决策树、神经网络等学习器上效用更为明显。

  其实就机器学习算法来说，其泛化误差可以分解为两部分，偏差（bias)和方差(variance)。这个可由下图的式子导出（这里用到了概率论公式D(X)=E(X^2)-[E(X)]^2）。偏差指的是算法的期望预测与真实预测之间的偏差程度，反应了模型本身的拟合能力；方差度量了同等大小的训练集的变动导致学习性能的变化，刻画了数据扰动所导致的影响。这个有点儿绕，不过你一定知道过拟合。

  也就是说，当我们训练一个模型时，偏差和方差都得照顾到，漏掉一个都不行。

  对于Bagging算法来说，由于我们会并行地训练很多不同的分类器的目的就是降低这个方差(variance) ,因为采用了相互独立的基分类器多了以后，h的值自然就会靠近.所以对于每个基分类器来说，目标就是如何降低这个偏差（bias),所以我们会采用深度很深甚至不剪枝的决策树。

  对于Boosting来说，每一步我们都会在上一轮的基础上更加拟合原数据，所以可以保证偏差（bias）,所以对于每个基分类器来说，问题就在于如何选择variance更小的分类器，即更简单的分类器，所以我们选择了深度很浅的决策树。

  ​

- GBDT 的负梯度为什么是残差？

  其实我觉得叫残差不适合，感觉只是一个梯度下降的做法，我们现在要优化损失函数，怎么优化？自然是求梯度，沿负梯度的方向下降即可减小损失函数。

- ​
