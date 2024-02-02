'''
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''
nro = int(input('Inserira um número: '))
listaPar = []
listaImpar = []

while nro !=0:
    if(nro > 0):
        if(nro%2==0):
            listaPar.append(nro)
        else:
            listaImpar.append(nro)
        nro = int(input('Inserira um novo número ou para sair aperto o número 0: '))
    else:
        print('Número inválido, somente valores positivos.')

par = len(listaPar)
impar = len(listaImpar)
print(f'Quantidade de números par é de {par}')
print(f'Quantidade de números impar é de {impar}')