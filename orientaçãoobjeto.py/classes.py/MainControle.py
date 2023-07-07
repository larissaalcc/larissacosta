from Controle_Remoto import*
cor_do_controle=input("Qual será a cor do contole?\n")
altura_do_controle=int(input("Qual será a altura do controle?\n"))
largura_do_controle=int(input("Qual será a largura do controle?\n"))
qntd_de_botoes_do_controle=int(input("Qual será a quantidade de botões do controle?\n"))

#print("\nCONTROLE REMOTO\nCor do controle:", cor_do_controle,"\nAltura do controle:",altura_do_controle,"\nLargura do controle:",largura_do_controle,"\nA quantidade de botões:",qntd_de_botoes_do_controle)
controle_remoto=Controle_Remoto(cor_do_controle,altura_do_controle,largura_do_controle,qntd_de_botoes_do_controle)
controle_remoto.Cores()
controle_remoto.Altura1()
controle_remoto.largura1()
controle_remoto.qntdd_De_Botoes_1()
