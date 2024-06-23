nome = input('Qual é o seu nome? ')
idade = int(input('Qual é sua idade? '))

if(nome == 'Matheus'):
    print('Bem-Vindo, Matheus!')
elif(idade < 18):
    print('Você não é o Matheus. você é de Menor!')
elif(idade > 100):
    print('Você não é o Matheus. Você não é Imortal!')