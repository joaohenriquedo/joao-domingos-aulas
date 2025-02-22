def get_nome():
    nome_usuario = input("entre com o seu nome:")
    return nome_usuario
def print_mensagem(nome_usuario):
    print("ola jovem padawan", nome_usuario)
def main():
        nome_usuario = get_nome()
        print_mensagem(nome_usuario)
    
main()