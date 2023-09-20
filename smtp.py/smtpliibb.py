import smtplib

#Configura o servidor e a porta
servidor_smtp  = 'smtp.gmail.com'
porta_smtp = 465

#Inicia conexão segura com o servidor
servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
servidor.starttls()

#Fazer login
nome_de_usuario = 'larissacgr05@gmail.com'
senha = 'sua_senha'
servidor.login(nome_de_usuario, senha)

#criar mensagem de email
email_origem = 'larissacgr05@gmail.com'
email_destino = 'luizguichimenes2002@gmail.com'
mensagem = 'corpo do email' 
assunto = 'assunto'

#envia o email 
servidor.sendmail(email_origem, email_destino, f'subject: {assunto}\n\n{mensagem}')

#fechar conexão
servidor.quit()

