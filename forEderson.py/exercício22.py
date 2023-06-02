listaT=[]
listaM=[]
listaA=[]
soma=0
cont=0
print("\n")
print("="*127)
while True:
    t=input("Digite a temperatura em graus celcius: ")
    if t=='x' or t== 'X':
        break
    m=int(input("Digite o mês: "))
    a=int(input("Digite o ano: " ))
    cont=cont+1
    t=float(t)
    listaT.append(t)
    listaM.append(m)
    listaA.append(a)
    soma=soma+t
    media=soma/cont
if listaT!=0:
    print("A menor temperatura= ",min(listaT))
    mn=min(listaT)
    n=listaT.index(mn)
    print("No mês: ",listaM[n])
    print("No ano: ",listaA[n])
    print(" A maior temperatura= ",max(listaT))
    z=max(listaT)
    x=listaT.index(z)
    print("No mês: ",listaM[x])
    print("No ano: ",listaA[x])
    print(" A média das temperaturas= ",media)
