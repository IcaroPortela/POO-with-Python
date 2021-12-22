def leiainteiro(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mErro: por favor, digite um numero válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mNão foi inserido nenhum valor.\n digite novamente!\033[m')
            return 0
        else:
            return x

def linha(tam = 42):
    return '_' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu')
    c=1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opicao = leiainteiro('\033[34mDigite a opção: \033[m')
    return opicao