[博客原文链接](https://mrtriste.github.io/2017/03/12/perceptron-%E6%84%9F%E7%9F%A5%E6%9C%BA/)

## L0、L1、L2范数

L-P范数：

$$
L_p=\sqrt[p]{\sum_1^n{x_i^p}}\quad,x=(x_1,x_2,···,x_n)
$$

L0:表示度量向量中非零元素的个数。

L1:表示向量x中非零元素的绝对值之和。（曼哈顿距离）

L2:表示向量元素的平方和再开平方。（欧式距离）


## 感知机

### 1、感知机模型

对n维的数据中的每一个n维向量x，n维权值向量w和偏置参数b，当w·x+b>=0，输出为1，当w·x+b<0，输出为0

即


$$
sign(w·x+b)=\begin{cases}
1&\text{w·x+b>=0}\
-1&\text{w·x+b<0}
\end{cases}
$$

感知机就是找到一种函数将训练集中的每个(x,y)进行分类，使y=sign(w·x+b)成立。

具体点的解释就是在n维空间中（n为数据集的维数），有这些训练集分布在这个空间中，感知机就是找到一个超平面分割这些点，在这个超平面的“上侧”的标记全为1，“下侧”全为-1。

### 2、感知机策略

感知机的目标：求得一个能够将训练集正实例点和负实例点完全正确分开的分离超平面。也就是确定权值向量w和偏置b。

损失函数：误分类点到当前超平面的总距离。

对每个误分类点(xi,yi)到超平面的距离为


$$
-\frac{1}{\left\|w\right\|}y_i(w·x_i+b)\quad,\left\|w\right\|是w的L_2范数.
$$

M为误分类点，总距离为

$$
-\frac{1}{\left\|w\right\|}\sum_{x_i\in{M}}{y_i(w·x_i+b)}
$$

不考虑$$\frac{1}{\left\|w\right\|}$$，损失函数为

$$
L(w,b)=-\sum_{x_i\in{M}}{y_i(w·x+b)}
$$

现在的目标就是根据损失函数学习w和b。



### 3、感知机算法

感知机学习算法是误分类驱动的。

首先L(w,b)的梯度为


$$
\begin{align}
&\nabla{_w}{L(w,b)}=-\sum_{x_i\in M}{y_ix_i}\\
&\nabla{_b}{L(w,b)}=-\sum_{x_i\in M}{y_i}
\end{align}
$$

随机选取一个误分类点$$(x_i,y_i)$$，对w,b进行更新，


$$
\begin{align}
&w\leftarrow w+\eta y_ix_i\\
&b\leftarrow  b+\eta y_i
\end{align}
$$

式中$$\eta(0<\eta<=1)$$为步长，也就是学习率。

为什么可以这样对w,b迭代就可以减小损失函数呢？可以这么理解，梯度就是沿着超空间中的一点值变化最快的方向，在二维平面中，就是直线的斜率。

由于要最小化风险函数，所以按梯度负方向来更新w,b。

#### 算法：

(1).选取初始值$$w_0,b_0$$

(2).在训练集中选取数据$$(x_i,y_i)$$

(3).如果$$y_i(w·x_i+b)<=0$$


$$
\begin{align}
&w\leftarrow w+\eta y_ix_i\\
&b\leftarrow  b+\eta y_i
\end{align}
$$

(4).转至(2)，直至没有误分类点。



可以证明，该算法经过有限次迭代可以实现将所有训练集正确分类。



#### 算法的对偶形式

在原算法中，要使用$$w\leftarrow w+\eta y_ix_i$$来对w进行更新，那么每一次更新都需要计算$$w\leftarrow w+\eta y_ix_i$$，那么对偶形式的思想就是，现在我用一个n维向量来记录对$$w\leftarrow w+\eta y_ix_i$$加多少次，为什么这样是等价的？因为损失函数的梯度只与随机选的误分类点有关，所以每次迭代可以认为是独立的。

具体实现就是，用一个n维向量$$\alpha$$来记录最后对每一个$$x_iy_i$$要乘以多少个$$\eta$$的和，也就是$$\alpha _i=k\eta \quad (k为加的次数)$$。





## 以下为参考资料

1. 《统计学习方法》     ——李航
2. [随机梯度下降（Stochastic gradient descent）和 批量梯度下降（Batch gradient descent ）的公式对比、实现对比](http://blog.csdn.net/lilyth_lilyth/article/details/8973972)
3. [为什么随机梯度下降方法能够收敛？ - 李文哲的回答 - 知乎](https://www.zhihu.com/question/27012077/answer/122359602)

