from sympy import *
from secao_aurea import *

x1, x2 = symbols('x1 x2')
variables = [x1, x2]

function = 100*(x2 - x1**2)**2 + (1 - x1)**2 

secao_aurea(0.1, 0.2, function)
print(secao_aurea(0.1, 0.2, function))
