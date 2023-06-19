'''Uma função que necessite de três argumentos, e que forneça a soma desses argumentos'''
def soma(x,y,z):
    resultado= x+y+z
    return resultado
a=int(input("Primeiro número:"))
b=int(input("Segundo número:"))
c= int(input("Terceiro número:"))
result=soma(a,b,c)
print("Soma=",result)