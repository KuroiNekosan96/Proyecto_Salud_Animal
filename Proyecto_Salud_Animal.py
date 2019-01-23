from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
#from reportlab.pdfgen import canvas

def operacion():
    r = Label(ventana, text="Ingrese el peso de la mascota:").place(x=20, y=180)
    r1 = Entry(ventana, textvariable=peso).place(x=180, y=180)
    r2 = Label(ventana, text="Escoga la enfermedad: ").place(x=20, y=200)
    combo = ttk.Combobox(ventana,state="readonly")
    r= ttk.Combobox(ventana)
    combo.place(x=180, y=200)
    combo['values'] = (
    'Seleccione', '1-Moquillo', '2-Rabia', '3-Gripe', '4-Desnutrucion')
    combo.current(0)

    numero=num.get()
    if opcion.get()==1:
        animal="Gato"
        print("Ha elegido gato")
    elif opcion.get()==2:
        animal="Perro"
        print("Ha elegido perro")

    if opcion.get()==3:
        animal="Canario"
        print("Ha elegido Canario")
    elif opcion.get()==4:
        animal="Hamster"
        print("Ha elegido Hamster")
    r.config(state=DISABLED)



#pip install reportlab
def generaPDF():
    c = canvas.Canvas("hola-mundo.pdf")
    c.save()
    c.drawString(50, 50, "¡Hola, mundo!")

#Aqui inicia la interfaz
ventana = Tk()
opcion=IntVar()
num=IntVar()
animal=StringVar()
peso=StringVar()
ventana.title("Salud Animal")
ventana.geometry("500x500")

#Código para cargar imagen utilizando Pil
img = ImageTk.PhotoImage(Image.open("170511.jpg"))
l=Label(image=img)
l.pack()

etiquetaTitulo = Label(ventana, text="Salud Animal").place(x=120, y=10)

etiqueta1=Label(ventana, text="Elige tu opción").place(x=20,y=50)
xGato=Radiobutton(ventana, text="Gato", value=1, variable=opcion).place(x=20,y=80)
xPerro=Radiobutton(ventana, text="Perro", value=2, variable=opcion).place(x=70,y=80)
xCanarios=Radiobutton(ventana, text="Canarios", value=3, variable=opcion).place(x=20,y=100)
xhamster=Radiobutton(ventana, text="Hamster", value=4, variable=opcion).place(x=110,y=100)
boton=Button(ventana,text="Aceptar",command=operacion).place(x=20,y=140)
ventana.mainloop()
