import Matrizes
import Funcoes_2
import Funcoes_exponelciais
import Conjuntos

def calculadora_final():
    while True:
        print("\033[33m\nEscolha uma opção:")
        print("1. Conjuntos")
        print("2. Função do 2º")
        print("3. Função Exponencial")
        print("4. Matrizes")
        print("5. Sair\033[0m")

        opcao = int(input("\033[33m\nOpção:\033[0m "))

        if opcao == 1:
            print(Conjuntos.conjuntos())
        elif opcao == 2:
            print(Funcoes_2.funcoes_2())
        elif opcao == 3:
            print(Funcoes_exponelciais.funcao_exponencial())
        elif opcao == 4:
            print(Matrizes.matrizes())
        elif opcao == 5:
            print("\033[32mObrigada, volte sempre!\033[0m")
            break 
        else:
            print("\033[31mOpção inválida, digite novamente\033[0m")

print(calculadora_final())

    