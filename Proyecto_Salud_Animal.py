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

def mostrarEnfermedad():
    ventana3 = Tk()
    ventana3.title("Salud Animal CRYP-Enfermedad")
    ventana3.geometry("1000x370")
    opciones=combo.get()
    if opcion.get()==1:
        etiqueta2 = Label(ventana3,
                          text="Otitis: Es una inflamación del conducto auditivo muy común en los perros, pero también en los gatitos y en los gatos adultos").place(
            x=80, y=80)
        etiqueta3 = Label(ventana3, text="Conjuntivitis: Es uno de los problemas más frecuentes en los gatos que se puede dar a cualquier edad. Se trata de la inflamación de la mucosa del ojo.").place(x=80, y=120)
        etiqueta4 = Label(ventana3, text="El gato puede llegar a perder la vista si no se diagnostica y se trata a tiempo. ").place(x=80, y=140)
        etiqueta5 = Label(ventana3, text="Rabia: Esta enfermedad causa un virus que se transmite a través de la saliva por la mordedura de un animal infectado.\n Se puede transmitir entre especies, de animales a humanos y viceversa\n").place(x=80, y=200)
        etiqueta6 = Label(ventana3, text="Panleucopenia felina: omo moquillo felino, enteritis o gastroenteritis infecciosa. Es una enfermedad mortal provocada por un parvovirus y los síntomas").place(x=80, y=260)
        etiqueta7 = Label(ventana3, text="más comunes son la fiebre y más adelante la hipotermia, los vómitos, la diarrea, la debilidad, la deshidratación, la anorexia y una importante bajada \nde los leucocitos y/o glóbulos blancos en la sangre.").place(x=80, y=280)
    elif opcion.get()==2:
        etiqueta2 = Label(ventana3,text="Moquillo: Esta enfermedad también es más grave en cachorros, tampoco tiene tratamiento específico.\nLos síntomas pueden ser respiratorios, digestivos o neurológicos en los casos más graves.").place(x=80, y=80)
        etiqueta3 = Label(ventana3,text="Artrosis: Este problema es una inflamación y degeneración de las articulacionesque puede ser secundaria a muchos otros problemas. \nLos más frecuentes son la displasia de cadera, displasia de codo y la obesidad.").place(x=80, y=120)

        etiqueta5 = Label(ventana3,text="Problemas urinarios: Los problemas urinarios son muy variados. El más común es la cistitis, más frecuente en animales mayores").place(x=80, y=200)
        etiqueta6 = Label(ventana3,text="Problemas digestivos: Es una clasificación un poco general, pero los vómitos y la diarrea son una de las causas más frecuentes de visita al veterinario.").place(x=80, y=260)


    palabra=opciones[0]
    print(opciones)


    ventana3.mainloop()
#Metodo para guardar variables falta la del combo
def guardar():
    animal=opcion.get();
    peso=r.get();
    edad=r2.get();


def operacion():

    if opcion.get()==1:
        mascota="Gato"
        print("Ha elegido gato")
        colorFondo = "White"
        Helvifont = font.Font(family="Helvetica", size=10, weight="bold")
        r = Label(ventana, text="Peso de la mascota en Kg: ", bg=colorFondo, font=Helvifont).place(x=20, y=250)
        r1 = Entry(ventana, textvariable=peso, font=Helvifont).place(x=230, y=250)
        r2 = Label(ventana, text="Elija la enfermedad: ", bg=colorFondo, font=Helvifont).place(x=20, y=300)

        r = ttk.Combobox(ventana)
        combo.place(x=230, y=300)
        combo['values'] = ( 'Seleccione', '1-Otitis', '2-Conjuntivitis', '3-Rabia', '4-Panleucopenia felina')
        combo.current(0)

        etiqueta2 = Label(ventana, text="Ingresar Edad de la mascota:", bg=colorFondo, font=Helfont).place(x=20, y=340)
        ed = Entry(ventana, textvariable=edad, font=Helvifont).place(x=230, y=340)
        boton = Button(ventana, text="Enviar Resultados", command=abrirventana2, bg=colorFondo, font=Hefont).place(x=20,y=370)
        boton2 = Button(ventana, text="Ver enfermedad", command=mostrarEnfermedad, bg=colorFondo, font=Hefont).place(x=160,y=370)
        opciones = combo.get()

        r.config(state=DISABLED)

    elif opcion.get()==2:
        mascota="Perro"
        print("Ha elegido perro")
        colorFondo = "White"
        Helvifont = font.Font(family="Helvetica", size=10, weight="bold")
        r3 = Label(ventana, text="Peso de la mascota en Kg: ", bg=colorFondo, font=Helvifont).place(x=20, y=250)
        r4 = Entry(ventana, textvariable=peso, font=Helvifont).place(x=230, y=250)
        r5 = Label(ventana, text="Elija la enfermedad: ", bg=colorFondo, font=Helvifont).place(x=20, y=300)

        r = ttk.Combobox(ventana)
        combo.place(x=230, y=300)
        combo['values'] = ('Seleccione', '1-Moquillo', '2-Artrosis', '3-Problemas urinarios', '4-Problemas digestivos')
        combo.current(0)
        etiqueta2 = Label(ventana, text="Ingresar Edad de la mascota:", bg=colorFondo, font=Helfont).place(x=20, y=340)
        ed = Entry(ventana, textvariable=edad, font=Helvifont).place(x=230, y=340)
        boton = Button(ventana, text="Enviar Resultados", command=abrirventana2, bg=colorFondo, font=Hefont).place(x=20,
                                                                                                                   y=370)
        boton2 = Button(ventana, text="Ver enfermedad", command=mostrarEnfermedad, bg=colorFondo, font=Hefont).place(x=160,
                                                                                                                 y=370)
        r.config(state=DISABLED)

    if opcion.get()==3:
        animal="Canario"
        print("Ha elegido Canario")
    elif opcion.get()==4:
        animal="Hamster"
        print("Ha elegido Hamster")


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
opciones=StringVar()
palabra=StringVar()
mascota=StringVar()

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

combo = ttk.Combobox(ventana, state="readonly")

Helfont=font.Font(family="Helvetica",size=10,weight="bold")

etiqueta1=Label(ventana, text="Elige tu opción",bg=colorFondo,font=Helfont).place(x=20,y=80)
xGato=Radiobutton(ventana, text="Gato", value=1, variable=opcion,bg=colorFondo,font=Helfont).place(x=20,y=120)
xPerro=Radiobutton(ventana, text="Perro", value=2, variable=opcion,bg=colorFondo,font=Helfont).place(x=110,y=120)
#xTortugas=Radiobutton(ventana, text="Tortugas", value=3, variable=opcion,bg=colorFondo,font=Helfont).place(x=20,y=150)
#xhamster=Radiobutton(ventana, text="Hamster", value=4, variable=opcion,bg=colorFondo,font=Helfont).place(x=110,y=150)
Hefont=font.Font(family="Helvetica",size=10,weight="bold")
boton=Button(ventana,text="Aceptar",command=operacion,bg=colorFondo,font=Hefont).place(x=20,y=200)

ventana.config(menu=menubar)
ventana.mainloop()