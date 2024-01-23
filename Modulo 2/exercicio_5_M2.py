'''
Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
'''
lado1 = float(input('1°- Digite o comprimento do primeiro lado do triângulo: '))
lado2 = float(input('2°- Digite o comprimento do segundo lado do triângulo: '))
lado3 = float(input('3°- Digite o comprimento do terceiro lado do triângulo: '))

if(lado1 == lado2 == lado3):
    print('É um triângulo equilátero')
elif((lado1 == lado2 or lado1 == lado3 or lado2 == lado3) and (lado1 != lado2 or lado1 != lado3 or lado2 != lado3)):
    print('É um triângulo isósceles')
else:
    print('É um triângulo escaleno')