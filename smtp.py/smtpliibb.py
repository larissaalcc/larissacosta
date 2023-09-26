
import smtplib
try:
    #definindo o servidor
    servidor = smtplib.SMTP('smtp.gmail.com', 587)

    #iniciando o servidor
    servidor.starttls()

    #logando
    servidor.login('estoquemedicohub@gmail.com', 'pifs imrb vvyo kdah')

    #montando o email
    
    remetente = 'estoquemedicohub@gmail.com'
    destinatarios = ['mauricio1desouza@gmail.com']
    conteudo = 'agora vai'

    #enviando o email
    servidor.sendmail(remetente, destinatarios, conteudo)
except Exception as error:
    print(f"Erro ao enviar o email --> {error}")
finally:
    #encerrando a conexao do servidor
    servidor.quit()