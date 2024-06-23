print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer botão para sair.')

x = float(input('Digite o 1o valor: '))
y = float(input('Digite o 2o valor: '))
op = input('Qual operação deseja realizar? ')

if (op == '+'):
    res = x + y
    print(f'Resultado: {x} + {y} = {res}')
elif(op == '-'):
    res = x - y
    print(f'Resultado: {x} - {y} = {res}')
elif(op == '*'):
    res = x * y
    print(f'Resultado: {x} * {y} = {res}')
elif(op == '/'):
    res = x / y
    print(f'Resultado: {x} / {y} = {res}')
else:
    print('Encerrando o programa...')