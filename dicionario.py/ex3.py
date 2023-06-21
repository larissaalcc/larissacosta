dicionario={}
while True:
    cpf=(input("Seu cpf ou 0 para imprimir: "))
    if cpf == "0":
        break
    nome=input("Digite seu nome: ")
    idade=(input("Sua idade: "))
    telefone=(input("Telefone para contato: "))
    dicionario[cpf]={"Nome: ":nome,"Idade: ":idade,"Telefone:":telefone}
print(dicionario)  