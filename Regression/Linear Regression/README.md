## LinearReg

objective function:
$$
loss = \frac{1}{2}(Xw-y)^T(Xw-y)
$$
derivative:
$$
\frac{\partial loss}{\partial w}=X^T(Xw-y)
$$
let it equals 0, we get:
$$
w = (X^TX)^{-1}X^Ty
$$


## Ridge

objective function:
$$
loss = \frac{1}{2}(Xw-y)^T(Xw-y)+ \frac{1}{2}\alpha* w^Tw
$$
derivative:
$$
\frac{\partial loss}{\partial w}=X^T(Xw-y)+\alpha Iw
$$
let it equals 0, we get:
$$
w = (X^TX+\alpha I)^{-1}X^Ty
$$


## Lasso

objective function:
$$
loss = \frac{1}{2n}(Xw-y)^T(Xw-y)+\alpha \parallel w \parallel _1
$$
