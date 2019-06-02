from sympy import *
from main import funcao_phi

x1, x2 = symbols('x1 x2')
vars = [x1, x2]

#Função de teste:
function = (x1**2) + 6*(x1*x2) + 4*(x2**2)

x_in = Matrix([0, 0])

def Secao_Aurea(epsilon, ro):
	#Intervalo [a,b]
	t1 = float((3 - sqrt(5))/2)
	t2 = float(1 - t1)
	a = 0
	s = float(ro)
	b = float(2*ro)
	while funcao_phi(s) < funcao_phi(t):
		a = s
		s = b
		b = 2*b
	#Obtenção do tamanho do passo:
	u = a + t1*(b-a)
	v = a + t2*(b-a)

	while b - a > epsilon:
		if funcao_phi(u) < funcao_phi(v):
			b = v
			v = u
			u = a + t1*(b-a)
		else:
			a = u
			u = v
			v = a + t2*(b-a)
			
	return (u + v)/2