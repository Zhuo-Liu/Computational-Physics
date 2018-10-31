<center> 
<font size=6> 计算物理第二次作业</font> <br>
<font size=3> 刘茁 </font> <br>
<font size=3> 1500011438 </font>
</center>

# 3. 含有zeta函数的方程求解
## (a)
- 在$l=m=0$的情形下，将$Z$写成四项
$$
Z_{00} (1;q^2)= \frac{e^{q^2}}{\sqrt{4\pi}} \sum_{\mathbf{n}} \frac{e^{-\mathbf{n}^2}}{\mathbf{n}^2-q^2} +\frac{\sqrt{\pi}}{2}\int_{0}^{1} dt\cdot t^{-3/2}e^{tq^2}\sum_{\mathbf{n} \ne 0}e^{-(\pi^2/t)\mathbf{n}^2}+ \frac{\pi}{2}\int_0^{1} dt\cdot t^{-3/2}(e^{tq^2}-1)-\pi 
$$

- 首先关注第一项，令$D(x)$为满足$|\mathbf{n}^2|=x$的$\mathbf{n}$的个数。为了确定误差范围，我们关注$|\mathbf{n}|\ge n_0$的项的上界，之后我们统一记为R

$$R=\sum_{|\mathbf{n}^2|\ge n_0^2} \frac{e^{-\mathbf{n}^2}}{\mathbf{n}^2-q^2}=\sum_{x\ge n_0^2} \frac{e^{-x}}{x-q^2}\cdot D(x)$$

被求和式随$|\mathbf{n}|$的增大显然单调递减，因此
$$ R\le \sum_{r\ge n_0}\frac{e^{-r^2}}{r^2-q^2}\left(\sum_{r^2\le x<(r+1)^2}D(x)\right)$$
$\sum_{r^2\le x<(r+1)^2}D(x)$为半径$r$到$r+1$球壳中的格点数，在$r$较大时可近似为$4\pi r^2$,将上界改写为积分形式
$$\begin{aligned}
R &\le \sum_{r\ge n_0}\frac{e^{-r^2}}{r^2-q^2}\left(\sum_{r^2\le x<(r+1)^2}D(x)\right)\\
& \approx \int_{n_0}^\infty 4\pi r^2 \frac{e^{-r^2}}{r^2-q^2} dr\\
& = \int_{n_0}^\infty \left(1+\frac {q^2}{r^2-q^2}\right) 4\pi e^{-r^2} dr\\
& \le \left(1+\frac {3}{n_0^2-3}\right)\cdot 2\pi^{3/2}(1-erf(n_0))
\end{aligned} $$

取$n_0=4$时
$$R\le 2.1\times 10^{-7}$$
足以达到6位有效数字的精度；若要达到12位有效数字，则$n_0$需取6

- 再来关注第二项。交换求和号和积分号的顺序（收敛性允许我们这么做），我们得到第三项的R可以表示为
$$R\le\frac{\sqrt{\pi}}{2}e^{q^2}\sum_{|\mathbf{n}|\ge n_0}\int_{0}^{1} dt\cdot t^{-3/2}e^{-(\pi^2/t)\mathbf{n}^2}$$
令$x=\frac 1 {\sqrt{t}}$，有
$$R\le\sqrt{\pi}e^{q^2}\sum_{|\mathbf{n}|\ge n_0}\int_{1}^{\infty}e^{-\pi^2\mathbf{n}^2x^2}dx=\frac{e^{q^2}}{\pi^{(3/2)}}\sum_{|\mathbf{n}|\ge n_0}\frac{e^{-\pi^2\mathbf{n}^2}}{\mathbf{n}^2}$$
  与第一项同样的做法，将求和转化为积分，并令$r=|\mathbf{n}|\pi$
$$\begin{aligned}
R & \approx \sqrt{\pi}e^{q^2}\int_{n_0}^\infty 4\pi r^2 \frac{e^{-r^2}}{r^2} dr\\
& = 4 \pi^{3/2}e^{q^2} \int_{n_0}^\infty  e^{-r^2} dr\\
& \le 2\pi e^{q^2}\mathrm{erfc}(\pi n_0)
\end{aligned} $$
注意$q^2<3$，当$n_0$取$2$时，
$$R\le8.0\times10^{-17}$$
在相同的$n_0$下，这一项的大小远远小于第一项，因此可以忽略。

- 最后来看第三项。第三项是一个瑕积分，真正计算的时候可以利用泰勒展开来处理。
$$e^{tq^2}=\sum_{m=0}\frac {(tq^2)^m}{m!}$$
代入原式中，交换求和和积分的顺序(积分收敛时允许我们这么做)
$$\frac{\pi}{2}\int_{0}^{1} dt\cdot t^{-3/2}(e^{tq^2}-1)=\frac {\pi}{2}\sum_{m=1}^{\infty}\frac{q^{2m}}{m!(m-\frac 1 2)}$$
这就化为和上面一样的截断问题。假设当$m=m_0-1$时截断，则与上面一样，R可以表示为
$$
\begin{aligned}
R & =\frac{\pi}{2}\sum_{m=m_0}^{\infty}\frac{q^{2m}}{m!(m-\frac 1 2)}\\
& <\frac{\pi}{2}\sum_{m=m_0}^{\infty}\frac{q^{2m}}{m!} \\
& <e^{q^2}\cdot\frac {(q^2)^{m_0+1}}{(m_0+1)!} \\
& <e^3\cdot\frac {3^{(m_0+1)}}{(m_0+1)!} \end{aligned}
$$
计算发现当$m_0=18$时余项不超过$1\times 10^{-7}$，当$m_0=25$时余项不超过$1\times 10^{-12}$，则该级数只需求和到$m=17$和$m=24$即可达到6位和12位有效数字的要求。

- 最后需要注意的是，我们的讨论是基于函数准确值是在10的0次方量级的。这一假设在绝大多数情况是成立的。但是，也存在一些特殊的情况。比如第一项的求和在$q^2 \to 0,1,2$的情况下是趋于无穷大的。

## (b)