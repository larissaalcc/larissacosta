listaCpf=[]
listaNome=[]
listaIdade=[]
listaTelefone=[]
while True:
    cpf=(input("Seu cpf ou 0 para imprimir: "))
    if cpf == "0":
        print(dicionario)
        break
    nome=input("Digite seu nome: ")
    idade=(input("Sua idade: "))
    telefone=(input("Telefone para contato: "))
    listaCpf.append(cpf)
    listaNome.append(nome)
    listaIdade.append(idade)
    listaTelefone.append(telefone)
    dicionario={"cpf",cpf,"Nome:",nome,"Idade:",idade,"Telefone:",telefone}
   