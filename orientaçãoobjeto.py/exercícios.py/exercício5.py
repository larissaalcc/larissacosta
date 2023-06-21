def valorPagamento(valor,dias):
    if dias==0:
        print("O valor da prestação é R$",valor)
    elif dias>0:
        total=valor+(valor*0.03+dias*0.01)
        print("Valor da prestação é R$",total)
        return total

listaValores=[]
listaAtraso=[]    
print("Pagamentos!!")
valor1=float(input("Informe o valor da prestação: "))
atraso=int(input("Dias de atraso: "))
valorPagamento(valor1,atraso)
