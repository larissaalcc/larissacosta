import mysql.connector

    

meubanco = mysql.connector.connect(
host="10.28.1.198",
user="suporte",
password="suporte",
database="sistema_cadastro"
)

meucursor = meubanco.cursor()

# Operações CRUD

# CREATE
def create_data(id,nome,cpf,email,telefone,endereco):
    sql = "INSERT INTO cadastro ( nome, cpf, email, telefone, endereco) VALUES ({self.inputnome},{self.inputcpf},{self.inputemail},{self.inputtelefone},{self.inputendereco})"
    val = (id,nome,cpf,email,telefone,endereco)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro efetuado !")

# READ
def read_data():
    meucursor.execute("SELECT * FROM cadastro")
    myresult = meucursor.fetchall()
    for x in myresult:
        print(x)

# UPDATE
def update_data_nome(id,nome,cpf,email,telefone,endereco):
    sql = "UPDATE cadastro SET nome = %s, cpf = %s, email = %s telefone = %s, endereco = %s WHERE id = %s "
    val = ( id, nome,cpf,email,telefone,endereco)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro atualizado.")
    
def update_data_cpf(nome,cpf,email,telefone,endereco):
    sql = "UPDATE cadastro SET  nome = %s, cpf = %s, email = %s telefone = %s, endereco = %s WHERE cpf = %s "
    val = ( nome,cpf,email,telefone,endereco,cpf)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro atualizado.")
    
def update_data_email( nome,cpf,email,telefone,endereco):
    sql = "UPDATE cadastro SET nome = %s, cpf = %s, email = %s telefone = %s, endereco = %s WHERE email = %s "
    val = ( nome,cpf,email,telefone,endereco)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro atualizado.")

def update_data_telefone(nome,cpf,email,telefone,endereco):
    sql = "UPDATE cadastro SET nome = %s, cpf = %s, email = %s telefone = %s, endereco = %s WHERE telefone = %s "
    val = ( nome,cpf,email,telefone,endereco)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro atualizado.")
    
def update_data_endereco( nome,cpf,email,telefone,endereco):
    sql = "UPDATE cadastro SET nome = %s, cpf = %s, email = %s telefone = %s, endereco = %s WHERE endereco = %s "
    val = ( nome,cpf,email,telefone,endereco)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro atualizado.")
    
# DELETE
def delete_data(id, nome):
    sql = "DELETE FROM cadastro WHERE id = %s"
    val = (id,nome)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "Cadastro excluido")



meubanco.close()

