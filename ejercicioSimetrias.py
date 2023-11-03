import sympy as sym
from sympy import symbols
from sympy.plotting import plot
x = symbols('x')


#estas para el primer cuadrante x1 >= 0, x2 >= 0
f1 = 8 - x
f2 = 18 - 3*x
Z1 = 20 - 2*x
Z2 = 10 - 2*x
Z3 = 5 - 2*x

#estas para el segundo cuadrante x1 <= 0, x2 >= 0 Cambio el signo de x1 a negativo
f3 = 8 + x
f4 = 18 + 3*x
Z4 = 20 + 2*x
Z5 = 10 + 2*x
Z6 = 5 + 2*x

#estas para el tercer cuadrante x1 <= 0, x2 <= 0 Cambio el signo de x1 a negativo y el de x2 tambien
f5 = -8 - x
f6 = -18 - 3*x
Z7 = -20 - 2*x
Z8 = -10 - 2*x
Z9 = -5 - 2*x

plot(f1, f2, Z1, Z2, Z3, (x, -2, 10), ylim=(-1, 20), legend=True, title='Simetrias')
plot(f3, f4, Z4, Z5, Z6, (x, -10, 10), ylim=(-10, 20), legend=True, title='Simetrias')
plot(f5, f6, Z7, Z8, Z9, (x, -10, 10), ylim=(-10, 20), legend=True, title='Simetrias')