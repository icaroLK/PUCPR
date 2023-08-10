def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[1;31mERRO! O usuário decidiu interromper o programa.\033[m')
            return 0
        else:
            return n


def leiaFloat(num):
    while True:
        try:
            r1 = input(num).replace(',', '.')
            r = float(r1)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número decimal.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mERRO! O usuário decidiu interromper o programa.\033[m')
            return 0
        else:
            return r