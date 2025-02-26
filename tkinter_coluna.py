from tkinter import *
i=Tk()
i.title("tabuada feita por João Henrique")
i.geometry('980x720+250+30')


'''lb1 = Label(i,text="login",bg="yellow")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e coluna(collumn)
lb1.grid(row=2,column=1)

lb2 = Label(i,text="SENHA", bg="blue")
lb2.grid(row=10, column=2)

ed1 = Entry(i)
ed1.grid(row=3, column=4)

ed2 = Entry(i)
ed2.grid(row=4, column=4)

bt1 = Button(i,text="Login")
bt1.grid(row=3,column=2)'''

# O CODIGO ABAIXO FAZ CORREÇÃO DA SPOSIÇÕES DAS LABLES, CAIXA DE TEXTO E BOTAO
lb1 = Label(i,text="login",bg="yellow")
lb1.grid(row=2,column=1)

lb2 = Label(i,text="SENHA", bg="blue")
lb2.grid(row=2, column=1)

ed1 = Entry(i)
ed1.grid(row=1, column=2)

ed2 = Entry(i)
ed2.grid(row=2, column=2)

bt1 = Button(i,text="Login")
bt1.grid(row=2,column=2)


i.mainloop()