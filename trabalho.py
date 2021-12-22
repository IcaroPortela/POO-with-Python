print('='*30)
print('{:^30}'.format('BANCO GRAU TEC'))
print('='*30)
  
valor = int(input('Digite o valor para saque: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        
        totalced = 0
        if total == 0:
            break
print('='*30)
print('Saque Finalizado! Volte sempre ao Banco GRAU TEC')