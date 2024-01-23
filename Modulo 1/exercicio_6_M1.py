'''
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''
import math
distanciaPercorrida = float(input('Insira a distância da viagem (km): '))
aviao = distanciaPercorrida/600 
carro = distanciaPercorrida/100
onibus = distanciaPercorrida/80

minutoAv, horaAv = math.modf(aviao)
calculoMinAv = round(minutoAv * 60)

minutoCar, horaCar = math.modf(carro)
calculoMinCar = round(minutoCar * 60)

minutoBus, horaBus = math.modf(onibus)
calculoMinBus = round(minutoBus * 60)


print(f'O tempo de viagem para cada transporte: \nAvião: {round(horaAv)}:{calculoMinAv}h \nCarro: {round(horaCar)}:{calculoMinCar}h \nÔnibus: {round(horaBus)}:{calculoMinBus}h')
