estoque = [1338,455,678,768,730,45,34,88,12,100,55,76,49]
produtos = ["coca cola", "pepsi", "guarana", 'skol', "brahma", "agua","del vale","red bull", "dolly", "fanta", "sprite", "sukita", "pepsi twist"]
minimo = 50
for i, qtde in enumerate(estoque) :
    if qtde < minimo:
        print(produtos[i],qtde)