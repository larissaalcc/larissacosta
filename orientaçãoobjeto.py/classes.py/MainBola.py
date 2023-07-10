from Modelo_bola import*
while True:
    escolha=int(input("\nEscolha\n1.Modelar\n2.Alterar modelagem\n3.Mostrar cor\nSua escolha:"))
    if escolha==1:
        cor1=input("Cor do objeto: ")
        tamanho1=(input("Circunferência do objeto: "))
        material1=input("Material do objeto: ")
        modelagem=Modelo_bola(cor1,tamanho1,material1,)
        continue
    elif escolha==2:
        w=input("Cor do objeto: ")
        a=input("Circunferência do objeto: ")
        b=input("Material do objeto: ")
        modelagem.trocar_cor(w,a,b,)
        continue
    elif escolha==3:
        modelagem.mostrar_cor()
        break
