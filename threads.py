#As Treads são processamentos de dados pelo processador onde esses processos são executados em paralelo.
#Podemos ter multiThreads como exemplos os processadores Intel I3, I5 , I7 e I9 que possuem essa capacidade de processamento paralelo simultâneo e sem consumir muita memória.

from threading import Thread
from time import sleep

class Menssagem:
    
    def funcao(self):
        for i in range(5):
            print(i, 'Vezes Executado')
            sleep(1)
            if i==3:
                break

m = Menssagem()
print('Iniciar')
Thread(target=m.funcao()).start()
sleep(2)
print('Fim do Thread')
