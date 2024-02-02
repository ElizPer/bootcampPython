'''
Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.

C > F = (C*1.8) + 32
F > C = (32 - F) /1.8
'''
def celfah(nC):
    calculoCF = (nC * 1.8) + 32
    return calculoCF

def fahcel(nF):
    calculoFC =  (nF - 32) / 1.8
    return calculoFC

converter = input('Deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa? S ou N ')
    
if(converter == 'S' or converter == 's'):
    escolha = input('Deseja converter para Celsius ou Fahrenheit? Digitar C ou F, respectivamente: ')
    if(escolha == 'F' or escolha == 'f'):
        valorCels = float(input('Digite o grau em Celsius: '))
        print(f'Temperatura em fahrenheit: {celfah(valorCels):.2f}')
    elif(escolha == 'C' or escolha == 'c'):
        valorFah = float(input('Digite o grau em Fahrenheit: '))
        print(f'Temperatura em celsius: {fahcel(valorFah):.2f}')
    else:
        print('Valor incorreto')
elif(converter == 'N' or converter == 'n'):
    print('Não deseja converter!')
else:
    print('Valor incorreto')
