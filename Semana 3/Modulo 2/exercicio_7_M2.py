'''
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''
idade = int(input('Insira sua idade: '))

if(idade <=12):
    print('É uma criança')
elif(idade <=17):
    print('É um adolescente')
else:
    print('É um adulto')