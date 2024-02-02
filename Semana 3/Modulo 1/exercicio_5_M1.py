'''
Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''

salarioBruto = float(input('Insira seu salário bruto: '))

if(salarioBruto <= 1903.98):
    print(f'Livre de imposto, seu sálario liquido é de {salarioBruto}')
elif(salarioBruto >1903.98 and salarioBruto <=2826.65):
    descontoIR = salarioBruto*0.075
    salarioLiquido = salarioBruto - descontoIR
    print(f'O desconto do imposto de renda é de R${descontoIR} e o salário liquído será de R${salarioLiquido}')
elif(salarioBruto >=2826.66 and salarioBruto <=3751.05):
    descontoIR = salarioBruto*0.15
    salarioLiquido = salarioBruto - descontoIR
    print(descontoIR)
    print(f'O desconto do imposto de renda é de R${descontoIR} e o salário liquído será de R${salarioLiquido}')
elif(salarioBruto >=3751.06 and salarioBruto <=4664.68):
    descontoIR = salarioBruto*0.225
    salarioLiquido = salarioBruto - descontoIR
    print(f'O desconto do imposto de renda é de R${descontoIR} e o salário liquído será de R${salarioLiquido}')
else:
    descontoIR = salarioBruto*0.275
    salarioLiquido = salarioBruto - descontoIR
    print(f'O desconto do imposto de renda é de R${descontoIR} e o salário liquído será de R${salarioLiquido}')