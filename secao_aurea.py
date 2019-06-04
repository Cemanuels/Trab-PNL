from sympy import *

x1, x2 = symbols('x1 x2')
variables = [x1, x2]

#Função de teste:
function = 100*(x2 - x1**2)**2 + (1 - x1)**2

grad_function = lambdify((x1, x2), derive_by_array(function ,(x1, x2)))

def funcao_phi(t, function):
	#Ponto inicial
	x_in = Matrix([0, 0])
	#Direção de descida
	d = -1 * Matrix(grad_function(x_in[0], x_in[1]))
	return function.subs(list(zip(variables, x_in + t * d)))

def secao_aurea(epsilon, ro, function):
	#Intervalo [a,b]
	t1 = float((3 - sqrt(5))/2)
	t2 = float(1 - t1)
	a = 0
	s = ro
	b = 2*ro
	while (funcao_phi(s, function) < funcao_phi(b, function)):
		a = s
		s = b
		b = 2*b		
	#Obtenção do tamanho do passo:
	u = a + t1*(b-a)
	v = a + t2*(b-a)

	while b - a > epsilon:
		if funcao_phi(u, function) < funcao_phi(v, function):
			b = v
			v = u
			u = a + t1*(b-a)
		else:
			a = u
			u = v
			v = a + t2*(b-a)
	return float((u + v)/2)