print('Frutaria')
print('')
print('1 - Laranja 5,00')
print('2 - Maçã 9,00')
print('3 - Banana 4,00')

produto = int(input('Qual o produto deseja comprar? '))
qnt = int(input('Quantidade: '))

match (produto):
    case 1:
        pagar = qnt * 5.00
        print(f'Produto escolhido foi Laranja. Quantidade: {qnt}x  Total:{pagar}')
    case 2:
        pagar = qnt * 9.00
        print(f'Produto escolhido foi Maçã. Quantidade: {qnt}x  Total:{pagar}')
    case 3:
        pagar = qnt * 4.00
        print(f'Produto escolhido foi Banana. Quantidade: {qnt}x  Total:{pagar}')
    case _:
        print('Produto não identificado!')