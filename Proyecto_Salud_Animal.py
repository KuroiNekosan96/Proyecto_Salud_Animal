from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import font
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter




#from reportlab.pdfgen import canvas

def donothing():
    x=0


def operacion():

    def creaPDF():
        # creacion del pdf
        w, h = A4
        c = canvas.Canvas("prueba.pdf", pagesize=A4)
        c.drawString(50, h - 50, "¡Primer PDF!")
        c.showPage()
        c.save()

    colorFondo = "White"
    Helvifont = font.Font(family="Helvetica", size=10, weight="bold")
    r = Label(ventana, text="Ingrese el peso de la mascota: ",bg=colorFondo,font=Helvifont).place(x=20, y=250)
    r1 = Entry(ventana, textvariable=peso,font=Helvifont).place(x=230, y=250)
    r2 = Label(ventana, text="Escoga la enfermedad: ",bg=colorFondo,font=Helvifont).place(x=20, y=300)
    combo = ttk.Combobox(ventana,state="readonly")
    r= ttk.Combobox(ventana)
    combo.place(x=230, y=300)
    combo['values'] = (
    'Seleccione', '1-Moquillo', '2-Rabia', '3-Gripe', '4-Desnutrucion')
    combo.current(0)
    boton = Button(ventana, text="Enviar Resultados", command=creaPDF, bg=colorFondo, font=Hefont).place(x=20, y=335)

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
'''def generaPDF():
    c = canvas.Canvas("hola-mundo.pdf")
    c.save()
    c.drawString(50, 50, "¡Hola, mundo!")'''

#Aqui inicia la interfaz
ventana = Tk()
opcion=IntVar()
num=IntVar()
animal=StringVar()
peso=StringVar()

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
filemenu.add_command(label="New",command=donothing)
filemenu.add_command(label="Open",command=donothing)
filemenu.add_command(label="Exit",command=ventana.quit)
menubar.add_cascade(label="File",men=filemenu)


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
