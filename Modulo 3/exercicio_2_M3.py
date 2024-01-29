'''
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
'''
media = []
alunos = 3

def Media(n1, n2, n3, n4):
    print(n1, n2, n3, n4)
    nota = (n1+n2+n3+n4)/4
    media.append(nota)

def Resultado():
    contador = 0
    for md in media:
        if(md >= 7):
            contador= contador+1
    return contador

def TesteNotas():
    for md in media:
        print(md)

def Condicao(x):
    n = float(input(f'Digite aqui a nota {x}: '))
    if(n >=0 and n <=10):
        return n
    else:
        print('Nota inválida, somente notas entre 0 e 10')
        return Condicao(x)

for aluno in range(alunos):
    print(f'Insira a nota do aluno {aluno+1} entre 0 e 10: ')
    nota1 = Condicao(1)
    nota2 = Condicao(2)
    nota3 = Condicao(3)
    nota4 = Condicao(4)
    Media(nota1, nota2, nota3, nota4)

TesteNotas()

print(f'Quantidade de alunos com nota igual ou maior que 7 são: {Resultado()}')
