'''
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

litrosConsumido = float(input('Insira a quantidade de combustível consumidos (litros): '))
distanciaPercorrida = float(input('Insira a distância percorrida (km): '))

consumoMedio = distanciaPercorrida/litrosConsumido

print(f'O consumo médio é de {consumoMedio}km/l')