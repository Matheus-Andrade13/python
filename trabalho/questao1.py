#Questão 1

print('Bem-vindo a Loja do Matheus Andrade')

#inputs do menu
valorDoPedido = float(input('Entre com o valor do pedido: '))
quantidadeParcelas = int(input('Entre com a quantidade de parcelas: '))

#Lógica e calculo dos juros
if quantidadeParcelas < 4:
    juros = (0/100)
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = (4/100)
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = (8/100)
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = (16/100)
else:
    juros = (32/100)

#calculando a saida do console pedida
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

print(f'O valor das Parcelas é de: R${valorDaParcela}')
print(f'O valor Total Parcelado é de: R${valorTotalParcelado}')