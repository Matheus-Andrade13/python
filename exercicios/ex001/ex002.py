preco = float(input('Digite o valor do produto: '))
percentual = float(input('Digite o percentual de desconto: '))

desconto = preco * (percentual / 100)
final = preco - desconto


print(f'Valor do produto: {preco}. Com um percentual de desconto de: {percentual}%')

print(f'O valor calculado de desconto foi de: {desconto}. O valor final do produto é de: {final}')