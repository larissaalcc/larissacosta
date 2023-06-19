
def positivo(x):
    if (x)>0:
        print("O número digitado é positivo")    
    elif (x)==0:
        print("O número digitado é 0")
    elif(x)<0:
        print("O número digitado é negativo")  

while True:
    num= int(input("Insira um número: "))
    positivo(num)
   
