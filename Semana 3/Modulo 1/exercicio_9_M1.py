'''
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
'''

hrExercicios = int(input('Insira a quantidade de tempo realizadas em exercícios por semana (minutos): '))

calorias = hrExercicios * 5
caloriasTot = calorias * 4

print(f'Total de calorias gasta ao mês: {caloriasTot}')