'''
Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
'''

num1 = float(input("Digite um número: "))
num2 = float(input("Digite mais um número: "))

soma=num1 + num2
subtracao=num1 - num2
multiplicacao=num1 * num2
divisão=num1 / num2

print('Resultados das principais operações matemática: soma, subtração, multiplicação e divisão')
print(f'Soma: {soma:.2f}')
print(f'Subtração: {subtracao:.2f}')
print(f'Multiplicação: {multiplicacao:.2f}')
print(f'Divisão: {divisão:.2f}')
