#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.

pais = ("Brasil","Argentina","Alemanha","Italia")
print("paises diisponiveis:",pais)
escolha=input("escolha um pais")
if escolha in pais:
    indice = pais.index(escolha)
    print("o indice é:",indice)
else:
    print("pais invalido")
    print("joao henrique")
