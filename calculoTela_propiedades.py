from tkinter import *

def bt_soma():
    #codigo abaixo é para a entrada apenas de numeros
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #se valores nao forem numericos imprime a mensagem abaixo:
        lb["text"] = num1 + num2
        lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "valores invalidos"
        lb["bg"] = "red"

def bt_subtracao():
 if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2
    lb["bg"] = "#00FA9A"



def bt_multiplicacao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def bt_divisao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2









i=Tk()
i.title("tabuada feita por João Henrique")
i.geometry('980x720+250+30')


lb=Label(i,text="0")
lb.place(x=230,y=200)

bt=Button(i,width="20",text = 'adição', command=bt_soma)
bt.place(x=230,y=230)

bt=Button(i,width="20",text = 'subtração', command=bt_subtracao)
bt.place(x=230,y=260)

bt=Button(i,width="20",text = 'multiplicação', command=bt_multiplicacao)
bt.place(x=230,y=290)

bt=Button(i,width="20",text = 'divisão', command=bt_divisao)
bt.place(x=230,y=310)


lb2=Label(i,text="João Henrique")
lb2.place(x=400,y=340)





ed1 = Entry(i)
ed1.place(x=230,y=150)
            
ed2 = Entry(i)
ed2.place(x=230,y=180)

i.mainloop()


