l1 = int(input('Qual o tamanho do 1o lado? '))
l2 = int(input('Qual o tamanho do 2o lado? '))
l3 = int(input('Qual o tamanho do 3o lado? '))

if(l1 > 0 and l2 > 0 and l3 > 0 and l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1):
    if(l1 == l2 and l1 == l3 and l2 == l3):
        print('Triangulo Equilátero')
    elif(l1 != l2 and l1 != l3 and l2 != l3):
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isósceles')
else:
    print('Os valores indicados não formam um Triangulo!')