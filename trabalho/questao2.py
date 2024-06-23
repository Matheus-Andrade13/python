#Questão 2

print(6*'-','Bem-vindo a Loja de Marmitas do Matheus Andrade',6*'-')
print(61*'-')
print(24*'-','Cardápio',27*'-')
print(61*'-')
print(2*'-','| Tamanho | Bife Acebolado(BA) |   Filé de Frango(FF) |',2*'-')
print(2*'-','|    P    |      R$ 16,00      |       R$ 15,00       |',2*'-')
print(2*'-','|    M    |      R$ 18,00      |       R$ 17,00       |',2*'-')
print(2*'-','|    G    |      R$ 22,00      |       R$ 21,00       |',2*'-')
print(61*'-')
print(61*'-')

valorTotal = 0

while True:

    #Lógica que usei para os inválidos
    sabor = input('Entre com o Sabor desejado (BA/FF): ')
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido. Tente novamente')
        print()
        continue
    else:
        tamanho = input('Entre com o Tamanho desejado (P/M/G): ')
        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            print('Tamanho inválido. Tente novamente')
            print()
            continue
                                  
    #Tamanhos e valores
    if sabor == 'BA' and tamanho == 'P':
        valor = 16.00
        valorTotal += valor 
        print('Você pediu um Bife Acebolado no Tamanho P: R$ 16,00')
    elif sabor == 'BA' and tamanho == 'M':
        valor = 18.00
        valorTotal += valor 
        print('Você pediu um Bife Acebolado no Tamanho M: R$ 18,00')
    elif sabor == 'BA' and tamanho == 'G':
        valor = 22.00
        valorTotal += valor 
        print('Você pediu um Bife Acebolado no Tamanho G: R$ 22,00')
    elif sabor == 'FF' and tamanho == 'P':
        valor = 15.00
        valorTotal += valor 
        print('Você pediu um Filé de Frango no Tamanho P: R$ 15,00')
    elif sabor == 'FF' and tamanho == 'M':
        valor = 17.00
        valorTotal += valor 
        print('Você pediu um Filé de Frango no Tamanho M: R$ 17,00')
    elif sabor == 'FF' and tamanho == 'G':
        valor = 21.00
        valorTotal += valor 
        print('Você pediu um Filé de Frango no Tamanho G: R$ 21,00')

    print()

    #Perguntar final e fim do laço
    maisPedido = input('Deseja pedir mais alguma coisa? (S/N): ')
    if maisPedido == 'S':
        continue
    elif maisPedido != 'S':
        print(f'O valor total a ser pago: R$ {valorTotal}0')
        break

