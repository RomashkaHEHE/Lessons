$a+b=c$
$2x^2-5x+3=0$
$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
$\log_a x+\log_a y=\log_a(xy)$
$e^{i\pi}+1=0$
$\ln\!\left(\frac{x^2+1}{x-1}\right)$
$\sqrt{x^2+y^2+z^2}$
$\sin(x)^2+\cos(x)^2=1$
$\frac{d}{dx}(x^3+\sin x)=3x^2+\cos x$
$\frac{\partial}{\partial x}(x^2y+y^3)=2xy$
$x\in\mathbb{R},\;n\in\mathbb{N}$
$\forall\varepsilon>0\;\exists\delta>0$
$f:\mathbb{R}\to\mathbb{R}$
$|x-a|<\varepsilon$
$\langle a,b\rangle=\|a\|\|b\|\cos\theta$
$\vec{a}+\vec{b}=\vec{c}$
$\|\vec{v}\|=\sqrt{x^2+y^2+z^2}$
$\sum_{k=1}^{n}k=\frac{n(n+1)}{2}$
$\sum_{k=1}^{n}k^2=\frac{n(n+1)(2n+1)}{6}$
$\prod_{k=1}^{n}k=n!$
$\lim_{x\to0}\frac{\sin x}{x}=1$
$\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e$
$\int x^2\,dx=\frac{x^3}{3}+C$
$\int_{0}^{1}x^2\,dx=\frac{1}{3}$
$\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}$
$\nabla f=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)$

$$
\vec{v}=\begin{pmatrix}x\\y\\z\end{pmatrix}
$$

$$
A=\begin{pmatrix}1&2\\3&4\end{pmatrix}
$$

$$
B=\begin{pmatrix}a&b\\c&d\end{pmatrix}
$$

$$
AB=\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}
$$

$$
\det A=ad-bc
$$

$$
A^{-1}=\frac{1}{\det A}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}
$$

$$
\begin{cases}
2x+y=1\\
x-y=3
\end{cases}
$$

$$
\begin{cases}
x+y+z=1\\
2x-y+z=0\\
x+3y-z=5
\end{cases}
$$

$$
\sum_{i=1}^{n}x_i=\frac{1}{2}\,n(x_1+x_n)
$$

$$
\left(\sum_{i=1}^{n}x_i\right)^2=\sum_{i=1}^{n}x_i^2+2\sum_{1\le i<j\le n}x_ix_j
$$

$$
\frac{\sum_{i=1}^{n}x_i y_i}{\sqrt{\sum_{i=1}^{n}x_i^2}\sqrt{\sum_{i=1}^{n}y_i^2}}
$$

$$
\int_{a}^{b}f'(x)\,dx=f(b)-f(a)
$$

$$
\lim_{x\to a}f(x)=L\iff(\forall\varepsilon>0)(\exists\delta>0):0<|x-a|<\delta\Rightarrow|f(x)-L|<\varepsilon
$$
$$
\begin{aligned}
f(x)
&=\frac{x^2-1}{x-1}+\frac{1}{x}\left(\ln(e^{2x})-\ln(e^x)\right) \\[6pt]
&=\frac{(x-1)(x+1)}{x-1}+\frac{1}{x}(2x-x) \\[6pt]
&=x+1+\frac{x}{x} \\[6pt]
&=x+1+1 \\[6pt]
&=x+2
\end{aligned}
$$
$$
\begin{aligned}
S
&=\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}\left(\int_{0}^{1}kx\,dx\right) \\[6pt]
&=\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}\left(k\int_{0}^{1}x\,dx\right) \\[6pt]
&=\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}\frac{k}{2} \\[6pt]
&=\lim_{n\to\infty}\frac{1}{2n}\cdot\frac{n(n+1)}{2} \\[6pt]
&=\lim_{n\to\infty}\frac{n+1}{4} \\[6pt]
&=\infty
\end{aligned}
$$
$$
\begin{aligned}
T
&=\sum_{k=1}^{n}\left(\frac{k^2-k}{k}\right)\cdot\frac{1}{n}\int_{0}^{1}\left(x^2+2x+1\right)\,dx \\[6pt]
&=\sum_{k=1}^{n}(k-1)\cdot\frac{1}{n}\int_{0}^{1}(x+1)^2\,dx \\[6pt]
&=\frac{1}{n}\sum_{k=1}^{n}(k-1)\left[\frac{(x+1)^3}{3}\right]_{0}^{1} \\[6pt]
&=\frac{1}{n}\sum_{k=1}^{n}(k-1)\cdot\frac{7}{3} \\[6pt]
&=\frac{7}{3n}\sum_{k=1}^{n}(k-1) \\[6pt]
&=\frac{7}{3n}\left(\sum_{k=1}^{n}k-\sum_{k=1}^{n}1\right) \\[6pt]
&=\frac{7}{3n}\left(\frac{n(n+1)}{2}-n\right) \\[6pt]
&=\frac{7}{3n}\cdot\frac{n(n-1)}{2} \\[6pt]
&=\frac{7}{6}(n-1)
\end{aligned}
$$
$$
\begin{aligned}
L
&=\lim_{x\to0}\frac{|x|}{x}\cdot\frac{\sqrt{1+x}-1}{x} \\[6pt]
&=\lim_{x\to0}\frac{|x|}{x}\cdot\frac{\sqrt{1+x}-1}{x}\cdot\frac{\sqrt{1+x}+1}{\sqrt{1+x}+1} \\[6pt]
&=\lim_{x\to0}\frac{|x|}{x}\cdot\frac{x}{x(\sqrt{1+x}+1)} \\[6pt]
&=\lim_{x\to0}\frac{|x|}{x}\cdot\frac{1}{\sqrt{1+x}+1} \\[6pt]
&=\frac{1}{2}\lim_{x\to0}\frac{|x|}{x} \\[6pt]
&=\begin{cases}
\frac{1}{2},&x\to0^+\\
-\frac{1}{2},&x\to0^-
\end{cases}
\end{aligned}
$$
$$
\begin{aligned}
F(x)
&=\frac{x^2-1}{x-1}-\frac{x^2-4}{x-2}+\ln\!\left(e^{3x}\right)-\ln\!\left(e^{x}\right)+\frac{\sin x}{x}\cdot x \\[6pt]
&=\frac{(x-1)(x+1)}{x-1}-\frac{(x-2)(x+2)}{x-2}+3x-x+\sin x \\[6pt]
&=(x+1)-(x+2)+2x+\sin x \\[6pt]
&=2x-1+\sin x
\end{aligned}
$$
$$
\begin{aligned}
G(x)
&=\frac{d}{dx}\left(F(x)\right) \\[6pt]
&=\frac{d}{dx}\left(2x-1+\sin x\right) \\[6pt]
&=2+\cos x
\end{aligned}
$$
$$
\begin{aligned}
I
&=\int_{0}^{\pi}\left(2+\cos x\right)\,dx \\[6pt]
&=\left[2x+\sin x\right]_{0}^{\pi} \\[6pt]
&=\left(2\pi+\sin\pi\right)-\left(0+\sin0\right) \\[6pt]
&=2\pi
\end{aligned}
$$
$$
\begin{aligned}
L
&=\lim_{x\to0}\frac{F(x)-F(0)}{x} \\[6pt]
&=\lim_{x\to0}\frac{(2x-1+\sin x)-(-1+0)}{x} \\[6pt]
&=\lim_{x\to0}\frac{2x+\sin x}{x} \\[6pt]
&=\lim_{x\to0}\left(2+\frac{\sin x}{x}\right) \\[6pt]
&=2+1 \\[6pt]
&=3
\end{aligned}
$$
$$
\begin{aligned}
A
&=\begin{pmatrix}
2&-1\\
1&3
\end{pmatrix} \\[6pt]
\det A
&=2\cdot3-(-1)\cdot1 \\[6pt]
&=6+1 \\[6pt]
&=7 \\[10pt]
A^{-1}
&=\frac{1}{\det A}\begin{pmatrix}
3&1\\
-1&2
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
3&1\\
-1&2
\end{pmatrix} \\[10pt]
AA^{-1}
&=\begin{pmatrix}
2&-1\\
1&3
\end{pmatrix}\cdot\frac{1}{7}\begin{pmatrix}
3&1\\
-1&2
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
2\cdot3+(-1)\cdot(-1)&2\cdot1+(-1)\cdot2\\
1\cdot3+3\cdot(-1)&1\cdot1+3\cdot2
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
6+1&2-2\\
3-3&1+6
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
7&0\\
0&7
\end{pmatrix} \\[6pt]
&=\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
\end{aligned}
$$
$$
\begin{aligned}
b
&=\begin{pmatrix}
4\\
5
\end{pmatrix} \\[6pt]
x
&=A^{-1}b \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
3&1\\
-1&2
\end{pmatrix}\begin{pmatrix}
4\\
5
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
3\cdot4+1\cdot5\\
(-1)\cdot4+2\cdot5
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
12+5\\
-4+10
\end{pmatrix} \\[6pt]
&=\frac{1}{7}\begin{pmatrix}
17\\
6
\end{pmatrix} \\[6pt]
&=\begin{pmatrix}
\frac{17}{7}\\
\frac{6}{7}
\end{pmatrix}
\end{aligned}
$$
$$
\begin{aligned}
B
&=\begin{pmatrix}
A&I\\
0&A
\end{pmatrix} \\[6pt]
&=\begin{pmatrix}
2&-1&1&0\\
1&3&0&1\\
0&0&2&-1\\
0&0&1&3
\end{pmatrix} \\[10pt]
B^T
&=\begin{pmatrix}
2&1&0&0\\
-1&3&0&0\\
1&0&2&1\\
0&1&-1&3
\end{pmatrix} \\[10pt]
B^{-1}
&=\begin{pmatrix}
A^{-1}&-A^{-1}IA^{-1}\\
0&A^{-1}
\end{pmatrix} \\[6pt]
&=\begin{pmatrix}
A^{-1}&-(A^{-1})^2\\
0&A^{-1}
\end{pmatrix} \\[6pt]
&=\begin{pmatrix}
\frac{1}{7}\begin{pmatrix}3&1\\-1&2\end{pmatrix}
&-\left(\frac{1}{7}\begin{pmatrix}3&1\\-1&2\end{pmatrix}\right)^2\\
0&\frac{1}{7}\begin{pmatrix}3&1\\-1&2\end{pmatrix}
\end{pmatrix}
\end{aligned}
$$
↓
### Теорема (спектральная для симметричных матриц)
Если $A\in\mathbb{R}^{n\times n}$ и $A^T=A$, то все собственные значения $A$ вещественны, и существует ортогональная матрица $Q$ такая, что
$$
Q^TAQ=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
$$

### Доказательство
**Шаг 1.** Рассмотрим функцию Релея
$$
r(x)=\frac{x^TAx}{x^Tx},\qquad x\neq0.
$$
На единичной сфере $S^{n-1}=\{x:\|x\|=1\}$ имеем $r(x)=x^TAx$. Сфера компактна, функция непрерывна, значит существует $v\in S^{n-1}$, на котором достигается максимум:
$$
\lambda:=v^TAv=\max_{\|x\|=1}x^TAx.
$$

**Шаг 2.** Покажем, что $Av=\lambda v$. Возьмём любой вектор $u$ такой, что $u^Tv=0$, и рассмотрим
$$
\phi(t)=\frac{(v+tu)^TA(v+tu)}{(v+tu)^T(v+tu)}.
$$
Так как $t=0$ — точка максимума (мы движемся по направлениям, касательным к сфере), то $\phi'(0)=0$.

Вычислим производную. Числитель:
$$
(v+tu)^TA(v+tu)=v^TAv+2t\,u^TAv+t^2u^TAu.
$$
Знаменатель:
$$
(v+tu)^T(v+tu)=1+t^2\|u\|^2.
$$
Отсюда
$$
\phi'(0)=2u^TAv.
$$
Значит $u^TAv=0$ для всех $u\perp v$. Это означает, что $Av$ ортогонален $v^\perp$, то есть $Av\in\operatorname{span}(v)$. Следовательно, $Av=\mu v$ для некоторого $\mu\in\mathbb{R}$.

Домножим слева на $v^T$:
$$
v^TAv=\mu v^Tv=\mu.
$$
Но $v^TAv=\lambda$, значит $\mu=\lambda$ и
$$
Av=\lambda v.
$$
В частности, $\lambda$ — вещественное собственное значение.

**Шаг 3.** Докажем инвариантность ортогонального дополнения $W=v^\perp$. Пусть $x\in W$, то есть $v^Tx=0$. Тогда
$$
v^T(Ax)=(A^Tv)^Tx=(Av)^Tx=(\lambda v)^Tx=\lambda v^Tx=0,
$$
значит $Ax\in W$. То есть $W$ инвариантно относительно $A$.

**Шаг 4. (Индукция по размерности.)** Ограничение $A|_W:W\to W$ снова симметрично. По индукции на $W$ существует ортонормированный базис из собственных векторов $(v_2,\dots,v_n)$:
$$
Av_i=\lambda_i v_i,\qquad \lambda_i\in\mathbb{R},\quad i=2,\dots,n.
$$
Добавляя $v_1:=v$, получаем ортонормированный базис $\mathbb{R}^n$ из собственных векторов $A$.

Пусть $Q=[v_1\;v_2\;\cdots\;v_n]$. Тогда $Q$ ортогональна ($Q^TQ=I$) и
$$
Q^TAQ=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
$$
Теорема доказана. $\square$


$$
\begin{aligned}
&\textbf{Теорема.}\;\;A\in\mathbb{R}^{n\times n},\;A^T=A\;\Longrightarrow\;\exists Q\in\mathbb{R}^{n\times n}:\;Q^TQ=I\;\wedge\;Q^TAQ=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\;\lambda_i\in\mathbb{R}.\\[10pt]
&\textbf{Доказательство.}\\[6pt]
&\textbf{(1) Определение.}\;\;\forall x\in\mathbb{R}^n\setminus\{0\}:\;r(x)=\frac{x^TAx}{x^Tx}.\;\;\text{Тогда }\forall x\neq0:\;r(cx)=r(x)\;(\forall c\neq0).\\[6pt]
&\Rightarrow\;\text{достаточно рассматривать }S^{n-1}=\{x\in\mathbb{R}^n:\|x\|=1\},\;\;\forall x\in S^{n-1}:\;r(x)=x^TAx.\\[10pt]
&\textbf{(2) Экстремум.}\;\;S^{n-1}\text{ компактна }\wedge\;x\mapsto x^TAx\text{ непрерывна }\\
&\Longrightarrow\;\exists v\in S^{n-1}:\;\lambda:=v^TAv=\max_{\|x\|=1}x^TAx.\\[10pt]
&\textbf{(3) Собственный вектор.}\;\;\forall u\in\mathbb{R}^n:\;(u^Tv=0)\Rightarrow
\phi(t)=\frac{(v+tu)^TA(v+tu)}{(v+tu)^T(v+tu)}\;\text{ имеет максимум при }t=0.\\[6pt]
&\Rightarrow\;\phi'(0)=0.\\[6pt]
&\phi(t)=\frac{v^TAv+2t\,u^TAv+t^2u^TAu}{1+t^2\|u\|^2}
\;\Longrightarrow\;\phi'(0)=2u^TAv.\\[6pt]
&\Rightarrow\;\forall u:\;(u^Tv=0)\Rightarrow u^TAv=0.\\[6pt]
&\text{Эквивалентно: }\forall u\in v^\perp:\;\langle u,Av\rangle=0\;\Longrightarrow\;Av\in(v^\perp)^\perp=\operatorname{span}(v).\\[6pt]
&\Rightarrow\;\exists \mu\in\mathbb{R}:\;Av=\mu v.\\[6pt]
&v^TAv=\mu v^Tv\;\wedge\;v^Tv=1\;\Longrightarrow\;\mu=v^TAv=\lambda.\\[6pt]
&\Rightarrow\;Av=\lambda v,\;\lambda\in\mathbb{R}.\\[10pt]
&\textbf{(4) Инвариантность }v^\perp.\;\;\forall x\in\mathbb{R}^n:\;(v^Tx=0)\Rightarrow v^T(Ax)=(A^Tv)^Tx=(Av)^Tx=(\lambda v)^Tx=\lambda(v^Tx)=0.\\[6pt]
&\Rightarrow\;\forall x\in v^\perp:\;Ax\in v^\perp,\;\text{т.е. }v^\perp\text{ инвариантно относительно }A.\\[10pt]
&\textbf{(5) Индукция по }n.\;\;\dim(v^\perp)=n-1,\;\;A|_{v^\perp}\text{ симметрична }\\
&\Longrightarrow\;\exists\text{ ортонормированный базис }(v_2,\dots,v_n)\subset v^\perp:\;\forall i\in\{2,\dots,n\}\;\exists \lambda_i\in\mathbb{R}:\;Av_i=\lambda_i v_i.\\[6pt]
&\text{Положим }v_1=v,\;Q=[v_1\;v_2\;\cdots\;v_n].\;\;\Rightarrow\;Q^TQ=I.\\[6pt]
&\forall i,j:\;(Q^TAQ)_{ij}=v_i^TAv_j=v_i^T(\lambda_j v_j)=\lambda_j(v_i^Tv_j)=\lambda_j\delta_{ij}.\\[6pt]
&\Rightarrow\;Q^TAQ=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\;\lambda_i\in\mathbb{R}.\\[6pt]
&\blacksquare
\end{aligned}
$$
