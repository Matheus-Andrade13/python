dias = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km foram percorridos? '))

preco = dias * 60 + km * 0.15

print(f'O valor do aluguel foi de: {preco}')