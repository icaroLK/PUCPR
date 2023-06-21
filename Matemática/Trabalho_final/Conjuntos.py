def conjuntos():
    A = set(input("\033[35mDigite os elementos do conjunto A separados por espaço: \033[0m").split())
    B = set(input("\033[35mDigite os elementos do conjunto B separados por espaço:\033[0m ").split())

    while True:
        
        print("\033[33m\nEscolha uma opção:")
        print("1. Verificar se A é subconjunto próprio de B")
        print("2. Realizar operação de União")
        print("3. Calcular intersecção")
        print("4. Calcular diferença")
        print("5. Sair\033[0m")

        opcao = int(input("\033[33m\nOpção:\033[0m "))


        if opcao == 1: 
            if A < B:
                print("\033[32mA é um subconjunto próprio de B.\033[0m")
            else:
                print("\033[32mA não é um subconjunto próprio de B.\033[0m")
        
        elif opcao == 2:
            print(f"\033[32mA união de A e B é:{A | B}\033[0m") 
        
        elif opcao == 3:
            print(f"\033[32mA intersecção de A e B é:{A & B}\033[0m") 
        
        elif opcao == 4:
            print(f"\033[32mA diferença de A e B é: {A - B}\033[0m")  
        
        elif opcao == 5:
            break
        
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[0m")