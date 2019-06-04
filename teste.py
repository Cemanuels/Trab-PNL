from secao_aurea import *
from sympy import *

x1, x2 = symbols('x1 x2')
variables = [x1, x2]
x_in = Matrix([0,0])
#Função de teste:
function = 100*(x2 - x1**2) + (1 - x1)

print(secao_aurea(0.7, 1.4, function))