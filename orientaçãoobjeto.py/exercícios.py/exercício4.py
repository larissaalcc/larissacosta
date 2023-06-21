
def converter_horas(horas,minutos):
    if horas<12:
        print(horas,":",minutos,"A.M")
    elif horas>=12:
        horas=horas-12
        print(horas,":",minutos,"P.M")
while True:
    print("Converter Horas!!\nDigite a para encerrar!")
    hr=int(input("Hora:"))
    if hr == "a":
        break
    mnt=int(input("Minutos:"))
    converter_horas(hr,mnt)
    

    
