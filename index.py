from prettytable import PrettyTable
table = PrettyTable()
funcionario = []

def cadastrar_funcionario():
    print("\nCadastrar funcionario")
    continuar = "S"
    while continuar == "S": 
        nome = str(input("Digite o nome do funcionario:")).upper()
        idade = int(input("Digite a idade do funcionario:"))
        cargo = str(input("Digite o cargo do funcionario:")).upper()
        salario = int(input("Digite o salário do funcionario(não use vírgula):"))
        funcionario.append([nome, idade, cargo, salario])
        continuar = input("Deseja adicionar outro funcionario(S/N): ").upper()
        if continuar == "N":
            break

def visualizar_funcionarios():
    print("\nVisualizar todos os funcionarios:")
    if not funcionario:
        print("Nenhum funcionario foi cadastrado!")
    else:
        table.clear()
        table.field_names = ["Nome", "Idade", "Cargo", "Salário"]
        for f in funcionario:
            table.add_row(f)
        print(table)

def buscar_funcionario():
    print("\nBuscar por nome:")
    nome_busca = input("Digite o nome do funcionario:").upper()
    encontrado = False
    for f in funcionario:
        if f[0] == nome_busca:
            print(f"Nome: {f[0]}, Idade: {f[1]}, Cargo: {f[2]}, Salário: {f[3]}")
            encontrado = True
            break
    if not encontrado:
        print("Funcionario não encontrado!")

def _media_salarial():
    print("\nCalcular média salarial:")
    if not funcionario:
        print("Nenhum funcionario foi cadastrado!")
    else:
        total_salario = sum(f[3] for f in funcionario)
        media_salarial = total_salario / len(funcionario)
        print(f"Média salarial dos funcionarios: {media_salarial:.2f}")

def sair():
    print("\nSair")
    exit()

while True:
    print("\nMENU".center(15))
    print("1 - Cadastrar funcionario")
    print("2 - Visualizar todos os funcionarios")
    print("3 - Buscar por nome")
    print("4 - Calcular media salarial")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        cadastrar_funcionario()
    elif opcao == 2:
        visualizar_funcionarios()
    elif opcao == 3:
        buscar_funcionario()
    elif opcao == 4:
        _media_salarial()
    elif opcao == 5:
        sair()
    else:
        print("Opção inválida. Tente novamente.")