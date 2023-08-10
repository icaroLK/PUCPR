'''
modulo clientes
'''
import os

def menu():
    os.system("cls")
    msg = "   Sistema de Clientes   "
    print(len(msg) * "-")
    print(msg)
    print(len(msg) * "-")
    print('1. Cadastrar Cientes')
    print('2. Editar Clientes')
    print('3. Pesquisar Clientes')
    print('4. Remover Cliente')
    print('5. Listar Clientes')
    print('6. Voltar')
    print(len(msg) * "-")
    return int(input('O que deseja fazer? '))


def add(clientes: dict):
    name = str(input('Digite seu nome: '))
    cpf = str(input('Digite seu CPF: '))
    idade = int(input('Digite sua idade: '))
    if not(cpf in clientes):
        clientes[cpf] = {
            'nome': name,
            'idade': idade
            }
    else:
        print('\033[1;31mEsse CPF já foi cadastrado!\033[m')
        input('Tentar Novamente')
    return clientes[cpf]

'''
def edit(clientes: dict):


def find(clientes: dict):
'''

def delete(cliente: dict):
    listar(cliente)
    ans = input('CPF de quem deseja remover: ')
    cliente.pop(ans)


def listar(clientes: dict):
    for k, v in clientes.items():
        print(f'CLIENTE: {v["nome"]}, {v["idade"]} anos - CPF: {k}')
    input('Continuar: <enter>')


def start(x):
    while True:
        os.system('cls')
        opt = menu()
        if opt == 1:
            os.system('cls')
            add(x)
            pass
        elif opt == 2:
            os.system('cls')
            pass
        elif opt == 3:
            os.system('cls')
            pass
        elif opt == 4:
            os.system('cls')
            delete(x)
            pass
        elif opt == 5:
            os.system('cls')
            listar(x)
        elif opt == 6:
            return
        else:
            print('Opção Invalida!')
            print('*'*20)


if __name__ == '__main__':
    clientes = {
        "006.973.559-00": {
            "nome": "Maicris Fernandes",
            "idade": 46,
        }
    }
    start(clientes)

'''
Estrutura do cliente
    "cpf": {
        "nome": str,
        "idade": int,
        "cpf": str

    }
'''