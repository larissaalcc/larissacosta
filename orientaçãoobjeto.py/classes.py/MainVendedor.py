from Vendedor import*
vendedor=input("Nome do vendedor: ")
valor=int(input("Valor das vendas:"))
vendasVendedor=Vendedor(vendedor,valor)
print("\nNome do vendedor:",vendasVendedor.nome)
print("Valor das vendas:",vendasVendedor.vendas)
vendasVendedor.bateu_meta(100)

