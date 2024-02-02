'''
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
'''

def conversao(dinheiro):
    dolarAm = dinheiro * 4.91
    pedoArg = dinheiro * 0.02
    dolarAust = dinheiro * 3.18
    dolarCan = dinheiro * 3.64
    francoSui = dinheiro * 0.42
    euro = dinheiro * 5.36
    libra = dinheiro * 6.21

    print(f' Dólar Americano: {dolarAm} \n Peso Argentino: {pedoArg} \n Dólar Australiano: {dolarAust} \n Dólar Canadense: {dolarCan} \n Franco Suiço: {francoSui} \n Euro: {euro} \n Libra esterlina: {libra}')

valorCarteira = float(input('Insira o valor a ser convertido: '))

conversao(valorCarteira)