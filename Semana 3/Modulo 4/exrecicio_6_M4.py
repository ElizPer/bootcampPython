'''
Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse exercício
'''
import random

tamanhoPalavra = 0
posicao = []
palavras = ['sabe', 'oxi', 'ola', 'livro', 'lata']
rodadas = 0
usadas = []


#escolhendo a palavra aleatória
palavraAleatoria = random.choice(palavras)

#tamanho palavra
for _ in palavraAleatoria:
    tamanhoPalavra += 1

#substituindo a palavraAleatoria por '_'
palavraAleatoria_espaço = list('_' * tamanhoPalavra)

#posição das letras
def localizacao(palavra, letra):
    for p in range(0, tamanhoPalavra):
        if (palavra[p] == letra):
            posicao.append(p)
    return posicao
    
#print(palavraAleatoria, tamanhoPalavra)
print(f'Iniciando o jogo da forca:\n {palavraAleatoria_espaço}')


#RODADAS
while rodadas <= 6:    
    letraDigitada = input('Digite uma letra ') 
    

    if letraDigitada in palavraAleatoria:
        print(f'A letra {letraDigitada} existe na palavra')
        posicao = localizacao(palavraAleatoria, letraDigitada)
        for i in posicao:
            if (palavraAleatoria_espaço[i] == '_'):
                palavraAleatoria_espaço[i] = letraDigitada 
                
        if("".join(palavraAleatoria_espaço) == palavraAleatoria):
            print(palavraAleatoria_espaço)
            print(f'Parabéns vc completou o jogo da forca, a palavra era {"".join(palavraAleatoria_espaço).upper()} e precisou de {rodadas+1} rodadas para descobrir a palavrar') 
            break             
        print(palavraAleatoria_espaço)
    else:  
        usadas.append(letraDigitada)           
        print(f'Letra incorreta, já utilizadas incorretamente: {usadas} ')  
 
    rodadas +=1
    if(rodadas >=6):
        print('\nO Jogo da Forca acabou')
        print(f'A palavra correta é: {palavraAleatoria.upper()}')
        break
