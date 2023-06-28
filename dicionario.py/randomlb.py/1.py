import random
print(random.random())
print(random.uniform(4,10))
print(random.randint(11,55))
cores=['verde','vermelho','azul']
print(random.choice(cores))

cartas_de_um_baralho=['zap','sete copas','espadilha','pica fumo']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho)