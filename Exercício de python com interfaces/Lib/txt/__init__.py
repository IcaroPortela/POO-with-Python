from Lib.Interface import cabecalho

def arqExiste(nome):
    try:
        file = open(nome, 'rt')
    except (FileNotFoundError):
        return False
    else:
        return True

def criararquivo(nome):
    try:
        file = open(nome, 'wt+')
        file.close()
    except:
        print('ERRO: Não foi possível criar um arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def listArquivo(nome):
    try:
        file = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabecalho('\033[32mPESSOAS CADASTRADAS\033[m')
        for linha in file:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
        #print(file.read())
    finally:
        file.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        file = open(arq, 'at')
    except:
        print('ERRO! não foi possível abrir o arquivo!')
    else:
        try:
            file.write(f'{nome}; {idade}\n')
        except:
            print('ERRO: Não foi possível escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            file.close()
        