from tkinter import *

#CRIANDO UMA FUNÇÃO PARA CLIQUE NO BOTÃO
def bt_click():
    # o label que usa propiedade text recebera a mensagem "trocou o texto"
    # a mensagem "trocou o texto"
    lb["text"] = "trocou o texto"
    #esse print abaixo exibe o texto na tela do console
    print("BOTÃO FOI CLICADO")

def bt_clickar():
    #esse print exibe exibe o texto digitado na caixa de texto e exibe na label da tela
    print(ed.get())
    lb["text"]=ed.get()

    # i de (instanciar) recebe o objeto TK
    i=Tk()
    #gerar titulo na janela
    i.title('programa finaceiro')
    i.geometry('980x720+250+30')
    i["bg"]= "green"
    #i.wm_iconbitmap('icone .ico')
    lb = Label(i,text='Nome do usuario')
    lb.place(x=100,y=100)

    bt = Button(i,width="20", text ='OK',
    command=bt_click)
    bt.place(x=230,y=100)
#o codigo abaixo cria um botão e posiciona abaixo do botão OK
    bt = Button(i,width="20", text='capturar',
   command=bt_click)
    bt.place(x=230,y=190)

    #O CODIGO ABAIXO CRIA A ACIXA DE TEXTO PARA DIDITAR ALGO DENTRO
    ed=Entry(i)
    ed.place(x=230,y=150)

    i.mainloop()
