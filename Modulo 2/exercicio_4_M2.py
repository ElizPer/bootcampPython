'''
Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
'''
nota=float(input('Digite uma nota de 0 a 10: '))
bol = True

while bol:
    if nota < 0 or nota > 10:
        print('Nota inválida, nota precisa ser entre 0 e 10')
        nota=float(input('Digite uma nota de 0 a 10: '))
    elif nota >=7:
        print('Aprovado')
        bol = False
    elif nota <7:
        print('Reprovado')
        bol = False
