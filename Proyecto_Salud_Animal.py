from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import font
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time
import tkinter as tk


def abrirventana2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('380x300')
    win.configure(background='dark turquoise')
    e3=tk.Label(win,text="Bienvenido Salud Animal CRYP")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    boton3=Button(win,text='OK',command=win.destroy)
    boton3.pack(side=tk.TOP)

def cerrarVentana():
    ventana.destroy()
#Metodo para limpiar variables

def newFile():
    opcion.set("")
    peso.set("")
    edad.set("")

def mostrarManual():
    ventana2 = Tk()
    ventana2.title("Salud Animal CRYP-Manual de Uso")
    ventana2.geometry("370x370")
    etiqueta2 = Label(ventana2, text="1.-Elegir una entre las cuatro opciones").place(x=80, y=80)
    etiqueta3 = Label(ventana2, text="2.-Dar Clic en aceptar, se desplegará más opciones").place(x=80, y=120)
    etiqueta4 = Label(ventana2, text="3.-Ingresar el peso de la mascota en gramos").place(x=80, y=160)
    etiqueta5 = Label(ventana2, text="4.-Elegir una de las enfermedades especificadas").place(x=80, y=200)
    etiqueta6 = Label(ventana2, text="5.-Ingresar la edad del perro").place(x=80, y=240)
    etiqueta7 = Label(ventana2, text="6.-Dar clic en enviar resultados").place(x=80, y=280)
    ventana2.mainloop()

#Metodo para guardar variables falta la del combo
def guardar():
    animal=opcion.get();
    peso=r.get();
    edad=r2.get();


def operacion():
    colorFondo = "White"
    Helvifont = font.Font(family="Helvetica", size=10, weight="bold")
    r = Label(ventana, text="Peso de la mascota en Kg: ",bg=colorFondo,font=Helvifont).place(x=20, y=250)
    r1 = Entry(ventana, textvariable=peso,font=Helvifont).place(x=230, y=250)
    r2 = Label(ventana, text="Elija la enfermedad: ",bg=colorFondo,font=Helvifont).place(x=20, y=300)
    combo = ttk.Combobox(ventana,state="readonly")
    r= ttk.Combobox(ventana)
    combo.place(x=230, y=300)
    combo['values'] = (
    'Seleccione', '1-Moquillo', '2-Rabia', '3-Gripe', '4-Desnutrucion','5-Infección por Campylobacter','6-La toxoplasmosis','7-La tiña')
    etiqueta2 = Label(ventana, text="Ingresar Edad de la mascota:", bg=colorFondo, font=Helfont).place(x=20, y=340)
    ed = Entry(ventana, textvariable=edad, font=Helvifont).place(x=230, y=340)
    boton = Button(ventana, text="Enviar Resultados", command=abrirventana2, bg=colorFondo, font=Hefont).place(x=20, y=370)


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

#--------Encabezado...... PDF..............
canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)

canvas.drawString(270, 750, 'SALUD ANIMAL')
canvas.drawString(30, 720, 'Correo: saludanimal@hotmail.com')
canvas.drawString(500, 720, 'Fecha:' + time.strftime("%d/%m/%y"))
canvas.line(500, 715, 585, 715)
canvas.drawString(30, 690, 'Telefono: 2345678')

canvas.drawString(220, 660, 'DETALLES DE LA MEDICACIÓN:')

canvas.line(20, 50, 580, 50)

canvas.save()
#...............-------------------------.................................

#Aqui inicia la interfaz
#Variables Globales
ventana = Tk()
r=DoubleVar()
peso=StringVar()
enfermedad=StringVar()
r2=IntVar()
opcion=IntVar()
num=IntVar()
animal=IntVar()
edad=IntVar()



#Aqui inicia para la barra de herramientas


ventana.title("Salud Animal CRYP")
ventana.geometry("830x400")
ventana.maxsize(height=400,width=830)
#Código para cargar imagen utilizando Pil
img = ImageTk.PhotoImage(Image.open("fondoanimal.jpg"))
l=Label(image=img)
l.pack()



menubar=Menu(ventana)
filemenu=Menu(menubar,tearoff=0)
filemenu1=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Menú",men=filemenu)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Exit",command=ventana.quit)

menubar.add_cascade(label="Informacion",men=filemenu1)
filemenu1.add_command(label="Manual",command=mostrarManual)


colorFondo="White"
Helvfont=font.Font(family="Helvetica",size=30,weight="bold")
etiquetaTitulo = Label(ventana, text="Salud Animal",font=Helvfont,bg=colorFondo).place(x=120, y=10)



Helfont=font.Font(family="Helvetica",size=10,weight="bold")

etiqueta1=Label(ventana, text="Elige tu opción",bg=colorFondo,font=Helfont).place(x=20,y=80)
xGato=Radiobutton(ventana, text="Gato", value=1, variable=opcion,bg=colorFondo,font=Helfont).place(x=20,y=120)
xPerro=Radiobutton(ventana, text="Perro", value=2, variable=opcion,bg=colorFondo,font=Helfont).place(x=110,y=120)
xCanarios=Radiobutton(ventana, text="Canarios", value=3, variable=opcion,bg=colorFondo,font=Helfont).place(x=20,y=150)
xhamster=Radiobutton(ventana, text="Hamster", value=4, variable=opcion,bg=colorFondo,font=Helfont).place(x=110,y=150)
Hefont=font.Font(family="Helvetica",size=10,weight="bold")
boton=Button(ventana,text="Aceptar",command=operacion,bg=colorFondo,font=Hefont).place(x=20,y=200)

ventana.config(menu=menubar)
ventana.mainloop()