'''
Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.
'''
import re
from collections import Counter

contar = 0

def contarvogais(palavra):
    vogais ='aeiouAEIOU'
    global contar
    for letra in palavra:
       if(letra in vogais):
            contar = contar + 1;
    return contar

palavra = input('Escreva uma palavra: ')
print(contarvogais(palavra))