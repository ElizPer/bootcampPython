'''
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
'''

listaContatos = {'Beth':'+55219000001', 'Vanessa': '+552190000002', 'Jefferson':'+552190000003', 'Thiago':'+552190000004'}

print('Insira o nome do contato para obter o número: ')
nome = input()

if(listaContatos.get(nome)):
    print(listaContatos.get(nome))
else:
    print('Contato inexistente, gostaria de adicionar, S-sim ou N-não?')
    novoContato = input()

    if(novoContato == 'S' or novoContato == 's'):
        #nomeNovo = input()
        listaContatos[nome] = input(f'Insira o número da {nome} com o código de discagem + DDD ')
        print('Lista de contato atualizada')
        print(listaContatos)
    else:
        print('Não quer adicionar, saindo da lista de contato')
