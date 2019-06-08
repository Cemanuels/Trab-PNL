from sympy import *
from armijo import *
from secao_aurea import *
import time
x1, x2 = symbols('x1 x2')
variables = [x1, x2]

def gradiente(function, errorRate, ite, x_in):
    t_ini = time.process_time()
	# Gradiente da função
    grad_function = lambdify((x1, x2), derive_by_array(function ,(x1, x2)))
    # Ponto inicial
    x_k = x_in
    k = 0 
    while Matrix(grad_function(x_k[0], x_k[1])).norm() > errorRate and k < ite:
        d_k = -1 * Matrix(grad_function(x_k[0], x_k[1]))
        t_k = armijo(0.7, function)
        x_k = [x_k[i] + t_k*d_k[i] for i in range(len(x_k))]
        k = k + 1
        # print("Ponto: ", x_k)
        # print(f"f({list(x_k)}): ", grad_function(x_k[0], x_k[1]))
    
	    
    if(k < ite):
        print(f"Número total de iterações: {k}")
        print(f"Tempo transcorrido: {time.process_time() - t_ini} segundos")
    else:
        print(f"Número de iterações excedido: {k}")
    
    print(f"Ponto Encontrado: {x_k}")

# Main ---- 

# Funções para teste

f1 = x1**2 + 4*x2**2 - 4*x1 - 8*x2
f2 = (x1 - x2**2) * (x1 - 1/2 * x2**2)
f3 = 2*x1**3 - 3*x1**2 - 6*x1 * x2 * (x1 - x2 - 1)
f4 = 1/2 * sin(x1) * sin(x2) + 1/2 * exp(x1**2 + x2**2)
f5 = 100*(x2 - x1**2)**2 + (1 - x1)**2

# print("Armijo: t = {}".format(armijo(0.7, f2)))
# print("Seção Aurea: t = {}".format(secao_aurea(0.7, 1.4, f2)))


# Gradiente(f1)
# Gradiente(f2)
# Gradiente(f3)
# Gradiente(f4)
# Gradiente(f5)

