#comando abaixo importa
#i(intanciar) recebe o objeto tk
from tkinter import *
i = Tk()
i.title("programa finaceiro")

#propiedade que altera o tamanho da janela
#(980x720) e distancia da direita e topo da janela
#(250x30)
i.geometry("980x720+250+30")

#propiedades graficas , cor de fundo da tela
#(bg) ou (background)

i["bg"]= "yellow"

#CRIA UM ICONE NA JANELA, VOCE DEVE A IMAGEM NO MESMO LOCAL DO CODIGO.
#i.wm_iconbitmap('icone .ico')

#cria um label e posiciona (place). ele em relação a tela.

lb = Label(i, text='Nome do usuario')
lb.place(x=100,y=100)

# cria um botão que posiciona (place ele em relação a label.

bt= Button(i, width='20', text='OK')
bt.place(x=230,y=100)

#gera a janela grafica
i.mainloop()
