'''Exercicio do Modulo 6 de Bando de Dados'''

import sqlite3

conexao = sqlite3.connect('bancoExercicios_M6')
cursor = conexao.cursor()

#----------1) Criando tabela aluno
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#----------2) Inserindo alunos na tabela
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Elizabeth", 34, "Ciência Ambiental")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Jefferson", 34, "Ciência da Computação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Vanessa", 30, "Geográfia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Thiago", 34, "Ciência da Computação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Julio", 29, "Educação Física")')

#---------- 3) Consultas Básicas
#a)Selecionar todos os registros da tabela "alunos"
#dados = cursor.execute('SELECT * FROM alunos')

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>31')

#c) selecionar os alunos do curso de 'Ciência' em ordem alfábética.
#dados = cursor.execute('SELECT * FROM alunos WHERE curso LIKE "Ciência %" ORDER BY nome ')

#d) Contar o número total de alunos na tabela
#dados = cursor.execute('Select count(*) FROM alunos')


#----------4) AtualizaçãoeRemoção
#a)Atualize a idade de um aluno específico na tabela
#dados = cursor.execute('UPDATE alunos SET idade=30 WHERE nome="Julio"')  

#b) Remova um aluno pelo ID
#dados = cursor.execute('DELETE FROM alunos WHERE id=1')  

#______________________________________________________________

#----------5a)CriarumaTabelaeInserirDados
#dados = cursor.execute('CREATE TABLE clientes(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT)')

#----------5b) Inserindo dados
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Elizabeth", 34, 3000)')
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Vanessa", 30, 4000)')
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Thiago", 36, 5000)')
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Flavio", 32, 4500)')
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Julio", 29, 4000)')
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Rael", 4, 2000)')
#dados = cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES ("Sandra", 62, 500)')

#----------6) Consultas e Funções Agregadas
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

#b) Calcule o saldo médio dos clientes
#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')

#c) Encontre o cliente com o saldo máximo
#dados = cursor.execute('SELECT MAX(saldo) FROM clientes')
#dados = cursor.execute('SELECT MIN(saldo) FROM clientes')

#d) Conte quantos clientes têm saldo acima de 1000
#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

#----------7) Atualização e Remoção com Condições
#a)Atualize o saldo de um cliente específico
#dados = cursor.execute('UPDATE clientes SET saldo=1500 WHERE nome="Sandra"')

#b) Remova um cliente pelo seu ID
#dados = cursor.execute('DELETE FROM clientes WHERE id=3')

#----------8) Junção de Tabelas: clientes e compras (criar, inserir produto a um cliente e trazer o cliente produto e )
#dados = cursor.execute('CREATE TABLE compras(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER, produto VARCHAR(100), valor FLOAT, CONSTRAINT cliente_id FOREIGN KEY (id) REFERENCES clientes(id))')

#dados = cursor.execute('INSERT INTO compras(id, produto, valor, cliente_id) VALUES(null, "sabão", 16, 1) ')
#dados = cursor.execute('INSERT INTO compras(id, produto, valor, cliente_id) VALUES(null, "bolacha", 19.5, 3) ')

#----------8c) exibir nome do cliente, produto e valor de cada compra
dados = cursor.execute('SELECT * FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
#--------------IMPRESSÃO DOS DADOS--------------
for dadosAluno in dados:
    print(dadosAluno)

conexao.commit() #dando commit para alterações na tabela
conexao.close() #fechando a conexao