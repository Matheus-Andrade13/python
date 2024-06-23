def checagem_tipo(dado):
    match (dado):
        case str(dado):
            print('String')
        case int(dado):
            print('Inteiro')
        case float(dado):
            print('Flutuante')

dados = [2.5, 4, 'tlg', '3', 99, 'C']

for dado in dados:
    checagem_tipo(dado)