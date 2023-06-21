def SomaImposto(valor,imposto):
    SomaImposto=valor+valor*imposto/100
    return SomaImposto
custo=float(input("Informe o custo do produto:"))
porcentagemImposto=float(input("Pocentagem do Imposto: "))
print(SomaImposto(custo,porcentagemImposto))

