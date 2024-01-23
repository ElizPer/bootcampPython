'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''

salarioHora = float(input('Quando você ganha por hora: R$ '))
horasTrab = int(input('Quantas horas você trabalhou no mês: '))

totalSalario = salarioHora * horasTrab

print(f'Seu salário no mês será de R${totalSalario}')

