'''
Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.
'''
from operator import add 
from functools import reduce
n = []
vezes = 3

def soma(n1):
    resultado = reduce(add, n1)
    return resultado

for qtd in range(vezes):
    n.append(float(input(f'{qtd+1}- Digite o nro: ')))

print(soma(n))
