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

  ​

- XGBoost二分类每轮迭代可不可以只训练一棵树？

  以前没想明白，因为在一轮迭代中，每棵树的叶子节点是score，那将score加起来后softmax得到的是概率，假如只有一棵树，分母除以谁呢？后来类比LR有点明白了，二分类我直接拟合的是a ( = z1 - z2)，而不是分开的z1和z2，这里z1=wx+b，概率即
  $$
  P(c_i=1)=\frac{e^{z_1}}{e^{z_1}+e^{z_2}}=\frac{1}{1+e^{-(z_1-z_2)}}=\frac{1}{1+e^{-a}}
  $$
  注意a是和类别为1 的概率成正比的，a越大，概率越大（回忆那张S形的sigmoid图）。当然a也可以等于z2-z1，求导多个负号就可以。

  为什么要这样？当我们遇到类别为1 的样本时，损失函数对$$a$$ 偏导为p-1，值是小于0的，要梯度下降，那么$$a$$ 是要a=a - (p-1)，即a增大，也即z1相对于z2更大，那么p1也会增大，损失函数就会减少。

  对于xgboost的二分类，我也直接拟合a，即a = z2-z1，而不是分开的z1和z2（这里的z1,z2是叶子节点上的值，没有具体的意义，只是相对大小表示概率的相对大小），其他的与LR类似。

  理解的难点是直接拟合a，只有一个变量，$$\frac{1}{1+e^{a}}和1-\frac{1}{1+e^{a}}$$ 分别就是两个类别的概率。其他类似于LR，注意我们这里的a没有负号，如果遇到c=1的样本，对a的偏导为1-p>0，梯度下降后，a的趋势是变小（a=a-(1-p)），z2-z1变小，也即z1相对z2增大，p1增加。 

  从两个变量到一个变量是最重要的。

  ​

- Lasso与Ridge比为什么可以选择重要特征？

  [维基百科](https://en.wikipedia.org/wiki/Lasso_(statistics)#Interpretations_of_lasso) 

  1. 几何解释：拉格朗日法，限制w的区域，lasso是正方形，有角，ridge是圆，没角，能更多的与损失函数的等高线相切
  2. 贝叶斯解释：lasso的参数先验是拉普拉斯分布，The Laplace distribution is sharply peaked at zero，ridge的是正态分布
  3. Convex relaxation interpretation：还不懂




- [正负样本不平衡](http://blog.csdn.net/losteng/article/details/50947161)

  1. 采样：上采样（小种类复制多份），下采样（剔除多的）
  2. 数据合成
  3. 加权：不同类别分错的代价不同
  4. 一分类（One-Class Learning）或异常检测（Novelty Detection）

  Paper: Learning from Imbalanced Data




- [过拟合](http://blog.csdn.net/heyongluoyao8/article/details/49429629)
  1. early stopping：当accuracy不再提高时，就停止训练
  2. 数据集扩增（Data augmentation）：有时候往往拥有更多的数据胜过一个好的模型
  3. 正则化（Regularization）：L1，L2
  4. 特征选择
  5. Dropout：神经网络中随机地删除一些（可以设定为一半，也可以为1/3，1/4等）隐藏层神经元
  6. 重新清洗数据：导致过拟合的一个原因也有可能是数据不纯导致的




- [欠拟合]()
  1. 添加其他特征项
  2. 添加多项式特征
  3. 减少正则化参数




- 正则项

  引用自http://blog.csdn.net/heyongluoyao8/article/details/49429629

  正则项是为了降低模型的复杂度，从而避免模型区过分拟合训练数据，包括噪声与异常点（outliers）。

  从另一个角度上来讲，正则化即是假设模型参数服从先验概率，即为模型参数添加先验，只是不同的正则化方式的先验分布是不一样的。这样就规定了参数的分布，使得模型的复杂度降低（试想一下，限定条件多了，是不是模型的复杂度降低了呢），这样模型对于噪声与异常点的抗干扰性的能力增强，从而提高模型的泛化能力。

  还有个解释便是，从贝叶斯学派来看：加了先验，在数据少的时候，先验知识可以防止过拟合；从频率学派来看：正则项限定了参数的取值，从而提高了模型的稳定性，而稳定性强的模型不会过拟合，即控制模型空间。 

  另外一个角度，过拟合从直观上理解便是，在对训练数据进行拟合时，需要照顾到每个点，从而使得拟合函数波动性非常大，即方差大。在某些小区间里，函数值的变化性很剧烈，意味着函数在某些小区间里的导数值的绝对值非常大，由于自变量的值在给定的训练数据集中的一定的，因此只有系数足够大，才能保证导数的绝对值足够大。

  另外一个解释，规则化项的引入，在训练（最小化cost）的过程中，当某一维的特征所对应的权重过大时，而此时模型的预测和真实数据之间距离很小，通过规则化项就可以使整体的cost取较大的值，从而，在训练的过程中避免了去选择那些某一维（或几维）特征的权重过大的情况，即过分依赖某一维（或几维）的特征（引用知乎）。 
  L2与L1的区别在于，L1正则是拉普拉斯先验，而L2正则则是高斯先验。它们都是服从均值为0，协方差为$$\frac{1}{\lambda}$$。当$$\lambda=0$$时，即没有先验）没有正则项，则相当于先验分布具有无穷大的协方差，那么这个先验约束则会非常弱，模型为了拟合所有的训练集数据， 参数w可以变得任意大从而使得模型不稳定，即方差大而偏差小。λ越大，标明先验分布协方差越小，偏差越大，模型越稳定。即，加入正则项是在偏差bias与方差variance之间做平衡tradeoff（来自知乎）。




- 偏差和方差

  图：https://www.zhihu.com/question/20448464/answer/20039077

  机器学习解释：https://www.zhihu.com/question/20448464/answer/146318047

  真实例子：http://scott.fortmann-roe.com/docs/BiasVariance.html

  模型复杂度低：高偏差，低方差

  模型复杂度高：低偏差，高方差

  现在才能理解这个公式：
  $$
  Error(x)=E[\ (y-f(x))^2\ ]
  $$
  bias-variance decomposition：
  $$
  \begin{align}
  Error(x)&=E[\{(y-E[f(x)])+(E[f(x)]-f(x))\}^2] \\
  &=E[\{y-E[f(x)]\}^2]+E[\{f(x)-E[f(x)]\}^2]+2E[\{y-E[f(x)]\}*\{E[f(x)]-F(x)\}] \\
  &= E[\{y-E[f(x)]\}^2]+E[\{f(x)-E[f(x)]\}^2]\\
  &= E[\{(y-t)+(t-E[f(x)])\}^2]+E[\{f(x)-E[f(x)]\}^2]\\
  &=E[\{y-t\}^2]+E[\{t-E[f(x)]\}^2]+2E[\{y-t\}*\{t-E[f(x)]\}]+E[\{f(x)-E[f(x)]\}^2]\\
  &=E[\{y-t\}^2]+E[\{t-E[f(x)]\}^2]+E[\{f(x)-E[f(x)]\}^2] \quad 假设噪声期望为0\\ 
  &=noice^2+bias^2+variance^2
  \end{align}
  $$
  可以看到误差函数可以分解成三项，关于noice，bias，variance，noice不可控，于是我们需要在偏差和方差间达到一个平衡，就是Ng教授经常说的。

  y是测量的数据，t是真实数据，我们测量的可能有误差，f(x)是我们的预测值，E[f(x)]是预测值的期望，假设噪声的期望为0，即E[y-t]=0




- [k-means缺点及改进](http://blog.csdn.net/u010536377/article/details/50884416)

  http://blog.csdn.net/u011204487/article/details/59624571

  缺点：

  1. 对于离群点和孤立点敏感；
  2. k值选择; 
  3. 初始聚类中心的选择； 
  4. 只能发现球状簇。 
  5. 在簇的平均值可被定义的情况下才能使用，可能不适用于某些应用；
  6. 需要不断地进行样本分类调整，不断地计算调整后的新的聚类中心，因此当数据量非常大时，算法的时间开销是非常大的；

  改进：详见博客

  ​

- [梯度下降和高斯牛顿法](https://www.zhihu.com/question/25000420)

  都是最优化方法

  梯度下降：

  1. 优点：始终逼近最优值
  2. 缺点：在远离极小值的地方下降很快，而在靠近极小值的地方下降很慢。

  高斯牛顿：

  1. 优点：牛顿法要比梯度下降法更具有全局判断能力，而梯度下降局部进行下降，往往是走之字型的。
  2. 缺点：若初始点距离极小值点过远，迭代步长过大会导致迭代下一代的函数值不一定小于上一代的函数值。

  ​

- [推荐系统冷启动](https://www.zhihu.com/question/19843390)

  1. 普遍、通用、基础的推荐，即热门排行榜，经过交互后迭代出新的推荐
  2. 让用户填写一些标签
  3. 从其他一些平台搜集用户资料

  ​

- [结构风险最小化和经验风险最小化](http://blog.csdn.net/philosophyatmath/article/details/51015222)

  置信风险与两个量有关，一是样本数量，显然给定的样本数量越大，我们的学习结果越有可能正确，此时置信风险越小；二是分类函数的VC维，显然VC维越大，推广能力越差，置信风险会变大。

  ​

  CS229 ERM笔记：http://blog.csdn.net/pi9nc/article/details/18766285，https://www.cnblogs.com/wallacup/p/6071515.html

  ​

  期望风险、经验风险与结构风险之间的关系：http://blog.csdn.net/liyajuan521/article/details/44565269

  1. 经验风险：对训练集中的所有样本点损失函数的平均

  2. 期望风险：怎么来衡量这个模型对所有的样本（包含未知的样本和已知的训练样本）预测能力呢？熟悉概率论的很容易就想到了用期望。

     通过上面的分析可以知道，经验风险与期望风险之间的联系与区别。现在在总结一下：

     经验风险是局部的，基于训练集所有样本点损失函数最小化的。

     期望风险是全局的，是基于所有样本点的损失函数最小化的。

     经验风险函数是现实的，可求的；

     期望风险函数是理想化的，不可求的；

  3. 结构风险：只考虑经验风险的话，会出现过拟合的现象，过拟合的极端情况便是模型f(x)对训练集中所有的样本点都有最好的预测能力，但是对于非训练集中的样本数据，模型的预测能力非常不好。怎么办呢？这个时候就引出了结构风险。结构风险是对经验风险和期望风险的折中。在经验风险函数后面加一个正则化项（惩罚项）便是结构风险了




- 模型选择

  交叉验证：

  1. hold-out cv: 70% train, 30% test --> choose parameter --> 100% train
  2. k-fold cv: k=10, 5; computation-expensive
  3. leave-one-out: data is very few




- 频率学派和贝叶斯学派

  频率学派：认为数据背后有一个真实的$$\theta$$ 来生成数据，这里的$$\theta$$ 不是一个随机变量，它有真实的值，只是我们不知道。对于线性回归我们用极大似然likehood来估计这个值。

  贝叶斯学派：我们不知道$$\theta$$ 的值，所以我们为$$\theta$$ 的值赋予一个先验概率，用先验概率表示$$\theta$$ 的不确定性，有了训练集后可以计算后验概率，与先验概率*likehood成正比，然后最大似然这个后验概率。

  ​


- [Nested CV](https://www.zhihu.com/question/55200250/answer/143797646)

  先弄明白一个概念：[验证集和测试集的区别](https://www.cnblogs.com/xfzhang/archive/2013/05/24/3096412.html)

  *好像比赛的测试集是官方评判结果的数据，即test.csv文件，我们在训练算法的时候不用分出测试集，用验证集就可以了。就是平时所用的CV即可。下面介绍的是包括比赛评判结果的一个完整的流程。* 

  简单来说验证集是在交叉验证（CV）中的，测试集是在最后评估准确率的；验证集是在model selection中 (其实是决定hyperparameter的过程)的概念，是比较一个模型的不同参数，测试集是进行不同模型间的比较。

  Andrew Ng建议将数据进行如下分割: (60% 20%) 20%

  下面进入正题：

  1. 首先将数据集分成70%的训练集（包括训练集和验证集）和30%的测试集

  2. 对每个模型进行以下操作：

     a. 每次设置一个超参数，用训练集进行k-fold交叉验证计算出平均的准确率acc_mean1

     b. 根据acc_mean1得到最好的参数

     （a, b是在做model selection (其实是决定hyper parameter的过程)）

     c. 用最好的参数训练该模型，预测一开始30%的测试集，得到准确率acc_mean2

  3. 根据acc_mean2挑选出最好的模型（参数也已经选好了）

  PS： 外层再来一个循环，即多次分数据集-->训练集和测试集的过程

  - method-1: Random/Shuffle

    更全面可靠的还有10 runs of 10-fold cross validation，就是把最开始的数据集分成70%和30%的过程随机做10次。每次随机分出来的（70%，30%）都做一次10-fold cross validation，得到10个在测试集上的测试结果。分别算出测试结果的平均值和方差，然后再来比较哪个比较好。

  - method-2: K-fold 

    针对nested cv的概念，与10 runs of 10-fold cross validation平级的还有一种方法—— k-fold，比如分成75%的训练集和25%的测试集，就可以4-fold，那么外层也k-fold了，这就是nested cv的叫法的原因。

    至于random和k-fold哪个效果更好, 我觉得没有太大区别。只是k-fold相比于random split保证了所有的数据都有被循环利用过做training和testing。

    ​


- [parameters & hyper parameters](https://www.youtube.com/watch?v=EJtTNboTsm8)

  https://www.quora.com/What-are-hyperparameters-in-machine-learning

  拿神经网络举个例子：

  parameters: $$w，b$$

  hyper parameters: 

  1. learning rate $$\alpha$$
  2. iterations 
  3. hidden layers
  4. hidden units
  5. choice of activation function

  超参数决定了参数最后会怎么样，所以有个超字

  However, there is another kind of parameters that cannot be directly learned from the regular training process. These parameters express “higher-level” properties of the model such as its complexity or how fast it should learn. They are called **hyperparameters**. Hyperparameters are usually fixed before the actual training process begins.

  ​

- [Some advantages of decision trees](http://scikit-learn.org/stable/modules/tree.html#classification)

  sklearn 上有一些模型的优缺点

  ​

- [ROC_AUC scores](http://www.dataschool.io/roc-curves-and-auc-explained/)

  ​

- [连续值的离散化为什么会提升模型的非线性能力](https://www.cnblogs.com/lianyingteng/p/7792693.html)

  以LR为例

  连续型变量：
  $$
  h(\theta)=\frac{1}{e^{-w_1x_1}}
  $$
  分解成离散型变量：
  $$
  h(\theta)=\frac{1}{e^{-(w_1x_1+w_2x_2+w_3x_3)}}
  $$
  使用连续值的LR模型用一个权值去管理该特征，而one-hot后有三个权值管理了这个特征，这样使得参数管理的更加精细，所以这样拓展了LR模型的非线性能力。

  这样做除了增强了模型的**非线性能力**外，还有什么好处呢？这样做了我们至少不用再去对变量进行归一化，也可以**加速**参数的更新速度；再者使得一个很大权值管理一个特征，拆分成了许多小的权值管理这个特征多个表示，这样做降低了特征值扰动对模型为**稳定性**影响，也降低了异常数据对模型的影响，进而使得模型具有更好的**鲁棒性**。





























