import smtplib

#Configura o servidor e a porta
servidor_smtp  = 'smtp.exemplo.com'
porta_smtp = 587

#Inicia conexão segura com o servidor
servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
servidor.starttls()

#Fazer login
nome_de_usuario = 'seu_email@exemplo.com'
senha = 'sua_senha'
servidor.login(nome_de_usuario, senha)

#criar mensagem de email
email_origem = 'jkhkzhdkz'
email_destino = 'kkikjsflik'
mensagem = 'corpo do email' 
assunto = 'assunto'

#envia o email 
servidor.sendmail(email_origem, email_destino,
f'subject: {assunto}\n\n{mensagem}')

#fechar conexão
servidor.quit()