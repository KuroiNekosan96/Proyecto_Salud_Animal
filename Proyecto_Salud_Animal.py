from tkinter import *

#solo adjunte un método de prueba si es de ser necesario cambiarlo
def operacion():
    numero=num.get()
    if opcion.get()==1:
        print("Ha elegido gato")
    elif opcion.get()==2:
        b="Perro"
        print("Ha elegido perro")
    else:
        print("No ha elegido nada")

#Aqui empieza la interfaz del programa por favor empezar añadiendo más cosas para el diseño

ventana = Tk()
opcion=IntVar()
num=IntVar()

ventana.title("Salud Animal")
ventana.geometry("250x250")

etiquetaTitulo = Label(ventana, text="Salud Animal").place(x=270, y=10)

etiqueta1=Label(ventana, text="Elige tu opción").place(x=20,y=50)
xGato=Radiobutton(ventana, text="Gato", value=1, variable=opcion).place(x=20,y=80)
xPerro=Radiobutton(ventana, text="Perro", value=2, variable=opcion).place(x=70,y=80)
boton=Button(ventana,text="imprima que eligió",command=operacion).place(x=20,y=140)
ventana.mainloop()
