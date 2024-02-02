'''
Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
'''
from datetime import date

anoNascimento = int(input('Insira o ano do seu nascimento: '))
ano = date.today().year
calcIdade = ano - anoNascimento

print(f'Sua idade é: {calcIdade}')