from sympy import *

def armijo(function, eta = 0.7, x_in = [0,0]):
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]

	# Gradiente
	grad_function = lambdify((x1, x2), derive_by_array(function ,(x1, x2)))
	# tamanho do passo inicial
	t = 1
	# Ponto inicial
	x = Matrix(x_in)
	# Direcao de descida = -gradiente(x)
	d = -1 * Matrix(grad_function(x[0], x[1]))
	while True:
	    if function.subs(list(zip(variables, x + t * d))) <=\
     		 		function.subs(list(zip(variables, x))) + \
       				eta * t * Matrix(grad_function(x[0], x[1])).dot(d):
	        return t
	    else:
	        t *= eta