from sympy import *
def funcao_phi(t, function):
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]
	#Ponto inicial
	x_in = Matrix([0, 0])
	#Gradiente
	grad_function = lambdify((x1, x2), derive_by_array(function ,(x1, x2)))
	#Direção de descida
	d = -1 * Matrix(grad_function(x_in[0], x_in[1]))
	print('d: ',d)
	return function.subs(list(zip(variables, x_in + t * d)))

def secao_aurea(ro, epsilon, function):
	#Intervalo [a,b]
	t1 = (3.0 - sqrt(5.0))/2.0
	t2 = 1.0 - t1
	a = 0
	s = ro
	b = 2*ro
	while (funcao_phi(b, function) < funcao_phi(s, function)):
		print(f'phi(b): {funcao_phi(b, function)}, phi(s): {funcao_phi(s, function)}')
		a = s
		print('a: ',a)
		s = b
		b = 2*b
		print('b: ',b)		
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