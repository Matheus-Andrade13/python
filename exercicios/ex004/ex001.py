print('LANCHONETE')
print('')
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - SAIR/SOMAR')
print('')

total = 0

while True: 
    i   = int(input ('Digite o Número do item: '))

    if (i == 1):
        qnt = int(input ('Digite a quantidade: '))
        total += qnt * 5.00
    elif (i == 2):
        qnt = int(input ('Digite a quantidade: '))
        total += qnt * 7.00
    elif (i == 3):
        qnt = int(input ('Digite a quantidade: '))
        total += qnt * 4.00
    elif (i == 4):
        qnt = int(input ('Digite a quantidade: '))
        total += qnt * 6.00
    elif (i == 5): 
        break
    else:
        print('Produto Inválido. Selecione outro.')

print(f'Total do pedido: {total}.')
        
    
