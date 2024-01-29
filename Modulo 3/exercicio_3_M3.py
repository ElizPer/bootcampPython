'''
Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''

carrinhoCompras = {}
produtos = 'FIM'
totalProd = 0

while produtos:
    print('Digite o produto e o valor, para sair digitar "FIM": ')
    produtos = input()
    if(produtos == 'FIM' or produtos == 'fim'):
        break
    carrinhoCompras[produtos] = float(input('R$: '))
    print(carrinhoCompras)

for compras in carrinhoCompras.values():
    print(compras)
    totalProd = totalProd + compras

print(totalProd)