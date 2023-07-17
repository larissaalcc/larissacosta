from datetime import datetime
data=datetime.now()

print(data)

data_e_hora_em_texto = data.strftime("%d/%m/%Y %H:%M")
print(data_e_hora_em_texto)