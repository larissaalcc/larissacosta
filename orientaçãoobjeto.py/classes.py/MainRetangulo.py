from Modelo_retangulo import *

while True:
    escolha=int(input("\nDigite\n1.Para informar os lados\n2.Para alterar valor dos lados e retornar valor\n3.Para Calcular a área e o perímetro\n0.Para sair\nSua escolha aqui:"))
    if escolha==0:
        break
    if escolha==1:
        lado1=int(input("Digite o lado :"))
        lado2=int(input("Digite o lado :"))
        ladoR=Modelo_retangulo(lado1,lado2)
        ladoR.calcular_area_e_perimetro(lado1,lado2)
    if escolha==2:
        a=int(input("Digite o novo valor:"))
        b=int(input("Digite o segundo novo valor:"))
        ladoR.mudar_valor_dos_lados(a,b)
    if escolha==3:
        ladoR.calcular_area_e_perimetro(a,b)
        break
