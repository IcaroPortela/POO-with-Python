class Animal():
    def __init__(self,nome,especie, age):
        self.nome = nome
        self.especie = especie
        self.age = age
    
    def Ruido(self):
        print("Rugido!")

ani = Animal("Alex","Leão",0)
ani.age = 8
print(ani.nome," o ", ani.especie)
print('Ele tem ', ani.age)
ani.Ruido()

import datetime, json
class Data():
    def __init__(self, data):
        self.data = data
    
    def Exibir(self):
        data = datetime.datetime.now()
        print(data.strftime('%x'))
        
class Cliente():
    def __init__(self, client):
        self.client = client
        
    def MyClient(self):
        client = '{"nome": "Antônio", "idade": 35, "TipoCliente": "Premium"}'
        tipo = json.loads(client)
        print(tipo["nome"])
        print(tipo["idade"])
        print(tipo["TipoCliente"])
D1 = Data("hoje")
C1 = Cliente("Cliente1")
D1.Exibir()
C1.MyClient()
