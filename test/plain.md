$$
(2+i)z^2+(1-3i)z+(-5-i)=0
$$

$$
\begin{flalign}
&(2+i)z^2+(1-3i)z+(-5-i)=0 & \\
&\begin{split}
\\D &= (1-3i)^2+4(5+i)(2+i)\\
&=1-6i-9+4(10+7i-1) = -8-6i+36+28i\\
&=28+22i
\end{split}\\\\
&\begin{split}
&\text{найдём }\sqrt{D}:\\&a+bi=\sqrt{28+22i}\\&(a+bi)^2=28+22i\\&a^2-b^2+2abi=28+22i\\
&\begin{cases}
a^2+b^2=28 \\
2ab=22
\end{cases}\\
\end{split}
\end{flalign}
$$

$$
\forall\varepsilon>0\;\exists\delta=\delta(\varepsilon):\forall x\in X:|x|>\delta\implies |f(x)-A|<\varepsilon
$$

$$
\int (\frac{2-x}{x})^2dx
$$

$$
\int \frac{dx}{\sqrt{ 3-5x^2 }}
$$
$$
\int e^{ax+b}dx
$$
$$
\int\frac{3}{\cos^2(5x)}dx
$$
$$
\int \frac{dx}{4x^2+9}
$$
$$
\int_{0}^{\pi/4} x\cos^2{x}dx
$$
$$
\int_{1}^{3} \frac{dx}{x^3+x}
$$
$$
\int_{1}^{10}\frac{dx}{x+\sqrt[4]{x}}
$$
$$
f(x)=x^3-5x
$$
$$
\int_{0}^{2\pi}\frac{3+\sin^2{x}}{\sqrt{5+2\sin{x}}}dx
$$
$$
\langle I \rangle =\frac{m<d>^{2}g<t>^{2}<h_{2}>}{4h_{1}(h_{1}+<h_{2}>)}
$$
где $m=m_{0}+Nm_{\text{п}}$; $<h_{2}>$ - 




4.5. Построение графика $M(\varepsilon)$ (**прилагаетя к отчёту**), определение $I_{0}$ и $M_{\text{тр}}$ из графика:
$$
I_{0}=2.26\cdot 10^{-3}\ кг\cdotм^{2};\quad M_{\text{тр}}=1\cdot 10^{-3}\ Н\cdotм
$$
4.6. Расчёт границ погрешностей результатов измерений
а) если использовался метож МНК (обработка результатов на компьютере)
$\varepsilon_{I_{0}}=0.1\cdot10^{-3}\ кг\cdotм^{2};\quad \varepsilon_{M_{\text{тр}}}=0.7\cdot 10^{-3}$

4.7 Окончательные результаты:
$$
\begin{aligned}
 & I_{0}=(\langle I_{0} \rangle\pm\Delta_{I_{0}} )=(226\pm 10)\cdot 10^{-5}\ кг\cdot м^{2}, &  & P=0.95 \\
 & M_{\text{тр}}=(\langle M_{\text{тр}} \rangle\pm\Delta_{M_{\text{тр}}} )=(10\pm 7)\cdot 10^{-4}\ Н\cdotм, &  & P=0.95
\end{aligned}
$$

4.8. Выводы:
С увеличением количества перегрузков увеличивается момент силы натяжения и растет угловое ускорение, следовательно, момент силы натяжения прямо пропорционален массе груза также, как и угловое ускорение, а значит момент силы натяжения прямо пропорционален угловому ускорению.
### альтернативная запись вывода. Берите в пример, как это дело редачить, чобы не засекалось списывание:
Момент силы натяжения и угловое ускорение увеличиваются, если увеличивать количество перегрузков.
$$
\implies M\propto m,\quad \varepsilon \propto m\implies M\propto\varepsilon
$$




Матрица $D$ равна $(2A+B)\cdot C^{\perp}$, где $A=\begin{pmatrix}4 & 1 & 3 \\ 2 & 0 & 5\end{pmatrix}$, $B=\begin{pmatrix}-2 & -5 & -4 \\ 0 & -2 & -3\end{pmatrix}$, $C=\begin{pmatrix}1 & 2 & 5 \\ 3 & 1 & 2\end{pmatrix}$.
Посчитать определитель матрицы $D$
$$
\begin{aligned}
2A+B & =\begin{pmatrix}
8-2 & 2-5 & 6-4 \\
4 & -2 & 10-3
\end{pmatrix} \\[4pt]
 & =\begin{pmatrix}
6 & -3 & 2 \\
4 & -2 & 7
\end{pmatrix}
\end{aligned}
$$
$$
C^{\perp}=\begin{pmatrix}
1 & 3 \\
2 & 1 \\
5 & 2
\end{pmatrix}
$$
$$
\begin{aligned}
\begin{pmatrix}
6 & -3 & 2 \\
4 & -2 & 7
\end{pmatrix} \cdot \begin{pmatrix}
1 & 3 \\
2 & 1 \\
5 & 2
\end{pmatrix} & = \begin{pmatrix}
6 \cdot 1 + (-3) \cdot 2 + 2 \cdot 5 & 6 \cdot 3 + (-3) \cdot 1 + 2 \cdot 2 \\
4 \cdot 1 + (-2) \cdot 2 + 7 \cdot 5 & 4 \cdot 3 + (-2) \cdot 1 + 7 \cdot 2
\end{pmatrix} \\
 & =\begin{pmatrix}
10 & 
\end{pmatrix}
\end{aligned}
$$

Последовательность чисел $a_{1}, a_{2},\dots ,a_{n}$
Можно совершать операцию
- Выбрать две позиции $1\leq i<j\leq n$, такие что $a_{i}=a_{j}$
- Затем, для каждого $i\leq x\leq j$: если $a_{z}<a_{i}$, то замените $a_{x}$ на 0
