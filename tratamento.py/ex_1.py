print("¨¨"*59)
lista_cliente=[]
lista_passagem=[]
lista_aviao=[]
lista_tripulacao=[]
while True:
    menu= int(input(" \nDigite:\n 1 Para Cadastro do cliente\n 2 Para Cadastro de passagem\n 3 Para Cadastro do avião\n 4 Para Cadastro da tripulação\n 5 Para Imprimir\n 6 Para sair\n Sua opção:"))
    if menu == 1:
        print("---- BEM VINDO AO CADASTRO DE CLIENTES----")
        while True:
            try:
                nome=str(input("\nNome do cliente: "))
                if nome.isalpha() == True:
                    print("Nome Válido")
                elif nome.isalpha() == False:
                    print("NOME INVÁLIDO")
                    continue
                sobrenome=str(input("\nSobrenome: "))
                rg=int(input("\nRg:"))
                cpf=int(input("\nCpf:"))
                fone=int(input("\nTelefone para contato: "))
                idade=int(input("\nIdade: "))
            except:
                print("Por favor, digite apenas números. Tente novamente")
            else:
                lista_cliente.append(nome,sobrenome,rg,cpf,fone,idade)
    if menu == 2:
        print("----BEM VINDO AO CADASTRO DE PASSAGENS----")
        
        try:
            destino=str(input("\nSeu destino: "))
            origem=str(input("\nSua origem: "))
            dias=int(input("\nDuração em dias:"))
            v=float(input("\nValor da passagem: "))
            d=(5/100*v)
            print("\nDesconto 5%:{:.2f}".format(d))
            t=(v-d)
            print("Total da viagem= R$",t)
        except:
            print("Por favor, digite apenas números. Tente novamente")
        else:
            lista_passagem.append(destino,origem,dias,v,d,t)
    if menu == 3:
        print("----BEM VINDO AO CADASTRO DO AVIÃO----")
        try:
           modelo=int(input("\nModelo da Aeronave: "))
           ano=int(input("\nAno de fabricação: "))
           horas=int(input("Horas de voo: "))
           cor=str(input("Cor da Aeronave: "))
           passageiros=int(input("Quantidade de passageiros:"))
        except:
            print("Por favor, digite apenas números. Tente novamente")
        else:
            lista_aviao.append(modelo,ano,horas,cor,passageiros)
    if menu == 4:
        print("----BEM VINDO AO CADASTRO DA TRIPULAÇÃO---")
        try:
            nome=str(input("\nNome: "))
            cargo=str(input("Descrição do cargo: "))
        except:   
            print("Digite apenas letras")
        try:
            idadeTripulacao=int(input("\nIdade: "))
            admissao=int(input("Data de Admissão: "))
            contato=int(input("Fone para contato: "))
        except:
            print("Por favor, digite apenas números. Tente novamente")
        else:
            lista_tripulacao.append(nome,cargo,idadeTripulacao,admissao,contato)
    if menu == 5:
        print("\nRELATÓRIOS")
        print(lista_cliente)
        print(lista_passagem)
        print(lista_aviao)
        print(lista_tripulacao)
    elif menu == 6:
        break

