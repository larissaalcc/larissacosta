def inverte(nome, sobrenome):
    nomeInverso= sobrenome+","+nome
    return nomeInverso
a= input("Nome:")
b= input("Sobrenome:")
invertido= inverte(a,b)
print("Olá",invertido)