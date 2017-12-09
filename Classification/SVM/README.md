## SVM

Here I just realize a simple SVM which only supports binary classification, named C-SVC.

- Formulation

  1. Linear
     $$
     max\ \gamma \quad s.t. \quad \frac {y_i(wx_i+b)}{|w|} \ge\gamma
     $$
     Due to $$ \gamma = \frac{\bar{\gamma}}{|w|}$$ , and we can scale $$|w|$$ to scale $$\bar{\gamma}$$ , so we define $$\bar{\gamma}$$ as 1.

     Then, the above formulation is as following:
     $$
     max\ \frac{1}{|w|} \quad s.t. \quad {y_i(wx_i+b)}\ge1
     $$
     That equals:
     $$
     min\ \frac{1}{2}{|w|}^2 \quad s.t. \quad {y_i(wx_i+b)}\ge1
     $$

  2. Non-Linear

     Many times, the data can not be classified linearly, so we will join a parameter $$\xi_i$$ for each sample.

     At the same time, we will add a penalty term about $$\xi_i$$ , and use a parameter C to control balance between it with $$|w|$$. 

     The formulation is as following:
     $$
     min\  \frac{1}{2}{|w|}^2+C\sum_i{\xi_i}\quad s.t.\quad y_i(wx_i+b)+\xi_i\ge1,\\\xi_i\ge0
     $$

  3. Kernel

     Replace $$x_ix_j$$ with $$K(x_i,x_j)$$.

     ​

- Lagrange dual problem

  1. origin problem 

     We want to solve a optimization problem {min P , with constraint C<=0}.

     Then we can define a Lagrange Function L = P + a*C.(a>=0)

  2. min max problem

     {min max L} <=> {min P with C<=0} , that is they have the same solution.

  3. max min problem -- dual problem

     {max min L}

     we need to connect it with the min max problem to conclude the connection between the origin problem and dual problem.

  The solution of origin problem and max min problem(dual problem) at the same time should satisfy the KKT condition.

  So back to the SVM problem, the Lagrange Function is that,
  $$
  \frac{1}{2}{|w|}^2+C\sum_i{\xi_i}-\sum_i{\alpha_i}\{y_i(wx_i+b)+\xi_i-1\}-\mu_i\xi_i
  $$
  Now the time of getting dual problem:

  First, we min this Lagrange Function, make a derivation about parameters $$w,b,\xi_i$$, and set them=0.

  Second, substitute the results of equations into the Lagrange Function to eliminate $$w,C,\mu_i,\xi_i,b$$, only reserve $$\alpha_i$$, and then max it.

  We will get the dual problem:
  $$
  \max_\alpha{\ -\frac{1}{2}\sum_i \sum_j\alpha_i \alpha_jy_i y_j(x_i.x_j)\ +\sum_i{\alpha_i}}\\
  s.t. \sum_i {\alpha_iy_i=0,\quad0\le\alpha_i \le\mu_i}
  $$
  That is,
  $$
  min\ \frac{1}{2}\alpha^TQ\alpha-e^T\alpha \\
  s.t. \quad y^T\alpha= 0,\\
  0\le\alpha_t\le C
  $$
  and $$Q_{ij}=y_iy_jK(x_i,x_j), e=[1,1,...1,1]^T$$.

  ​

- Solver.py

  We will solve such a problem
  $$
  min\ \frac{1}{2}\alpha^TQ\alpha+p^T\alpha \\
  s.t. \quad y^T\alpha= \Delta,\\
  0\le\alpha_t\le C
  $$
  Then, the following step is described in the Paper [libsvm].
