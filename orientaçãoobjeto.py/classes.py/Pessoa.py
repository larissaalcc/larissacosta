class Pessoa():
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cidade=cidade
        self.estado=estado

    def relatorio(self):
        print("Nome: ",self.nome)
        print("Idade: ",self.idade)
        print("Endereço: ",self.endereco)
        print("Cidade: ",self.cidade)
        print("Estado: ",self.estado)

class Aluno(Pessoa):
    def __init__(self,mensalidade,nome,idade,endereco,cidade,estado):
        super().__init__(self,mensalidade,nome,idade,endereco,cidade,estado)
        self.mensalidade=mensalidade
        print("-------------------")
        print("SEJA BEM-VINDO ALUNO!")
        super().relatorio()
        print("Mensalidade:",self.mensalidade)

class Professor(Pessoa):
    def __init__(self,salario,nome,idade,endereco,cidade,estado):
        super().__init__(self,salario,nome,idade,endereco,cidade,estado)
        self.salario=salario
        print("--------------------")
        print("SEJA BEM VINDO PROFESSOR!")
        super().relatorio()
        print("Salario: ",self.salario)