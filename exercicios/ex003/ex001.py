soma = 0
cont = 1
while (cont <= 5):
    x = float(input(f'Digite a {cont} nota: '))
    soma += x
    cont += 1
media = soma / 5
print(f'Nota final: {media}')
