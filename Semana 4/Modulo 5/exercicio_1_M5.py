'''
1. Crie uma classe que modele o objeto "carro". 
2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade. 
3. Um carro temos seguintes comportamentos: liga,desliga,acelera, desacelera. 
4. Crie uma instância da classe carro. 
5. Faça o carro "andar" utilizando os métodos da sua classe. 
6. Faça o carro "parar" utilizando os métodos da sua classe. 
'''
#Crie uma classe que modele o objeto "carro"
class Carro:
    def __init__(self): #metodo construtor com vários atributos
        self.ligada = False
        self.cor = 'preto'
        self.modelo = 'HB20'
        self.velocidade = 0
        self.velocidadeMin = 0
        self.velocidadeMax = 200

    def __str__(self) -> str:
        return f'Carro - ligado: {self.ligada} - cor: {self.cor} - modelo: {self.modelo} - velocidade: {self.velocidade}km '
  
    def ligarCarro(self):
        self.ligada = True

    def desligarCarro(self):
        self.ligada = False 
    
    def aumentarVelocidade(self):
        if not self.ligada:
            return
        if self.velocidade < self.velocidadeMax:
            self.velocidade += 20
    
    def diminuirVelocidade(self):
        if not self.ligada:
            #print (f'Carro está na velocidade {self.velocidade}')
            return 
        if self.velocidade > self.velocidadeMin:
            self.velocidade -= 20
        else:
            print (f'Carro está na velocidade {self.velocidade}km, não tem como diminuir')

    def pararCarro(self):
        if not self.ligada:
            return
        if self.velocidade > self.velocidadeMin:
            self.velocidade = 0
        else:
            print (f'Carro está na velocidade {self.velocidade}km, não tem como aumentar')

 
carroBeth = Carro() #objeto
carroJeff = Carro() #objeto

#Imprimindo dados iniciais dos carros
print(f'Carro da Beth: {carroBeth}')
print(f'Carro do Jeff: {carroJeff}')

#Ligando o carro
carroBeth.ligarCarro()
print(f'Agora o carro da Beth está ligado? {carroBeth.ligada}')

#Aumenta a velocidade em 2x
for _ in range(10):
    carroBeth.aumentarVelocidade()
print(f'Carro da Beth: {carroBeth}')
print(f'Carro do Jeff: {carroJeff}\n')

#diminui a velocidade em 1x
for _ in range(1):
    carroBeth.diminuirVelocidade()
print(f'Carro da Beth: {carroBeth}')
print(f'Carro do Jeff: {carroJeff}\n')

#Para o carro, ou seja, coloca na velocidade 0km
carroBeth.pararCarro()
print(f'Carro da Beth: {carroBeth}')
print(f'Carro do Jeff: {carroJeff}\n')

#tenta diminuir a velocidade mesmo o carro estando em 0km. Chegando aqui o carro vai estar com 0km e vai imprimir uma msg de alerta.
carroBeth.diminuirVelocidade()

#aumenta novamente a velocidade em 3x
for _ in range(3):
    carroBeth.aumentarVelocidade()
print(f'Carro da Beth: {carroBeth}')
print(f'Carro do Jeff: {carroJeff}\n')