class Pessoa():
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cidade=cidade
        self.estado=estado

    def relatorio(self):
        print("Nome: ")
        print("Idade: ")
        print("Endereço: ")
        print("Cidade: ")
        print("Estado: ")

class aluno(Pessoa):
    def __init__(self,mensalidade,nome,idade,endereco,cidade,estado):
        super().__init__(self,mensalidade,nome,idade,endereco,cidade,estado)
        self.mensalidade=mensalidade
        print("-------------------")
        print("SEJA BEM-VINDO ALUNO!")
        super().relatorio()
        print("Mensalidade:",self.mensalidade)

