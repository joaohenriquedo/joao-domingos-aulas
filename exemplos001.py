lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [11,12,13,14,15]
todas_listas = [lista1,lista2,lista3]
print(todas_listas)

produtos = ["tv", "celular", "mouse" , "teclado" , "tablet "]
print(produtos[1])

produtos = ["tv","celular","mouse","teclado","tablet "]
vendas = [  1000,  1500,      350,    270,     900]
print(produtos[1])
print("as vendas de {} foram de: {}".format(produtos[1],vendas[1]))

#i = nome_da_lista.index("o_que_voce_procura")

produtos = ["tv","celular","mouse","teclado","tablet "]
i = produtos.index("mouse")
print("o valor de i é: "+ str(produtos[i]))

produtos = ["tv","celular","mouse","teclado","tablet "]
estoque = [100,150,100,120,70,130,80]

produto = input("insira o produto em letra minuscula")
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print("temos {} unidades de {} no estoque".format(qtde_estoque,produto))
else:
     print("{} não existe no estoque".format(produto))


