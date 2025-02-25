from tkinter import *
i=Tk()
i.title("tabuada feita por João Henrique")
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1', bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 2', bg="pink")
lb2.place(x=230,y=200)

lb3 = Label(i,text='Label 3', bg="green")
lb3.place(x=230,y=200)

lb4 = Label(i,text='Label 4', bg="red")
lb4.place(x=230,y=200)


'''lb1.pack(side=TOP,fill=X) #COMANDO FILL É RESPONSAVEL DO PREENCHIMENTO 100%, DEVE USAR X PARA HORIZONTAL E DEVE SER MAIUSCULO

lb2.pack(side=RIGHT,fill=X) #COMANDO FILL É RESPONSAVEL DO PREENCHIMENTO 100%, DEVE USAR X PARA VERTICAL E DEVE SER MAIUSCULO

lb3.pack(side=LEFT,fill=X) #COMANDO FILL É RESPONSAVEL DO PREENCHIMENTO 100%, DEVE USAR X PARA HORIZONTAL E DEVE SER MAIUSCULO

lb4.pack(side=BOTTOM,fill=X) #COMANDO FILL É RESPONSAVEL DO PREENCHIMENTO 100%, DEVE USAR X PARA VERTICAL E DEVE SER MAIUSCULO'''


lb1.pack(side=TOP,fill=BOTH,expand=1) 
lb2.pack(side=TOP,fill=BOTH,expand=1) 
lb3.pack(side=TOP,fill=BOTH,expand=1) 
lb4.pack(side=TOP,fill=BOTH,expand=1) 

i.mainloop()
