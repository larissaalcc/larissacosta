def calcular_pagamento(qntd_hr, qntd_valor):
    horas= float(qntd_hr)
    valor=float(qntd_valor)
    if horas<= 40:
        salario=horas*valor
    else:
        h_extra=horas-40
        salario=40*valor+(h_extra+(1.5*valor))
        print(salario)
calcular_pagamento(46,49)
