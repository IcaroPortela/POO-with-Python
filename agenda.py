#Criando uma agenda com POO
class Agenda:
    nomes = []

    def Adcionar(self):
        x = int(input('Quantos nomes você deseja adicionar? '))
        for i in range(x):
            n = str(input('Digite o seu nome: '))
            self.nomes.append(n)

    def Remove(self):
        liste_nome = str(input('Informe o nome que deseja remover: '))
        if liste_nome in self.nomes:
            self.nomes.remove(liste_nome)
            print('Nome {} removido com sucesso!'.format(liste_nome))
            print(self.nomes)
        else:
            print("Nome {} não foi encontrado.".format(liste_nome))
            print(self.nomes)

    def Listar(self):
        print('Está é sua lista de nomes: ')
        for nome in self.nomes:
            print(f'{nome}')

    def Ordenar(self):
        print('Escolha a forma com quer ordenar:')
        print('''1. - Para ordenar de forma crescente 
            2.- Para ordenar de forma decrescente
        ''')
        op = int(input('Digite a opção: '))
        if op == 1:
            self.nomes.sort()
            for name in self.nomes:
                print(name)
        else:
            self.nomes.reverse()
            for name in self.nomes:
                print(name)
    
    def Pesquisar(self):
        achar = False
        pos = 0
        vetnomes = str(input('Informe o nome que você quer pesquisar: '))
        while(achar == False and pos < len(self.nomes)):
            if vetnomes == self.nomes[pos]:
                achar = True
                print(len(self.nomes[pos]))
            else:
                pos += 1
        if achar == True:
            print(f'O nome que você queriaa achar é esse {self.nomes[pos]}')
        else:
            print('O nome que você digitou não foi encontrado!')

    def Alterar(self):
        chnome = str(input('Informe o nome que você quer pesquisar: '))
        altnome = str(input('Digite o nome que quer alterar'))
        achar = False
        pos = 0
        while(achar == False and pos < len(self.nomes)):
            if chnome == self.nomes[pos]:
                achar = True
                self.nomes[pos] = altnome
            else:
                pos += 1
        if achar == True:
            print(f'O nome {chnome} foi alterado para {self.nomes[pos]}.')
        else:
            print(f'Não foi possivel alterar o nome {chnome}')

    def menu_op(self):
        op = 0
        menu = '''
                1. - Add new member
                2. - Remove a member
                3. - Show list
                4. - Order the list
                5. - Search the member
                6. - Alter the member
                7. - Exit
            '''
        while(True):
            print(menu)
            op = int(input('Digite a opção: '))
            if op == 1:
                self.Adcionar()
            elif op == 2:
                self.Remove()
            elif op == 3:
                self.Listar()
            elif op == 4:
                self.Ordenar()
            elif op == 5:
                self.Pesquisar()
            elif op == 6:
                self.Alterar()
            else:
                print('Obrigado por tudo, volte sempre!')
                break