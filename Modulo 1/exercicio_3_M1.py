'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.

'''
nroKM = float(input('Digite um valor em km: '))

nroM = nroKM * 1000
nroCM = nroKM * 100000
nroMM = nroKM * 1000000

print('Transformação de Km para m, cm e mm')
print('Km: ', nroKM)
print('Km: ', nroM)
print('Km: ', nroCM)
print('Km: ', nroMM)