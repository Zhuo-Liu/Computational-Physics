<center> 
<font size=6> 计算物理第二次作业</font> <br>
<font size=3> 刘茁 </font> <br>
<font size=3> 1500011438 </font>
</center>

# 1. Householder 与Givens 在QR 分解中的比较
## (a)
### 使用Householder
- Householder矩阵为
$$
P _ { ( k ) } = \left[ \begin{array} { c c } { \mathbb { 1 } _ { k } } & { 0 } \\ { 0 } & { R _ { n - k } } \end{array} \right] , R _ { n - k } = 1 _ { n - k } - 2 \frac { w ^ { ( k ) } \left( w ^ { ( k ) } \right) ^ { T } } { \left\| w ^ { ( k ) } \right\| _ { 2 } ^ { 2 } }
$$
其中，$w ^ { ( k ) }$由下式决定
$$
w ^ { ( k ) } = x ^ { ( n - k ) } \pm \left\| x ^ { ( n - k ) } \right\| _ { 2 } e _ { 1 } ^ { ( n - k ) }
$$
- 计算向量$w^{(k)}$，要求$x^{(n-k)}$的欧式模，计算量为$(n-k)$次。
  
  计算$P_{(k)}$要进行一次矢量点乘运算和和一次除法，因此$P_{(k)}$变换的计算量为$2\times(n-k)+1$次

  每次迭代时，前$k-1$列无需计算，因此每次利用Householder变换进行迭代需要进行$(n-k+1)\times(2\times(n-k)+1)$次运算；保留到领头阶，总共的运算次数为
$$\sum_{k=0}^{n-2}(n-k+1)\times(2\times(n-k)+1)\approx \frac 2 3 n^3$$
- Q 的计算为
  $$Q^T=P_{(n-2)}P_{(n-1)}\cdots P_{(0)}$$
 构建P总共需要约$n^2$次计算， 之后每一次计算都要对全部n列进行，总的计算次数为
 $$
2 n ^ { 2 } + \sum _ { k = 1 } ^ { n - 2 } n \times ( 2 \times ( n - k ) + 1 ) \approx n ^ { 3 }
$$
- 因此总的计算次数为
  $$\frac{5}{3}n^3$$

### 使用Givens
- 记转动矩阵 $G _ { 2,1 } = G ( 1,2 , \theta )$，givens变换得到上三角矩阵的过程应该可以记为
$$
\left( G _ { n , n - 1 } G _ { n , n - 2 } G _ { n - 1 , n - 2 } \cdots G _ { 2,1 } \right) A = Q ^ { T } A = R
$$
- 在对第j列的对角元以下的元素进行消元时，仅需计算从第j列到第n列的旋转,每次旋转的计算次数为$2+2\times2\times (n-j+1)$ (对靠右的两条元素进行运算）
  
  那么，对于矩阵R的计算，总共的运算次数为：
$$\sum_{j=1}^{n-1}(n-j)\times(2+2\times2\times (n-j+1))\approx \frac 4 3 n^3$$

- Q的计算为
$$
Q ^ { T } = G _ { n , n - 1 } G _ { n , n - 2 } G _ { n - 1 , n - 2 } \cdots G _ { 2,1 }
$$
其中$G_{i,j}$仅需对第j+1到第n列进行计算，每次计算次数也是$2+2\times2\times (n-j+1)$，因此总计算次数和矩阵R的计算次数相同，也是$\frac 4 3 n^3$次
- 因此总的计算次数为
  $$\frac{8}{3}n^3$$

## (d)
- 编写程序 run_time.py来比较运行时间。
- 这里我不仅仅比较了$n=6$的情况（n表示方阵维度），我取了n=3~50的情况，结果如下图所示。


- 可以看出，在维度较大时，Householder方法会显著地快于Givens变换，这与我们之前的讨论是一致的。在维度较小时，由于运行总时间很小，并不能很有效地比较两种方法的快慢。

# 2. 幂次法求矩阵最大模的本征值和本征矢
## (a)
- 原子满足的经典运动方程为
  $$\ddot{x_i}-[x_{i-1}+x_{i+1}-2x_i]=0$$
- 假设解满足
  $$x_i(t)=x_ie^{-i\omega t}$$
  则有
  $$-\omega^2x_i-[x_{i-1}+x_{i+1}-2x_i]=0$$
  注意到
  $$(-A)_{ij} = \delta_{i-1,j}+\delta_{i+1,j} - 2\delta_{i,j}$$
  于是有
  $$Ax = \lambda x$$
  其中$\lambda = \omega^2$

## (b)
- A的本征值为 $\lambda_1 \gt \lambda_2 \geq \lambda_3 \geq... \geq \lambda_N$，对应的本征矢为 $\bm{v_1},\bm{v_2},\bm{v_3},...,\bm{v_N}$。
- 将$\bm{q^{(0)}}$用本征矢展开
  $$\bm{q^{(0)}} = \sum_{i=1}^{N} a_i \bm{v_i}$$
  第k阶的公式很容易总结得到
  $$\bm{q^{(k)}} = \frac{\bm{z^{(k)}}}{||z^{(k)}||} = \frac{A\cdot \bm{q^{(k)}}}{||z^{(k)}||} = C \sum_{i=1}^N a_i \lambda_i^k \bm{v_i}$$
  其中C是归一化常数。
- $k \rightarrow \infty$ 时，
  $$\lim_{k \rightarrow \infty} \bm{q^{(k)}} = C \lim _ { k \rightarrow \infty } \lambda _ { 1 } ^ { k } \sum _ { i = 1 } ^ { N } a _ { i } \bm{v_{i}} \left( \frac { \lambda _ { i } } { \lambda _ { 1 } } \right) ^ { k } = C \lim _ { k \rightarrow \infty } a _ { 1 } \lambda _ { 1 } ^ { k }\bm{v_{1}}$$
    这是由于
    $$ \left| \frac { \lambda _ { i } } { \lambda _ { 1 } } \right| < 1 , \forall i \neq 1$$
    最后只剩下$\bm{v_1}$这个方向，根据归一化的特性，于是有
    $$\lim_{k \rightarrow \infty} \bm{q^{(k)}} = \bm{v_1}$$
    $$\lim_{k \rightarrow \infty} \bm{\nu^{(k)}} = \lim_{k \rightarrow \infty} \left[ \bm{q^{(k)}} \right] ^ { \dagger } A \bm{q^{(k)}}  = \bm{v_1}^{\dagger} A \bm{v_1} = \lambda_1$$
 - 编写程序 power_method.py 求解结果
    -  最大本征值 $\lambda_1 = 4.0$

    - 对应本征矢
  $[ 0.12013117 -0.23053002  0.3222527  -0.38786838  0.42206128 -0.42206128 0.38786839 -0.3222527   0.23053002 -0.12013117]$

# 3. 关联函数的拟合和数据分析