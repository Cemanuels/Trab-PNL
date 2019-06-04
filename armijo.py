from sympy import *
def armijo():
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]

	# Funcao
	function = 100*(x2 - x1**2)**2 + (1 - x1)**2

	# Gradiente
	grad_function = lambdify((x1, x2), derive_by_array(function ,(x1, x2)))
	# acessar
	# func_result = function.subs(list(zip(variables, x_in))) [(x1, value), (x2, value)] - return value
	# grad_result = grad_function(x_in[0], x_in[1]) (value, value) - reuturn list


	# constante eta entre (0, 1)
	eta = 0.7
	# tamanho do passo inicial
	t = 1
	# Ponto inicial
	x_in = Matrix([0, 0])
	# Direcao de descida, que é -gradiente(x_in)
	d = -1 * Matrix(grad_function(x_in[0], x_in[1]))

	while True:
	    if function.subs(list(zip(variables, x_in + t * d))) < function.subs(list(zip(variables, x_in))) + eta * t * Matrix(grad_function(x_in[0], x_in[1])).dot(d):
	        print(f"Tamanho do passo: {t}")
	        break
	    else:
	        t *= eta
