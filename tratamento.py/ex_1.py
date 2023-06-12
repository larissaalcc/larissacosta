print("¨¨"*59)
lista_cliente=[]
lista_passagem=[]
lista_aviao=[]
lista_tripulacao=[]
c=0
while True:
    try:
        menu= int(input(" \nDigite:\n 1 Para Cadastro do cliente\n 2 Para Cadastro de passagem\n 3 Para Cadastro do avião\n 4 Para Cadastro da tripulação\n 5 Para Imprimir\n 6 Para sair\n Sua opção:"))
    except ValueError:
        print("Digito inválido.Tente novamente")
    if menu == 1:
        print("---- BEM VINDO AO CADASTRO DE CLIENTES----")
        while True:
                nome=str(input("\nNome do cliente: "))
                if nome.isalpha() == True:
                    print("Nome Válido")
                elif nome.isalpha() == False:
                    print("NOME INVÁLIDO")
                sobrenome=str(input("\nSobrenome: "))
                if sobrenome.isalpha()== True:
                    print("Sobrenome Válido")
                elif sobrenome.isalpha()== False:
                    print("Sobrenome Inválido")
                    continue
                try:
                        rg=int(input("\nRg:"))
                        cpf=int(input("\nCpf:"))
                        fone=int(input("\nTelefone para contato: "))
                        idade=int(input("\nIdade: "))
                        
                except :
                    print("Por favor, digite apenas números. Tente novamente")
                    break
    if menu == 2:
        print("----BEM VINDO AO CADASTRO DE PASSAGENS----")
    destino=str(input("\nSeu destino: "))
    if destino.isalpha()== True:
        print("Destino válido")
    elif destino.isalpha()== False:
        print("Destino Desconhecido. Insira uma origem válida")
        continue
    origem=str(input("\nSua origem: "))
    if origem.isalpha()== True:
        print("Destino Válido")
    elif origem.isalpha()== False:
        print("Destino Desconhecido. Insira um destino válido")
        continue
    try:
        dias=int(input("\nDuração em dias:"))
        valor=float(input("\nValor da passagem: "))
        desconto=(5/100*valor)
        print("\nDesconto 5%:{:.2f}".format(desconto))
        total=(valor-desconto)
        print("Total da viagem= R$",total)
    except:
        print("Por favor, digite apenas números. Tente novamente")
        lista_passagem.append(destino)
        lista_passagem.append(origem)
        lista_passagem.append(dias)
        lista_passagem.append(valor)
        lista_passagem.append(desconto)
        lista_passagem.append(total)
        continue
    if menu == 3:
        print("----BEM VINDO AO CADASTRO DO AVIÃO----")
    try:
        modelo=int(input("\nModelo da Aeronave: "))
        ano=int(input("\nAno de fabricação: "))
        horas=int(input("\nHoras de voo: "))
        cor=str(input("\nCor da Aeronave: "))
        passageiros=int(input("\nQuantidade de passageiros:"))
    except:
        print("Por favor, digite apenas números. Tente novamente")
        continue
    lista_aviao.append(modelo)
    lista_aviao.append(ano)
    lista_aviao.append(horas)
    lista_aviao.append(cor)
    lista_aviao.append(passageiros)
    continue
if menu == 4:
        print("----BEM VINDO AO CADASTRO DA TRIPULAÇÃO---")
try:
    nome=str(input("\nNome: "))
    cargo=str(input("\nDescrição do cargo: "))
except:   
    print("Digite apenas letras")
try:
    idadeTripulacao=int(input("\nIdade: "))
    admissao=int(input("\nAno de Admissão: "))
    contato=int(input("\nFone para contato: "))
except:
                print("Por favor, digite apenas números. Tente novamente")
tripulacao1=[nome,cargo,idadeTripulacao,admissao,contato]
for i in tripulacao1:
                lista_tripulacao.append(i)
                continue
if menu == 5:
                clienteP=["Nome:","Sobrenome:","Rg:","Cpf:","Telefone:","Idade:"]
                passagem=["Destino:","Origem:","Dias","Valor","Desconto:","Total:"]
                aviao=["Modelo:","Ano:","Horas","Cor","Passageiros:"]
                tripulacao=["Nome:","Descrição do cargo:","Idade:","Data de admissão:","Telefone para contato:"]
                print("\nRELATÓRIO CLIENTE")
                c=0
if len(lista_cliente)>0:
                for pergunta in clienteP:
                
                    print(pergunta,lista_cliente[c])
                    c+=1
c=0
print("-"*100)
print("PASSAGEM")
if len(lista_passagem)>0:
                for pergunta in passagem:
                    print(pergunta,lista_passagem[c])
                    c+=1
c=0
print("-"*100)
print("AERONAVE")
if len(lista_aviao)>0:
    for pergunta in aviao:
        print(pergunta,lista_aviao[c])
        c+=1
c=0
print("-"*100)
print("TRIPULAÇÃO")
if len(lista_tripulacao)>0:
    for pergunta in tripulacao:
        print(pergunta,lista_tripulacao[c])
        c+=1
c=0