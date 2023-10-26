import mysql.connector

meubanco = mysql.connector.connect(
  host="10.28.1.198",
  user="suporte",
  password="suporte",
  database="projeto"
)

meucursor = meubanco.cursor()

# Operações CRUD

# CREATE
def create_data(name, age, email):
    sql = "INSERT INTO customers (name, age, email) VALUES (%s, %s, %s)"
    val = (name, age, email)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "registro(s) inserido(s).")

# READ
def read_data():
    meucursor.execute("SELECT * FROM customers")
    myresult = meucursor.fetchall()
    for x in myresult:
        print(x)

# UPDATE
def update_data(id, name, age, email):
    sql = "UPDATE customers SET name = %s, age = %s, email = %s WHERE id = %s"
    val = (name, age, email, id)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "registro(s) atualizado(s).")

# DELETE
def delete_data(id):
    sql = "DELETE FROM customers WHERE id = %s"
    val = (id,)
    meucursor.execute(sql, val)
    meubanco.commit()
    print(meucursor.rowcount, "registro(s) excluído(s).")


create_data("Larissa", 32, "mauricio1desouza@gmail.com")
create_data( "luiz", 30, "thiago.almeida@example.com")

meubanco.close()
,