$a+b=c$
$2x^{2}-5x+3=0$
$x=\frac{-b\pm \sqrt{ b^{2}-4ac }}{2a}$
$\log_{a}x+\log_{a}y=\log_{a}(xy)$
$e^{i\pi}+1=0$
$\ln\left( \frac{x^{2}+1}{x-1} \right)$
$\sqrt{ x^{2}+y^{2} +z^{2}}$
$\sin(x)^{2}+\cos(x)^{2}=1$
$\frac{d}{dx}(x^{3}+\sin x)=3x^{2}+\cos x$
$\frac{\partial}{\partial x}(x^{2}y+y^{3})=2xy$
$x\in \mathbb{R},\;n \in \mathbb{N}$
$\forall\varepsilon>0\;\exists\delta>0$
$f:\mathbb{R}\to \mathbb{R}$
$|x-a|<\varepsilon$
$\left< a,b \right>=\lVert a \rVert\lVert b \rVert\cos\theta$
$\vec{a}+\vec{b}=\vec{c}$
$\lVert \vec{v} \rVert=\sqrt{ x^{2}+y^{2}+z^{2} }$
$\sum_{k=1}^{n}k=\frac{n(n+1)}{2}$
$\sum_{k=1}^{n}k^{2}=\frac{n(n+1)(2n+1)}{6}$
$\prod_{k=1}^{n}k=n!$
$\lim_{ x \to 0 } \frac{\sin x}{x}=1$
$\lim_{ n \to \infty }\left( 1+\frac{1}{n} \right)^{n}=e$
$\int x^{2} \, dx=\frac{x^{3}}{3}+C$
$\int_{0}^{1} x^{2} \, dx=\frac{1}{3}$
$\int_{-\infty}^{\infty} e^{-x^{2}} \, dx=\sqrt{ \pi }$
$\nabla f=(\frac{ \partial f }{ \partial x },\frac{ \partial f }{ \partial y },\frac{ \partial f }{ \partial z })$
$$
\vec{v}=\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
$$
$$
A=\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$
$$
B=\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$
$$
AB=\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$
$$
\det A=ad-bc
$$
$$
A^{-1}=\frac{1}{\det A}\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$
$$
\begin{cases}
2x+y=1 \\
x-y=3
\end{cases}
$$
$$
\begin{cases}
x+y+z=1 \\
2x-y+z=0 \\
x+3y-z=5
\end{cases}
$$
$$
\sum_{i=1}^{n} x_{i}=\frac{1}{2}n(x_{1}+x_{n})
$$
$$
\left( \sum_{i=1}^{n} x_{i} \right)^{2}=\sum_{i=1}^{n} x_{i}^{2}+2\;\;\sum_{1\leq i<j\leq n}^{} x_{i}x_{j}
$$
$$
\frac{\sum_{i=1}^{n} x_{i}x_{j}}{\sqrt{ \sum_{i=1}^{n} x_{i}^{2} }\sqrt{ \sum_{i=1}^{n} y_{i}^{2} }}
$$
$$
\int_{a}^{b} f'(x) \, dx =f(b)-f(a)
$$
$$
\lim_{ x \to a } f(x)=L\iff(\forall\varepsilon>0)(\exists\delta>0):0<\lvert x-a \rvert <\delta\implies \lvert f(x)-L \rvert <\varepsilon
$$
$$
\begin{aligned}
f(x) & =\frac{x^{2}-1}{x-1}+\frac{1}{x}(\ln(e^{2x})-\ln(e^{x})) \\[6pt]
 & =\frac{(x-1)(x+1)}{x-1}+\frac{1}{x}(2x-x) \\[6pt]
 & =x+1+\frac{x}{x} \\[6pt]
 & =x+1+1 \\[6pt]
 & =x+2
\end{aligned}
$$
$$
\begin{aligned}
S & = \lim_{ n \to \infty } \frac{1}{n}\sum_{k=1}^{n}\left( \int_{0}^{1} kx \, dx  \right) \\
 & = \lim_{ n \to \infty } \frac{1}{n}\sum_{k=1}^{n} \left( k\int_{0}^{1} x \, dx  \right) \\
 & =\lim_{ n \to \infty } \frac{1}{n}\sum_{k=1}^{n} \frac{k}{2} \\
 & =\lim_{ n \to \infty } \frac{1}{2n}\cdot\frac{n(n+1)}{2} \\
 & =\lim_{ n \to \infty } \frac{n+1}{4} \\
 & =\infty
\end{aligned}
$$
$$
\begin{aligned}
T & =\sum_{k=1}^{n} \left( \frac{k^{2}-k}{k} \right)\cdot \frac{1}{n}\int_{0}^{1} \left( x^{2}+2x+1 \right)  \, dx \\[6pt]
 & =\sum_{k=1}^{n} \left( k-1 \right) \cdot \frac{1}{n} \int_{0}^{1} \left( x+1 \right) ^{2} \, dx  \\[6pt]
 & =\frac{1}{n}\sum_{k=1}^{n} \left( k-1 \right) \left[ \frac{\left( x+1 \right) ^{3}}{3} \right] _{0}^{1} \\[6pt]
 & =\frac{1}{n}\sum_{k=1}^{n} \left( k-1 \right) \cdot \frac{7}{3} \\[6pt]
 & =\frac{7}{3n}\sum_{k=1}^{n} \left( k-1 \right)  \\[6pt]
 & = \frac{7}{3n} \left( \sum_{k=1}^{n} k-\sum_{k=1}^{n} 1 \right)  \\[6pt]
 & =\frac{7}{3n}\left( \frac{n\left( n+1 \right) }{2}-n \right)  \\[6pt]
 & = \frac{7}{3n}\cdot \frac{n\left( n-1 \right) }{2} \\[6pt]
 & =\frac{7}{6}\left( n-1 \right) 
\end{aligned}
$$
$$
\begin{aligned}
L & =\lim_{ x \to 0 } \frac{\lvert x \rvert }{x}\cdot \frac{\sqrt{ 1+x }-1}{x} \\[6pt]
 & =\lim_{ x \to 0 } \frac{\lvert x \rvert }{x}\cdot\frac{\sqrt{ 1+x }-1}{x}\cdot\frac{\sqrt{ 1+x }+1}{\sqrt{ 1+x }+1} \\[6pt]
 & =\lim_{ x \to 0 } \frac{\lvert x \rvert }{x}\cdot\frac{x}{x(\sqrt{ 1+x }+1) } \\[6pt]
 & =\lim_{ x \to 0 } \frac{\lvert x \rvert }{x}\cdot\frac{1}{\sqrt{ 1+x }+1} \\[6pt]
 & =\frac{1}{2}\lim_{ x \to 0 } \frac{\lvert x \rvert }{x} \\[6pt]
 & =\begin{cases}
\frac{1}{2}, & x\to 0^{+} \\
-\frac{1}{2}, & x\to 0^{-}
\end{cases}
\end{aligned}
$$
$$
\begin{aligned}
F(x) & = \frac{x^{2}-1}{x-1}- \frac{x^{2}-4}{x-2} + \ln(e^{3x}) - \ln(e^{x}) + \frac{\sin x}{x} \cdot x \\[6pt]
 & = \frac{(x-1)(x+1)}{x-1} - \frac{(x-2)(x+2)}{x-2} + 3x - x + \sin x \\[6pt]
 & =(x+1) - (x+2) +2x + \sin x \\[6pt]
 & = 2x-1+\sin x
\end{aligned}
$$
$$
\begin{aligned}
G(x) & =\frac{d}{dx}\left( F(x) \right)  \\
 & =\frac{d}{dx}\left( 2x-1+\sin x \right)  \\
 & =2+\cos x
\end{aligned}
$$
$$
\begin{aligned}
I & =\int_{0}^{\pi} \left( 2+\cos x \right)  \, dx  \\[6pt]
 & = \left[ 2x+\sin x \right] _{0}^{\pi} \\[6pt]
 & =\left( 2\pi+\sin \pi \right)  - \left( 0+\sin 0 \right) \\[6pt]
 & =2\pi 
\end{aligned}
$$
$$
\begin{aligned}
L & =\lim_{ x \to 0 } \frac{F(x)-F(0)}{x} \\[6pt]
 & =\lim_{ x \to 0 } \frac{(2x-1+\sin x)-(-1+0)}{x} \\[6pt]
 & =\lim_{ x \to 0 } \frac{2x+\sin x}{x} \\[6pt]
 & =\lim_{ n \to 0 } \left( 2+\frac{\sin x}{x} \right) \\[6pt]
 & = 2 + 1 \\[6pt]
 & = 3
\end{aligned}
$$
$$
\begin{aligned}
 & A=\begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix} \\[9pt]
 & \begin{aligned}
\det A  & = 2\cdot 3 - (-1) \cdot 1 \\[6pt]
 & =6+1 \\[6pt]
 & =+7
\end{aligned} \\[9pt]
 & \begin{aligned}
A^{-1} & =\frac{1}{\det A}\begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix} \\[6pt]
 & =\frac{1}{7}\begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix}
\end{aligned} \\[9pt]
 & \begin{aligned}
AA^{-1} & =\begin{pmatrix}
2 & -1 \\
1 & 3
\end{pmatrix} \cdot \frac{1}{7} \begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix} \\[6pt]
 & =\frac{1}{7} \begin{pmatrix}
2 \cdot 3 + (-1) \cdot(-1) & 2 \cdot 1 + (-1) \cdot 2 \\
1 \cdot 3 + 3 \cdot (-1) & 1 \cdot 1 + 3 \cdot 2
\end{pmatrix} \\[6pt]
 & =\frac{1}{7} \begin{pmatrix}
6 + 1  & 2 - 2 \\
3 - 3 & 1 + 6
\end{pmatrix} \\[6pt]
 & =\frac{1}{7} \begin{pmatrix}
7 & 0 \\
0 & 7
\end{pmatrix} \\[6pt]
 & =\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
\end{aligned}
\end{aligned}
$$
$$
\begin{aligned}
 & b = \begin{pmatrix}
4 \\
5
\end{pmatrix} \\[9pt]
 & \begin{aligned}
x & =A^{-1}b \\[6pt]
 & =\frac{1}{7}\begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix} \begin{pmatrix}
4 \\
5
\end{pmatrix} \\[6pt]
 & =\frac{1}{7}\begin{pmatrix}
3 \cdot 4 + 1 \cdot 5 \\
(-1) \cdot 4 + 2 \cdot 5
\end{pmatrix} \\[6pt]
 & = \frac{1}{7} \begin{pmatrix}
12 + 5 \\
-4 + 10
\end{pmatrix} \\[6pt]
 & =\frac{1}{7} \begin{pmatrix}
17 \\
6
\end{pmatrix} \\[6pt]
 & = \begin{pmatrix}
\frac{17}{7} \\
\frac{6}{7}
\end{pmatrix}
\end{aligned}
\end{aligned}
$$
$$
\begin{aligned}
 & \begin{aligned}
B & = \begin{pmatrix}
A & I \\
0 & A
\end{pmatrix} \\[6pt]
 & = \begin{pmatrix}
2 & -1 & 1 & 0 \\
1 & 3 & 0 & 1 \\
0 & 0 & 2 & -1 \\
0 & 0 & 1 & 3
\end{pmatrix}
\end{aligned} \\[9pt]
 & B^{T} = \begin{pmatrix}
2 & 1 & 0 & 0 \\
-1 & 3 & 0 & 0 \\
1 & 0 & 2 & 1 \\
0 & 1 & -1 & 3
\end{pmatrix} \\[9pt]
 & \begin{aligned}
B^{-1} & = \begin{pmatrix}
A^{-1} & -A^{-1}IA^{-1} \\
0 & A^{-1}
\end{pmatrix} \\[6pt]
 & = \begin{pmatrix}
A^{-1} & -(A^{-1})^{2} \\
0 & A^{-1}
\end{pmatrix} \\[6pt]
 & = \begin{pmatrix}
\frac{1}{7}\begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix} & -\left( \frac{1}{7} \begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix} \right) ^{2} \\
0 & \frac{1}{7}\begin{pmatrix}
3 & 1 \\
-1 & 2
\end{pmatrix}
\end{pmatrix}
\end{aligned}
\end{aligned}
$$
