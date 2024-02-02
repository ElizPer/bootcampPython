'''
Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
'''
import getpass #a senha fica em branco ao digitar
import pwinput #a senha fica com asteriscos ao digitar

login = input('Login: ')
#senha = getpass.getpass(prompt='Senha: ', stream=None )
senha = pwinput.pwinput(prompt='Senha: ')
bol = True

while bol:
    if(login == 'admin' and senha == 'admin123'):
        print('Acesso concedido')
        bol = False
    else:
        print('Login ou senha inválidos, digite novamente')
        login = input('Login: ')
        #senha = getpass.getpass(prompt='Senha: ', stream=None )
        senha = pwinput.pwinput(prompt='Senha: ')   