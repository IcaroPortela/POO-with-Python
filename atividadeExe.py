def leiaint(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31m Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return x

def leiafloat(msg2):
    while True:
        try:
            y = float(input(msg2))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número real.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31m Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return y        
num = leiaint('Digite um número: ')
num2 = leiafloat('Digite um número real: ')
print(f'O valor digitado real é {num2}, e o valor inteiro é {num}')