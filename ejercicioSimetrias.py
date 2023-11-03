import sympy as sym
from sympy import symbols
from sympy.plotting import plot
x = symbols('x')
f1 = 8 - x
f2 = 18 - 3*x

Z1 = 20 - 2*x
Z2 = 10 - 2*x
Z3 = 5 - 2*x

plot(f1, f2, Z1, Z2, Z3, (x, -2, 10), ylim=(-1, 20), legend=True, title='Simetrias')