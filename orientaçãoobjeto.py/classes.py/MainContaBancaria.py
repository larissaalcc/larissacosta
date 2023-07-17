from Conta_bancaria import*



while True:
    escolha=int(input("\n>>Bem vindo a sua Conta Bancária\n>>Para prosseguir selecione a operação que deseja efetuar!\n1.Cadastro\n2.Saque\n3.Depósito\n4.Ver extrato\nOu 0 para encerrar\nDigite aqui: "))

    if escolha==0:
        break

    elif escolha==1:
        
        print("\nVamos fazer seu cadastro!")
        nome=input("Nome Completo: ")
        cpf=input("Cpf: ")
        senha=int(input("Digite sua senha: "))
        banco=Conta_bancaria(nome,cpf,senha)
        print("Cadastro realizado com sucesso!")
        
    elif escolha==2:
        print("\nBem vindo ao saque:")
        s=int(input("Digite sua senha: "))
        banco.sacar(s)
        
        

    elif escolha==3:
        print("\nBem vindo ao depósito!")
        d=float(input("Quanto você deseja depositar: "))
        banco.depositar(d)
        

    elif escolha==4:
        print("Vamos consultar seu extrato!")
        s=int(input("Digite sua senha: "))
        extrato=banco.extrato(s)
        for a in extrato:
           print()
           for b in a:
               print(b,end=' ')
        print("\n")
           
       
        
       



    