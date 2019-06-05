from sympy import *
from secao_aurea import *
from armijo import *
x1, x2 = symbols('x1 x2')
variables = [x1, x2]
x_in = [0, 0]
function = x1**2 - 8*x1 + 16

print(secao_aurea(0.5, 0.01, function))