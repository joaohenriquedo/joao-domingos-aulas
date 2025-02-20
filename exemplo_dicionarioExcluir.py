lucro = {"janeiro":1000, "fevereiro":1500,"março":2000}
lucro2 ={"abril":3,"maio":7,"junho":10}
#deleta com o comando delete
del lucro2["abril"]
print(lucro2)
#adiciona
lucro_jun = lucro2.pop("junho")
print(lucro2)
print(lucro_jun)
#removendo todos os dados
lucro2.clear()
print(lucro2)