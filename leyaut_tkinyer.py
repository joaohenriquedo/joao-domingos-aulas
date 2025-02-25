from tkinter import *
i=Tk()
i.title("tabuada feita por João Henrique")
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1', bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 1', bg="pink")
lb2.place(x=230,y=200)

lb3 = Label(i,text='Label 1', bg="green")
lb3.place(x=230,y=200)

lb4 = Label(i,text='Label 1', bg="red")
lb4.place(x=230,y=200)

"""lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()"""
#o codigo abaixo é respondavel por posicionar o label no topo da interface
'''lb1.pack(side="top")
#o codigo abaixo é respondavel por posicionar o label na esquerda
lb2.pack(side="left")
# o codigo abaixo é responsavel por posicionar para direita
lb3.pack(side="right")
# o codigo abaixo é responsavel por posicionar para baixo
lb4.pack(side="bottom")'''


lb1.pack(side="left")
lb2.pack(side="left")
lb3.pack(side="right")
lb4.pack(side="right")











i.mainloop()