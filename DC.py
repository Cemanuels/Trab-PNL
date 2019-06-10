from sympy import *
import time
def tam_passo(function, p1, p2, d):
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]
	grad_function = lambdify((x1, x2), derive_by_array(function, (x1, x2)))
	gradiente = Matrix(grad_function(p1, p2))
	hessiana = derive_by_array(derive_by_array(function, (x1, x2)), (x1,x2))
	d = -1 * gradiente
	t = -(gradiente[0]*d[0] + gradiente[1]*d[1])/(((d[0]*hessiana[0,0] + d[1]*hessiana[1,0])*d[0]) + ((d[0]*hessiana[0,1] + d[1]*hessiana[1,1])*d[1]))
	return float(t)
def dir_conj(function, x_in = [0, 0], ite = 100, errorRate=1e-8):
	x1, x2 = symbols('x1 x2')
	variables = [x1, x2]
	t_ini = time.process_time()
	grad_function = lambdify((x1, x2), derive_by_array(function, (x1, x2)))
	hessiana = derive_by_array(derive_by_array(function, (x1, x2)), (x1,x2))
	x_k = Matrix(x_in) 
	d = -1 * Matrix(grad_function(x_in[0], x_in[1]))
	k = 0
	while k < ite:
		if Matrix(grad_function(x_in[0], x_in[1])).norm() < errorRate:
			print(f"Ponto: {x_k}, valor: {function.subs(list(zip(variables, x_k)))}")
			print(f'Total de iteracoes: {k}')
			print(f"Tempo transcorrido: {time.process_time() - t_ini} segundos")
			break
		t_k = tam_passo(function, x_k[0], x_k[1], d)
		x_k = [x_in[i] + t_k*d[i] for i in range(len(x_k))]
		print(f"Ponto: {x_k}, {function.subs(list(zip(variables, x_k)))}")
		grad_x_k = grad_function(x_k[0], x_k[1])
		beta = (((d[0]*hessiana[0,0] + d[1]*hessiana[1,0])*grad_x_k[0]) + ((d[0]*hessiana[0,1] + d[1]*hessiana[1,1])*grad_x_k[1]))/(((d[0]*hessiana[0,0] + d[1]*hessiana[1,0])*d[0]) + ((d[0]*hessiana[0,1] + d[1]*hessiana[1,1])*d[1]))
		d_k = [-1 * grad_x_k[i] + beta*d[i] for i in range(len(grad_x_k))]
		d = d_k
		k += 1
		print
	if k == ite:
		print('Otimo nao encontrado.')
		print(f"Tempo transcorrido: {time.process_time() - t_ini} segundos")