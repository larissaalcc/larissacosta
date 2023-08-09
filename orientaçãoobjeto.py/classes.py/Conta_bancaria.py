from datetime import datetime
historico=[]
h_filho=[]

class Conta_bancaria():

    def __init__(self,nome,cpf,senha):
        self.nome=nome
        self.__saldo=0.0
        self.__cpf=cpf
        self.__senha=senha

    def extrato(self,s):
        #self.__senha=s
        if s!=self.__senha:
            print("Senha inválida")
        else:
            return historico

    def depositar(self,x):
        tempo=datetime.now()
        data_e_hora_em_texto = tempo.strftime("%d/%m/%Y %H:%M")
        h_filho.append("Depósito:")
        h_filho.append(x)
        h_filho.append(data_e_hora_em_texto)
        historico.append(h_filho.copy())
        h_filho.clear()
        self.__saldo=self.__saldo+x
        print("\nDepósito efetuado com suceso")
        print("Seu saldo agora é:",self.__saldo)

 
    def sacar(self,s):

        if s!=self.__senha:
            print("Senha inválida")
        else:
            s1=float(input("Quanto você deseja sacar: "))
            tempo=datetime.now()
            data_e_hora_em_texto = tempo.strftime("%d/%m/%Y %H:%M")
            h_filho.append("Saque:")
            h_filho.append(s1)
            h_filho.append(data_e_hora_em_texto)
            historico.append(h_filho.copy())
            h_filho.clear()
            self.__saldo=self.__saldo-s1
            print("Seu saldo:",self.__saldo)




