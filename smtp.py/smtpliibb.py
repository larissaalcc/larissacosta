
import smtplib
try:
    #definindo o servidor
    servidor = smtplib.SMTP('smtp.gmail.com', 587)

    #iniciando o servidor
    servidor.starttls()

    #logando
    servidor.login('estoquemedicohub@gmail.com', 'wick dniz fslg huop')

    #montando o email
    remetente = 'estoquemedicohub@gmail.com'
    destinatarios = ['larissacgr05@gmail.com']
    conteudo = 'TOMA'

    #enviando o email
    servidor.sendmail(remetente, destinatarios, conteudo)
except Exception as error:
    print(f"Erro ao enviar o email --> {error}")
finally:
    #encerrando a conexao do servidor
    servidor.quit()