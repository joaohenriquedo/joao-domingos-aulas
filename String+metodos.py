#TRANSFORMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAISCULA
nome = "joão"
print(nome.capitalize(),"\n")

#TRANSFORMA AS LETRAS EM MINUSCULAS
nome = "JOÃO"
print(nome.casefold(),"\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING
nome = "joaohenrique@gmail.com"
print(nome.count("o"), "\n")

#RETORNA TRUE (VERDADEIRO) OU FALSE (FALSO) PARA UM TESTE SE A STRING TERMINA COM UMA STRING ESPECIFICA
nome = "joaohenrique@gmail.com"
print(nome.endswith ("gmail.com"), "\n")

#RETORNA A POSIÇÃO DO TERMO PROCURADO LEMBRE-SE COMEÇA DO ZERO
nome = "joaohenrique@gmail.com"
print(nome.find ("@"), "\n")

#VERIFICA SE O TEXTO É TODO FEITO COM LETRAS
nome = "joao"
print(nome.isalpha()),"\n"


#VERIFICA SE O TEXTO É FEITO COM NUMEROS
nome = "123"
print(nome.isnumeric(),"\n")


#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO
nome = "joao"
print(nome.replace("o","u"),"\n")

#SEPARA O TEXTO STRING BASEADO EM ALGUM CARACTERE INDICADO
nome = "joao @ paula fernades"
print(nome.split("@"),"\n")

#COLOCA TODAS AS LETRAS INICIAIS EM MINUSCULA
nome = "joão henrique domingos"
print(nome.title(),"\n")

#RETIRA OS CARACTERES INDESEJADOS, COMO POR EXEMPLO ESPAÇOS QUE NÃO AGRADAM VALOR
nome = " joao henrique domingos  "
print(nome.strip(),"\n")

#RETORNA TRUE OU FALSE PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO
nome = "joao 2008"
print(nome.startswith("ser"), "\n")
print(nome.startswith("Ser"),"\n")