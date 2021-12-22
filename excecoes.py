#Exceções são erro que são gerados por divergências de dados informados no código
#Tipos de exceções: NameError, ValueError, ZeroDivizionError, TypeError, etc...
#Exemplo:
try:
    a = int(input('Digite um número: '))
except Exception as erro:
    print(f'Não foi informado nenhum valor, por favor digite um número. {erro.__cause__} ')
except ValueError:
    print('Não encontrado valor, digite novamente.')
else:
    print(f'O valor é: {a}')
finally:
    print('Programa rodando com sucesso!')

#Usando exceções com POO 
import math
class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calcular(self):
        #x = (-self.b(math.sqrt(self.b**2 - (4 *self.a *self.c)))/ 2*self.a )
        #return print('O resultado é : ', x)
        x = self.a + self.b - self.c
        return print('o resultado é: ',x)

eq2g = A(5,4,10)
try:
    eq2g.calcular()
except Exception as erro:
    print(f'Não foi possível executar este calculo! {erro.__class__}')
else: 
    print('Equação realizada com sucesso!')
finally:
    print('Fim do processo! Volte sempre!')
