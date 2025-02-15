pessoas = ["joão", "maria", "felipe", "augusto", "antonio"]
telefones =[136,444,887,999,532]
bairros =["iririu","floresta","pescador","aventureiro","palmerode"]
pessoa = input("insira o nome da pessoa em letra minuscula")
if pessoas in pessoa:
     i = pessoas.index(pessoa)
     e = bairros.index(bairros)
     p = telefones.index(telefones)
print("o nome é:{} seu telefone é:{} bairro:{} ".format(pessoas))

