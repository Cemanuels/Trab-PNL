from sympy import *
x1, x2 = symbols('x1 x2')
variables = [x1, x2]
def tam_passo(function, x1, x2, d):
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]
	grad_function = lambdify((x1, x2), derive_by_array(function, (x1, x2)))
	gradiente = Matrix(grad_function(x1, x2))
	hessiana = derive_by_array(derive_by_array(function, (x1, x2)), (x1,x2))
	d = -1 * gradiente
	t = -(gradiente[0][0]*d[0][0] + gradiente[1][0]*d[1][0])/

def dir_conj(function):
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]
	grad_function = lambdify((x1, x2), derive_by_array(function, (x1, x2)))
	hessiana = derive_by_array(derive_by_array(function, (x1, x2)), (x1,x2))
	x_in = [0, 0]
	d = -1 * Matrix(grad_function(x_in[0], x_in[1]))
	tam_passo(function, x_in[0], x_in[1], d)
	"""while True:
		if grad_function(x_in[0], x_in[1]) == [0, 0]:
			break"""
dir_conj(100*x1 + 200*x2)