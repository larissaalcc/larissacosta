from Conta import*
while True:
    try:
        escolha= int(input("\nBem vindo à sua Conta Bancária, para iniciar, selecione a operação que deseja realizar:\n1.Cadastro\n2.Fazer depósito\n3.Saque\n4.Consultar saldo\ndigite: "))
    except ValueError:
        print("Digite apenas números, tente novamente!")
    if escolha>4:
        print("Opção inválida")
    if escolha==1:
        print("\nBem vindo ao sistema de cadastro ")
        try:
            agencia1=int(input("\nNúmero da agência: "))
            numero_conta1=int(input("Número da conta: "))
            nome1=(input("Nome completo: "))
            fone1=int(input("Telefone para contato: "))
            cpf1=int(input("CPF: "))
        except ValueError:
            print("Dígito inválido!")
        else:
            print("Dados cadastrados!")
            conta1=conta(agencia1,numero_conta1,nome1,fone1,cpf1)  
    if escolha==2:
        print("\nBem vindo ao depósito!")
        try:
            total=float(input("Valor do depósito: "))
        except ValueError:
            print("Digite apenas números")
        else:
            conta1.depositar(total)
    if escolha==3:
        print("\nBem vindo ao saque!")
        try:
            total=float(input("Valor do saque: "))
        except ValueError:
            print("Digite apenas números")
        else:
            conta1.sacar(total)
    if escolha==4:
            print("\nSeu saldo é de: ")
            conta1.extrato()
            
            
           



   
