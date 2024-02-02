'''
Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
'''

num1 = int(input('1-Insira um número inteiro: '))
num2 = int(input('2-Insira um número inteiro: '))
num3 = int(input('3-Insira um número inteiro: '))

if(num1 > num2):
    if(num1 > num3):
        print(f'Número {num1} é o maior entre os três')
    else:
        print(f'Número {num3} é o maior entre os três')
elif(num2 > num3):
    print(f'Número {num2} é o maior entre os três')
else:
    print(f'Número {num3} é o maior entre os três')
