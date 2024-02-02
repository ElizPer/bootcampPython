'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
'''
pesoKg = float(input('Insira seu pego (Kg): '))
alturaM = float(input('Insiera sua altura (m): '))

imc = pesoKg / (alturaM * alturaM)

print(f'Seu índice de massa corporal (IMC) é de: {imc:.2f}')