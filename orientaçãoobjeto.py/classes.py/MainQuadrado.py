from Modelo_quadrado import*

while True:

    escolha=int(input("\nSelecione\n1.Para mostrar área e 2.Para alterar valor ou 0 para encerrar: "))

    if escolha==0:
        break

    elif escolha==1:
        a=int(input("\nDigite o tamanho do lado: "))
        quadrado=Modelo_quadrado(a)

    elif escolha==2:
        x=int(input("Digite o novo valor:"))
        quadrado.mudar_valor_lado(x)
    