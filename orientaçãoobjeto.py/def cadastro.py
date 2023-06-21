def cadastro():
    name=input("Insira seu nome:")
    age=int(input("Insira sua idade:"))
    return name,age
print("Iniciando cadastro...")
nome,idade= cadastro()
print("Cadastro realizado com sucesso")
print("Sr(a)",nome,"de",idade,"anos")