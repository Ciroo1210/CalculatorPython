from tkinter import * 

Ventana = Tk()
Ventana.title("Calculadora")

i = 0


e_texto = Entry(Ventana, font= ("Calibri 20"))
e_texto.grid(row=0, column=0, columnspan= 4, padx= 50, pady=5)

def  click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete(0, END)
    i = 0

def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i = 0



# numeros
boton1 = Button(Ventana, text="1",width=5,height=2, command= lambda: click_boton(1))
boton2 = Button(Ventana, text="2",width=5,height=2, command= lambda: click_boton(2))
boton3 = Button(Ventana, text="3",width=5,height=2, command= lambda: click_boton(3))
boton4 = Button(Ventana, text="4",width=5,height=2, command= lambda: click_boton(4))
boton5 = Button(Ventana, text="5",width=5,height=2, command= lambda: click_boton(5))
boton6 = Button(Ventana, text="6",width=5,height=2, command= lambda: click_boton(6))
boton7 = Button(Ventana, text="7",width=5,height=2, command= lambda: click_boton(7))
boton8 = Button(Ventana, text="8",width=5,height=2, command= lambda: click_boton(8))
boton9 = Button(Ventana, text="9",width=5,height=2, command= lambda: click_boton(9))
boton0 = Button(Ventana, text="0",width=19,height=2, command= lambda: click_boton(0))

#botones no numericos
botonborrar = Button(Ventana, text="AC",width=5,height=2, command= lambda: borrar())
botonparentesis1 = Button(Ventana, text="(",width=5,height=2, command= lambda: click_boton("("))
botonparentesis2 = Button(Ventana, text=")",width=5,height=2, command= lambda: click_boton(")"))
boton_pun = Button(Ventana, text=".",width=5,height=2, command= lambda: click_boton("."))
botondiv = Button(Ventana, text="/",width=5,height=2, command= lambda: click_boton("/"))
botonmul = Button(Ventana, text="x",width=5,height=2, command= lambda: click_boton("*"))
botonres = Button(Ventana, text="-",width=5,height=2, command= lambda: click_boton("-"))
botonsum = Button(Ventana, text="+",width=5,height=2, command= lambda: click_boton("+"))
botonigual = Button(Ventana, text="=",width=5,height=2, command= lambda: operacion())

#interfaz

botonborrar.grid(row =1, column =0, padx = 5, pady = 5)
botonparentesis1.grid(row =1, column =1, padx = 5, pady = 5)
botonparentesis2.grid(row =1, column =2, padx = 5, pady = 5)
botondiv.grid(row =1, column =3, padx = 5, pady = 5)

botonmul.grid(row =2, column =3, padx = 5, pady = 5)
botonres.grid(row =4, column =3, padx = 5, pady = 5)
botonigual.grid(row =5, column =3, padx = 5, pady = 5)
botonsum.grid(row =3, column =3, padx = 5, pady = 5)

boton_pun.grid(row =5, column = 2, padx = 5, pady = 5)
boton7.grid(row =2, column =0, padx = 5, pady = 5)
boton8.grid(row =2, column =1, padx = 5, pady = 5)
boton9.grid(row =2, column =2, padx = 5, pady = 5)

boton4.grid(row =3, column =0, padx = 5, pady = 5)
boton5.grid(row =3, column =1, padx = 5, pady = 5)
boton6.grid(row =3, column =2, padx = 5, pady = 5)

boton1.grid(row =4, column =0, padx = 5, pady = 5)
boton2.grid(row =4, column =1, padx = 5, pady = 5)
boton3.grid(row =4, column =2, padx = 5, pady = 5)

boton0.grid(row =5, column =0,columnspan=2, padx = 5, pady = 5)


Ventana.mainloop()