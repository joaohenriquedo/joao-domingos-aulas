mais_vendidos = {"tecnologia":"iphone","refirgeracao": "ar consul 1200 btu","livros":"o alquimista"}
vendas_tecnologia={"iphone":1500,"samsung galaxy":12000, "tv samsung":1000, "ps5":1430}
livro = mais_vendidos["livros"]
# uso de chaves para acessar o valor - retire comentario da linha abaixo para testar.print(mais_vendidos["geladeiras"])
#uso do get para acessar o valor
print(mais_vendidos.get("livros"))
print(mais_vendidos["livros"])
print("fim programa")