import clientes
import produtos
import vendas
import os

def menu():
    os.system('cls')
    msg = "   Sistema de Vendas   "
    print(len(msg) * "=")
    print(msg)
    print(len(msg) * "=")
    print('1. Modulo de Cientes')
    print('2. Modulo de Produtos')
    print('3. Modulo de Vendas')
    print('4. Sair')
    print(len(msg) * "=")
    print()
    return int(input('Digite sua opção: '))


def start(x):
    while True:
        os.system('cls')
        opt = menu()
        if opt == 1:
            clientes.start(x)
        elif opt == 2:
            produtos.menu()
        elif opt == 3:
            vendas.menu()
        elif opt == 4:
            return
        else:
            print('Opção Invalida!')
            print('*'*20)


if __name__ == '__main__':
    print('Obrigado pela preferência!')
    database = {
        "clientes": {},
        "produtos": {},
        "vendas": {}
        }
    start(database)