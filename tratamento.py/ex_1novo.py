print("¨¨"*59)
lista_Cliente=[]
lista_Passagem=[]
lista_Aviao=[]
lista_Tripulacao=[]
c=0
while True:
    try:
        menu=int(input("Digite\n 1 Para cadastro de cliente\n 2 Para cadastro de passagem\n 3 Para cadastro do avião\n 4 Para cadastro da tripulação\n Sua escolha:"))
    except ValueError:
        print("Digito inválido. Tente novamente")
        while True:
            if menu == 1:
                print("Bem vindo ao cadastro do cliente.\n Vamos lá\n")
            nome=(input("Nome do cliente: "))
            if nome.isalpha()==True:
                print("Nome válido")
            elif nome.isalpha()== False:
                print("Nome inválido. Tente novamente")
                continue
            while True:
                sobrenome=(input("\nSobrenome: "))
                if sobrenome.isalpha()==True:
                    print("Sobrenome válido")
                elif sobrenome.isalpha()==False:
                    print("Sobrenome inválido")
                    continue
                try:
                    rg=int(input("\nRg: "))
                    cpf=int(input("\nCpf: "))
                    fone=int(input("\nFone para contato: "))
                    idade=int(input("\nIdade: "))
                except ValueError:
                    print("Digite apenas números. Tente novamente")
                    continue




