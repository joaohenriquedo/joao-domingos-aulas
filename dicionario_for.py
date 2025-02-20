vendas_tecnologia = {"iphone":100,"samsung":300,"ps5":400} 
vendas_tecnologia2 = {"iphone":100,"samsung":300,"ps5":400} 
for chave in vendas_tecnologia:
    print(chave)
# usando o format
vendas_tecnologia = {"iphone":100,"samsung":300,"ps5":400} 
vendas_tecnologia2 = {"iphone":100,"samsung":300,"ps5":400} 
for chave in vendas_tecnologia:
    print("o produto {} vendeu {} unidades".format(chave,vendas_tecnologia2[chave]))
    #items
    vendas = {"notebook":200, "iphone":150}
for item in vendas.items():
    print(item)
#upanking
    vendas = {"notebook":200, "iphone":150}
for produtos, vendas in vendas.items():
    print("{}: {} de uunidades".format(produtos,vendas))

