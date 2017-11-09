## Stochastic Gradient Descent(SGD) Classification

The core idea of GLM is that, we want to split the space into several parts one hyperspace, which is controlled by one parameter vector $$\vec{w}$$, and our duty is to find that parameter.

Every time, we randomly choose one sample to update the parameter $$\vec{w}$$.
$$
\vec{w} = \vec{w} - \eta*\{\alpha*\frac{\partial R(\vec{w})}{\partial \vec{w}}+\frac{\partial E(\vec{w}\vec{x},y)}{\partial \vec{w}}\}
$$
$$\eta$$ is learning rate, $$\alpha$$ is regularization parameter, $$R(\vec{w})$$ is regularization , and $$E(wx,y)$$ is the loss of one sample.

Here we use $$R(\vec{w})=\frac{1}{2}\lVert w \rVert^2$$ as the regularization, and we use four different loss functions as our $$E(wx,y)$$. They are HingeLoss, LogisticLoss, ModifiedHuberLoss, SquaredHingeLoss.

- Hinge Loss

$$
E(wx,y)=\begin{cases}
0,& wx*y>1\\
1-wx*y,& otherwise
\end{cases}
$$

$$
deriv=\frac{d(E'(wx,y))}{d(wx)}=\begin{cases}
0,& wx*y>1\\
-y,& otherwise
\end{cases}
$$

- Logistic Loss

$$
E(wx,y)=ln(1+\exp(-wx*y))
$$

$$
deriv=\frac{d(E'(wx,y))}{d(wx)}=-\frac{y}{1+\exp(wx)}
$$

- Modified Huber Loss

$$
E(wx,y)=\begin{cases}
0,& wx*y>1\\
(1-wx*y)^2,& -1\le wx*y \le1\\
-4py,& wx*y\ge -1
\end{cases}
$$

$$
deriv=\frac{d(E'(wx,y))}{d(wx)}=\begin{cases}
0,& wx*y>1\\
-2y*(1-wx*y),& -1\le wx*y \le1\\
-4y,& wx*y\ge -1
\end{cases}
$$

- Squared Hinge Loss

$$
E(wx,y)=\begin{cases}
0,& wx*y>1\\
(1-wx*y)^2,& otherwise
\end{cases}
$$

$$
deriv=\frac{d(E'(wx,y))}{d(wx)}=\begin{cases}
0,& wx*y>1\\
-2y*(1-wx*y),& otherwise
\end{cases}
$$

 So, the update formula is as following:
$$
\vec{w} = \vec{w} - \eta*\{\alpha*\vec{w}+deriv*\vec{x}\}
$$
Core Code:

```python
for i in range(n_samples):
    Xi = X[self.index[i]];yi = y_[self.index[i]]
    p = np.dot(w,Xi)/(pow(np.dot(w,w),0.5)) # p = w*x in the above fomula
    deriv = self.loss_function.deriv(yi,p)
    Rw = eta*self.alpha*w
    Lw = eta*deriv*Xi
    w -= (Rw+Lw)
```



 

