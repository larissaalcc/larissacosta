def valorPagamento(valor,dias):
    if dias==0:
        print("O valor da prestação é R$",valor)
    elif dias>0:
        valor=valor+(valor*0.03+dias*0.01)
        print("Valor da prestação é R$",valor)
    return valor


listaValores=[]
listaAtraso=[]    
print("Pagamentos!!")
while True:
    valor1=float(input("Informe o valor da prestação ou digite 0 para encerrar: ")) 
    if valor1==0:  
        break
    atraso=int(input("Dias de atraso: "))
    listaValores.append(valorPagamento(valor1,atraso))
    listaAtraso.append(atraso)
   
print("Valor total das prestações:",listaValores,"Dias de atraso:",listaAtraso)
    
