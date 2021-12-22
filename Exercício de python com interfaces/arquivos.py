from Lib.Interface import *
from Lib.txt import *
from time import sleep

arq1 = 'cadastro.txt'
'''if arqExiste(arq1):
    print('Arquivo encontrado com Sucesso!')
else:
    print('Arquivo não encontrado!')
    criararquivo(arq)
'''
if not arqExiste(arq1):
    criararquivo(arq1)

while True:
    resposta = menu(['Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        #print('Opção 1')
        #Listar nomes cadastraddos
        listArquivo(arq1)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME:'))
        idade = leiainteiro('IDADE: ')
        cadastrar(arq1, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema...    Até logo!')
        break
    else:
        print('ERRO: Opção inválida! \n Digite uma opção válida!')
    sleep(2)