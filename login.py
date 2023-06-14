# Cadastro de usuario

from os import system
import getpass
import stdiomask
from time import sleep

# Criando o menu

def menu():
    print('-' * 30)
    print('Bem vindos ao projeto')
    print('-' * 30)
    print('Sistema de Login')
    print('Escolha uma opção: \n[1] Cadastro de novo usuário\n[2] Fazer login\n[3] Sair do programa')
    opcao = int(input('Digite a opção desejada: '))
    return(opcao)


# Fazendo o login


def fazer_login():
    login = str(input('Usuário: '))
    senha = stdiomask.getpass(prompt='Senha: ', mask='*')
    print(senha)
    return(login,senha)

# Pesquisando usuários no arquivo txt


def pesquisa_usuario(login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for line in arquivo.read().splitlines():
                usuario_tmp = line.split(' ')
                usuarios.append((usuario_tmp[0], usuario_tmp[1]))
            print(usuarios)
            for usuario in usuarios:
                username = usuario[0]
                password = usuario[1]
                if login == username and senha == password:
                    return True
            return False
    except FileNotFoundError:
        return False


while True:
    opcao = menu()

    if opcao == 1:  # Cadastro de novo usuario
        login, senha = fazer_login()
        if len(senha) < 5:
            print('Sua senha deve ter pelo menos 5 dígitos.')
            senha = stdiomask.getpass(prompt='Senha: ', mask='*')
        user = pesquisa_usuario(login, senha)
        if user:
            print('Usuário já cadastrado. Tente novamente!')
            exit()
        else:
            with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
            print('Cadastro realizado com sucesso!')
            exit()

    elif opcao == 2:  # Fazer o login
        login, senha = fazer_login()
        user = pesquisa_usuario(login, senha)
        if user == True:
            print('Login realizado com sucesso!')
            exit()
        elif user == False:
            print('Login e/ou senha inválido. Tente novamente.')
            sleep(3)
            exit()
            
    elif opcao == 3:
        print('Volte sempre! Obrigada.')
        exit()
    else:
        print('\nEsta é uma opção inválida. Por favor, digite apenas as opções 1, 2 ou 3.\n')
        continue