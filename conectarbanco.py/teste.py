import mysql.connector

mydb = mysql.connector.connect(
  host="10.28.1.198",
  user="suporte",
  password="suporte",
  database="projeto"
)

mycursor = mydb.cursor()

# Operações CRUD

# CREATE
def create_data(name, age, email):
    sql = "INSERT INTO customers (name, age, email) VALUES (%s, %s, %s)"
    val = (name, age, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro(s) inserido(s).")

# READ
def read_data():
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# UPDATE
def update_data(id, name, age, email):
    sql = "UPDATE customers SET name = %s, age = %s, email = %s WHERE id = %s"
    val = (name, age, email, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro(s) atualizado(s).")

# DELETE
def delete_data(id):
    sql = "DELETE FROM customers WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro(s) excluído(s).")


create_data("Larissa", 32, "mauricio1desouza@gmail.com")
create_data( "luiz", 30, "thiago.almeida@example.com")

mydb.close()
