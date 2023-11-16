import mysql.connector

#CRUD em python

while True:
    meubanco = mysql.connector.connect(
    host="10.28.1.198",
    user="suporte",
    password="suporte",
    database="cadastro"
    )
    meucursor = meubanco.cursor()
    
    print ("\nBem vindo ao sistema de cadastro !\n")
    print ("Escolha:\n1 - Para cadastro\n2 - Para visualizar os cadastros ou\n3 - Para sair ")
    opcao = int(input("Digite aqui: "))
    
    if opcao == 3:
        break
    
    elif opcao == 1:
        
        nome = input("\nNome Completo: ")
        cpf = (input("\nCPF: "))
        fone = (input("\nTelefone para contato: "))
        idade = (input("\nIdade: "))
        email = input("\nEmail para contato: ")
        cidade = input("\nCidade: ")
        estado = input ("\nEstado: ")        
        pais = input("\nPaís: ")        
        estado_civil = input("\nEstado Civil: ")
        
        sql = "INSERT INTO usuario VALUES (null,"+"'"+nome+"','"+cpf+"','"+fone+"',"+idade+",'"+email+"','"+cidade+"','"+estado+"','"+pais+"','"+estado_civil+"');"

        
        print(sql)
        meucursor.execute(sql)
        meubanco.commit()
        print(meucursor.rowcount, "Cadastro concluído.")
        
    elif opcao == 2:
        
        meucursor.execute("SELECT * FROM usuario;")
        myresult = meucursor.fetchall()
        for x in myresult:
            print(x)
            
  
          
    meubanco.close()
        
