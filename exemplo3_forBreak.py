pessoas = ["john snow", "jesse pikman", "aria stark", "tyrion", "lanniister"]
#quero saber se uma pessoa especifica estA PRESENTE
chamada = "aria stark"
for pessoa in pessoas:
    if pessoa == chamada:
        print("{} esta presente".format(chamada))
        break
    else:
        print("print para mostrar que o for passou por essa pessoa:"+str(pessoa))

        pessoas = ["john snow", "jesse pikman", "aria stark", "tyrion", "lanniister"]
#quero saber se uma pessoa especifica estA PRESENTE
chamada = "aria stark"
for pessoa in pessoas:
    if pessoa == chamada:
        print("{} esta presente".format(chamada))
        break
    else:
        print("print para mostrar que o for passou por essa pessoa:"+str(pessoa))
        continue


        