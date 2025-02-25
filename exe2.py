produtos = ()
add_pro = list(produtos)
for i in range(10):
    produto = input("digite o nome do produto:")
    add_pro.append(produto)
    produtos = tuple(add_pro)
print(produtos)
nome = input("digite um nome de produto")
if nome in produtos:
    for i in range(len(produtos)):
        if produtos[i] == nome:
            print(i)
else:
    print("o produto não foi adicionado")
num = int(input("insira um numero entre 0 e 9"))
print(produtos[num])