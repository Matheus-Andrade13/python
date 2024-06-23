x = int(input('Digite um número: '))

if (x % 2 == 0):
    print('O número digitado é par!')
else:
    print('O número digitado é impar!')

################################################

a = 10
b = 1
c = 1.55

res = a > b or not c == b and b != b + c / a
print(res)