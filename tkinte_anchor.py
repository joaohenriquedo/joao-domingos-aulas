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

#CODIGO ABAIXO CADA LABEL EM LUGARES DIFERENTES
#APOS TESTAR COMENTE A LINHA DO LB1 ATE O LB4

lb1.pack(side=LEFT)
lb2.pack(side="left")
lb3.pack(anchor="w") # SEMPRRE QUE NÃO UTILIZO A OPÇÃO SISIDE, ELE SEMPRE SERA TOPO
#lb4.pack(anchor="w") # SEMPRRE QUE NÃO UTILIZO A OPÇÃO SISIDE, ELE SEMPRE SERA TOPO


#lb4.pack(side=BOTTOM, anchor="sw")

lb4.pack(anchor="e")


i.mainloop()