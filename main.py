from sympy import *
from secao_aurea import *
from armijo import *
from gradiente import gradiente
from dc import dir_conj
x1, x2 = symbols('x1 x2')
variables = [x1, x2]
f1 = x1**2 + 4*x2**2 - 4*x1 - 8*x2
f2 = (x1 - x2**2) * (x1 - 1/2 * x2**2) # problema ilimitado, ponto 0 estacionário porém não minimizador.
f3 = 2*x1**3 - 3*x1**2 - 6*x1 * x2 * (x1 - x2 - 1)
f4 = 1/2 * sin(x1) * sin(x2) + 1/2 * exp(x1**2 + x2**2)

option = [f1, f2, f3, f4, f5]
titulo = 'Bem vindo!'

print(titulo.center(50, '*'))
print('Selecione um dos seguinte metodos (digite um dos numeros correpondentes):\n1 - Metodo do Gradiente\n2 - Direcoes Conjugadas')
opt = int(input('Opcao:' ))
if opt == 1:
	print('Escolha uma das seguintes funcoes:\n1 - f1 = x1**2 + 4*x2**2 - 4*x1 - 8*x2\n2 - f2 = (x1 - x2**2) * (x1 - 1/2 * x2**2)\n3 - f3 = 2*x1**3 - 3*x1**2 - 6*x1 * x2 * (x1 - x2 - 1)\n4 - f4 = 1/2 * sin(x1) * sin(x2) + 1/2 * exp(x1**2 + x2**2)\n')
	opt2 = int(input('Opcao: '))
	if opt2 > 0 and opt2 < 5:
		titulo = 'Executando Método'
		print(titulo.center(50,'-'))
		gradiente(option[opt2-1])
	else:
		print('Opcao invalida.')
elif opt == 2:
	print('Escolha uma das seguintes funcoes:\n1 - f1 = x1**2 + 4*x2**2 - 4*x1 - 8*x2\n2 - f2 = (x1 - x2**2) * (x1 - 1/2 * x2**2)\n3 - f3 = 2*x1**3 - 3*x1**2 - 6*x1 * x2 * (x1 - x2 - 1)\n4 - f4 = 1/2 * sin(x1) * sin(x2) + 1/2 * exp(x1**2 + x2**2)\n')
	opt2 = int(input('Opcao: '))
	if opt2 > 0 and opt2 < 5:
		titulo = 'Executando Método'
		print(titulo.center(50,'-'))
		dir_conj(option[opt2-1])
	else:
		print('Opcao invalida.')
else:
	print('Opcao invalida.')