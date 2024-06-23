print("Bem vindos ao Sistema de Gerenciamento de Funcionários da Empresa X!")

lista_funcionarios = []
id_global = 1  # Substitua com seu número de RU

def cadastrar_funcionario(id):
  nome = input("Digite o nome do funcionário: ")
  setor = input("Digite o setor do funcionário: ")
  salario = float(input("Digite o salário do funcionário: "))

  funcionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}
  lista_funcionarios.append(funcionario.copy())  # Copia o dicionário para evitar modificações na variável original

  print(f"Funcionário {nome} cadastrado com sucesso!")

def consultar_funcionarios():
  while True:
    opcao = int(input("""
    Menu de Consulta:

    1. Consultar Todos
    2. Consultar por Id
    3. Consultar por Setor
    4. Retornar ao Menu

    Opção: """))

    if opcao == 1:
      # Consultar Todos
      if not lista_funcionarios:
        print("Não há funcionários cadastrados.")
      else:
        for funcionario in lista_funcionarios:
          print(f"""
          Funcionário: {funcionario['nome']}
          Id: {funcionario['id']}
          Setor: {funcionario['setor']}
          Salário: R$ {funcionario['salario']:.2f}
          """)

    elif opcao == 2:
      # Consultar por Id
      id_busca = int(input("Digite o ID do funcionário: "))
      funcionario_encontrado = None
      for funcionario in lista_funcionarios:
        if funcionario['id'] == id_busca:
          funcionario_encontrado = funcionario
          break

      if funcionario_encontrado:
        print(f"""
        Funcionário: {funcionario_encontrado['nome']}
        Id: {funcionario_encontrado['id']}
        Setor: {funcionario_encontrado['setor']}
        Salário: R$ {funcionario_encontrado['salario']:.2f}
        """)
      else:
        print("Funcionário com o ID informado não encontrado.")

    elif opcao == 3:
      # Consultar por Setor
      setor_busca = input("Digite o setor do funcionário: ")
      funcionarios_setor = []
      for funcionario in lista_funcionarios:
        if funcionario['setor'].lower() == setor_busca.lower():
          funcionarios_setor.append(funcionario)

      if funcionarios_setor:
        print(f"Funcionários do setor {setor_busca}:")
        for funcionario in funcionarios_setor:
          print(f"- {funcionario['nome']}")
      else:
        print(f"Não há funcionários cadastrados no setor {setor_busca}.")

    elif opcao == 4:
      # Retornar ao Menu
      return

    else:
      print("Opção inválida. Tente novamente.")


def remover_funcionario():
  while True:
    id_remocao = int(input("Digite o ID do funcionário a ser removido: "))
    funcionario_encontrado = None
    for funcionario in lista_funcionarios:
      if funcionario['id'] == id_remocao:
        funcionario_encontrado = funcionario
        break

    if funcionario_encontrado:
      lista_funcionarios.remove(funcionario_encontrado)
      print(f"Funcionário {funcionario_encontrado['nome']} removido com sucesso!")
      return
    else:
      print("Funcionário com o ID informado não encontrado.")
