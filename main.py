from sympy import *
from secao_aurea import *
from armijo import *
from gradiente import gradiente
x1, x2 = symbols('x1 x2')
variables = [x1, x2]
x_in = [0, 0]
f1 = x1**2 + 4*x2**2 - 4*x1 - 8*x2
gradiente(f1, 1e-10, 1000, [0, 0])