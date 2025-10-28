funcionario = []

while True:
    print("\nMENU".center(15))
    print("1 - Cadastrar funcionario")
    print("2 - Visualizar todos os funcionarios")
    print("3 - Buscar por nome")
    print("4 - Calcular media salarial")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        print("\nCadastrar funcionario")
        continuar = "S"
        while continuar == "S": 
            nome = input("Digite o nome do funcionario:").upper()
            salario = float(input("Digite o salário do funcionario(não use vírgula):"))
            funcionario.append([nome, salario])
            continuar = input("Deseja adicionar outro funcionario(S/N): ").upper()
            if continuar == "N":
                break

    elif opcao == 2:
        print("\nVisualizar todos os funcionarios:")
        if not funcionario:
            print("Nenhum funcionario foi cadastrado!")
        else:
            for f in funcionario:
                print(f"Nome: {f[0]}, Salário: {f[1]}")

    elif opcao == 3:
        print("\nBuscar por nome:")
        nome_busca = input("Digite o nome do funcionario:").upper()
        encontrado = False
        for f in funcionario:
            if f[0] == nome_busca:
                print(f"Nome: {f[0]}, Salário: {f[1]}")
                encontrado = True
                break
        if not encontrado:
            print("Funcionario não encontrado!")

    elif opcao == 4:
        print("\nCalcular média salarial:")
        if not funcionario:
            print("Nenhum funcionario foi cadastrado!")
        else:
            total_salario = sum(f[1] for f in funcionario)
            media_salarial = total_salario / len(funcionario)
            print(f"Média salarial dos funcionarios: {media_salarial:.2f}")

    elif opcao == 5:
        print("\nSair")
        break
    else:
        print("Opção inválida. Tente novamente.")
