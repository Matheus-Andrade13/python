print('Bem-Vindo a Frutaria!')
print('Produto 1: Maça')
print('Produto 2: Laranja')
print('Produto 3: Banana')

produto = int(input('Qual é o produto? '))
qnt = int(input('Qual é a quantidade? '))

if(produto == 1):
    pagar = qnt * 2.3
    print(f'Produto escolhido foi Maça. quantidade: {qnt}. Valor: {pagar}')
else: 
    if(produto == 2):
        pagar = qnt * 3.6
        print(f'Produto escolhido foi Laranja. quantidade: {qnt}. Valor: {pagar}')
    else:
        if(produto == 3):
            pagar = qnt * 6
            print(f'Produto escolhido foi Banana. quantidade: {qnt}. Valor: {pagar}')
        else:
            (produto > 3)
            print('Produto inesxistente!')

