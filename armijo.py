from sympy import *

x1, x2 = symbols('x1 x2')
vars = [x1, x2]

# Funcao
func = 100*(x2 - x1**2)**2 + (1 - x1)**2

# Gradiente
grad_f = lambdify((x1, x2), derive_by_array(func ,(x1, x2)))

# acessar
# func_result = func.subs(list(zip(vars, p))) [(x1, value), (x2, value)] - return value
# grad_result = grad_f(p[0], p[1]) (value, value) - reuturn list


# constante o entre (0, 1)
o = 0.7
# tamanho do passo inicial
t = 1
# Ponto inicial
p = Matrix([0, 0])
# Direcao de descida, que é -gradiente(p)
d = -1 * Matrix(grad_f(p[0], p[1]))

while True:
    if func.subs(list(zip(vars, p + t * d))) < func.subs(list(zip(vars, p))) + o * t * Matrix(grad_f(p[0], p[1])).dot(d):
        print(f"Tamanho do passo: {t}")
        break
    else:
        t *= o