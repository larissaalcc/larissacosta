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
#sql = "'INSERT INTO usuario VALUES (null,"+nome+cpf+fone+idade+email+cidade+estado+pais+estado_civil+");"

print(sql)