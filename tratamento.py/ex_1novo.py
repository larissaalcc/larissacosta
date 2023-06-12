print("¨¨"*59)

lista_Passagem=[]
lista_Aviao=[]
lista_Tripulacao=[]
lista_cliente=[]
c=0
while True:
    try:
        menu=int(input("Digite\n 1 Para cadastro de cliente\n 2 Para cadastro de passagem\n 3 Para cadastro do avião\n 4 Para cadastro da tripulação\n 5 Para imprimit\n 6 Para sair\n Sua escolha:"))
    except ValueError:
        print("Digito inválido. Tente novamente")
    else:
        if menu == 1:
                while True:
                    print("Bem vindo ao cadastro do cliente.\n Vamos lá\n")
                    nome=(input("Nome do cliente: "))
                    if nome.isalpha()==True:
                        print("Nome válido")
                    elif nome.isalpha()== False:
                        print("Nome inválido. Tente novamente")
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
                    else:
                        lista_cliente.append(nome)
                        lista_cliente.append(sobrenome)
                        lista_cliente.append(rg)
                        lista_cliente.append(cpf)
                        lista_cliente.append(fone)
                        lista_cliente.append(idade)
        if menu == 2:
            while True:
                print("Bem vindo ao cadastro de passagem\n")





