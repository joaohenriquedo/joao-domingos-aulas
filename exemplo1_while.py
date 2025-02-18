venda = input("registre um produto, para cancelar o registro de um novo produto, basta apertar enter sem digitar nada")
vendas = []
#crie o programa
while venda != "":
    vendas.append(venda)
    venda = input("registre um produto, para cancelar o registro de um novo produto, basta apertar enetr sem digitar nada:")
print("registros finalizado. As vendas cadastradas foram:{}".format(vendas))