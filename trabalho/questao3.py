#Questão 3

def escolha_modelo():
    #Função do modelo
    while True:
        #Menu de modelos
        print('Bem-vindo a Fábrica de Camisetas do Matheus Andrade')
        print('Entre com o modelo desejado')
        print('MCS - Manga Curta Simples')
        print('MLS - Manga Longa Simples')
        print('MCE - Manga Curta com Estampa')
        print('MLE - Manga Longa com Estampa')
        modelo = input('>> ')
        #Lógica para verificar a entrada
        if modelo in ('MCS', 'MLS', 'MCE', 'MLE'):   
            if modelo == 'MCS':
                valorDoModelo = 1.80
            elif modelo == 'MLS':
                valorDoModelo = 2.10
            elif modelo == 'MCE':
                valorDoModelo = 2.90
            elif modelo == 'MLE':
                valorDoModelo = 3.20
            return valorDoModelo
        else:
            print('Opção inválida. Tente novamente.\n')

def num_camisetas():
    #Função da quantidade de camisetas
    while True:
        try:    #Lógica para saber o desconto sobre a quantidade
            numeroDeCamisetas = int(input('Entre com o número de camisetas: '))
            if numeroDeCamisetas > 20000:
                print('Não aceitamos tantas camisetas de uma vez.')
                print('Por favor, entre com o número de camisetas novamente.\n')
            else:
                if numeroDeCamisetas < 20:
                    desconto = 0
                elif numeroDeCamisetas >= 20 and numeroDeCamisetas < 200:
                    desconto = 5
                elif numeroDeCamisetas >= 200 and numeroDeCamisetas < 2000:
                    desconto = 7
                elif numeroDeCamisetas >= 2000 and numeroDeCamisetas < 20000:
                    desconto = 12  
                camisetasDesconto = numeroDeCamisetas * (1 - desconto / 100) 
                return camisetasDesconto         
        except ValueError:
                print('Não aceitamos dados não numéricos.')
                print('Por favor, entre com o número de camisetas novamente.\n')
                    
def tipo_frete():
    #Função do frete
    while True: 
        #Menu do fretes
        print('Escolha o tipo de frete:')
        print('1 - Frete por Transportadora - R$ 100.00')
        print('2 - Frete por Sedex - R$ 200.00')
        print('0 - Retirar pedido na Fábrica - R$ 0.00')
        frete = int(input('>> '))
        #Lógica para verificar a entrada
        if frete in (1, 2, 0):
            if frete == 1:
                valorFrete = 100.0
            elif frete == 2:
                valorFrete = 200.0               
            elif frete == 0:
                valorFrete = 0.00
            return valorFrete
        else:
            print('Opção inválida. Tente novamente.\n')   

#Código principal
valor = 0          
x = escolha_modelo() 
y = num_camisetas()
z = tipo_frete()

#Calculo da saída
valor = (x*y)+z 

print(f'Total: R$ {valor}0 (Modelo: {x} * Quantidade(Com desconto): {y} + Frete: {z})')