'''
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
'''
respostasSIM = []
respostasNAO = []

def interrogatorio(resp):
    if(resp == 'S'):
        respostasSIM.append(resp)
    elif(resp == 'N'):
        respostasNAO.append(resp)
    else:
        print('Valor inválido, resposda "S" ou "N" ')
        resp = input('Responda ')
        interrogatorio(resp)

def participacao():
    if(len(respostasSIM) == 2):
        print('Suspeita(o)')
    elif(len(respostasSIM) > 2 and len(respostasSIM) <= 4 ):
        print('Cúmplice')
    elif(len(respostasSIM) == 5):
        print('Assassino')
    else:
        print('Inocente')

r1 = input('Telefonou para a vítima? ')
interrogatorio(r1)

r2 = input ('Esteve no local do crime? ')
interrogatorio(r2)

r3 = input('Mora perto da vítima? ')
interrogatorio(r3)

r4 = input('Devia para a vítima?')
interrogatorio(r4)

r5 = input('Já trabalhou com a vítima?')
interrogatorio(r5)

print(f'Não: {len(respostasNAO)}')
print(f'Sim: {len(respostasSIM)}')
participacao()