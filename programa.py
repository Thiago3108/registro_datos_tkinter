#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox, ttk

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel centigrados
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title("Registro de notas")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("400x200")
    toplevel_notas.config(bg="white")

   
    # etiqueta para el registro de notas
    lb_notas = Label(toplevel_notas, text = "Notas del estudiante ")
    lb_notas.config(bg="white", fg="dark khaki", font=("Helvetica", 18))
    lb_notas.place(x=10, y=10)

    #--------------------------------
    # frame entrada datos en el
    #--------------------------------
    frame_entrada = Frame(toplevel_notas)
    frame_entrada.config(bg="snow2", width=380, height=140)
    frame_entrada.place(x=10, y=50)

    # etiqueta para valor de la nota 1
    lb_notas = Label(frame_entrada, text = "Nota 1 = ")
    lb_notas.config(bg="snow2", fg="black", font=("Helvetica", 18))
    lb_notas.place(x=10, y=20)

    # caja de texto para valor de la nota 1
    entry_notas = Entry(frame_entrada, textvariable=notas)
    entry_notas.config(bg="white", fg="black", font=("Times New Roman", 18), width=6)
    entry_notas.focus_set()
    entry_notas.place(x=120,y=20)

        # etiqueta para valor de la nota 2
    lb_notas = Label(frame_entrada, text = "Nota 2 = ")
    lb_notas.config(bg="snow2", fg="black", font=("Helvetica", 18))
    lb_notas.place(x=10, y=60)

    # caja de texto para valor de la nota 2
    entry_notas = Entry(frame_entrada, textvariable=nota2)
    entry_notas.config(bg="white", fg="black", font=("Times New Roman", 18), width=6)
    entry_notas.place(x=120,y=60)

        # etiqueta para valor de la nota 3
    lb_notas = Label(frame_entrada, text = "Nota 3 = ")
    lb_notas.config(bg="snow2", fg="black", font=("Helvetica", 18))
    lb_notas.place(x=10, y=100)

    # caja de texto para valor de la nota 3
    entry_notas = Entry(frame_entrada, textvariable=nota3)
    entry_notas.config(bg="white", fg="black", font=("Times New Roman", 18), width=6)
    entry_notas.place(x=120,y=100)

    # lista para kelvin y fahrenheit
    cmb_kf = ttk.Combobox(frame_entrada, textvariable=prom_selected, values=prom, font=("Helvetica", 12))
    cmb_kf.place(x=250, y=30, width= 100, height=30)

    # boton para aceptar 
    bt_aceptar = Button(frame_entrada,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=250, y=70, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(notas.get())
    toplevel_notas.destroy()

# convertir
def promediar():
    messagebox.showinfo("Promedio de notas", "Promedio realizado")
    # cent = int(c.get())
    if prom.get()=="kelvin":
        k = cent + 273.15
        t_resultados.insert(INSERT, f"\n{int(notas.get())} °C equivalen a {k} °K")
    elif prom.get() == "fahrenheit":
        f = cent*9/5 + 32
        t_resultados.insert(INSERT, f"\n{int(notas.get())} °C equivalen a {f} °F")
    else:
        t_resultados.insert(INSERT, "Debe seleccionar una opción")
    
# borrar
def borrar():
    messagebox.showinfo("Registro de estudiante", "Los datos serán borrados")
    notas.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Registro de estudiante", "La app se va a cerrar")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Registro estudiante")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="khaki")

#--------------------------------
# variables globales
#--------------------------------
notas,nota2,nota3,name,cod = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
prom = StringVar()
prom = ["Fundamentos de programacion", "Calculo I", "Alegebra lineal", "Quimica Basica", "Taller de lenguaje"]
prom_selected = StringVar()



#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=580, height=180)
frame_entrada.place(x=10, y=10)


# titulo de la app
titulo = Label(frame_entrada, text="Registro de estudiante")
titulo.config(bg = "white",fg="dark khaki", font=("MuseJazz Text", 20))
titulo.place(x=10,y=10)

# etiqueta para valor del nombre
lb_c = Label(frame_entrada, text = "Nombre")
lb_c.config(bg="white", fg="black", font=("MuseJazz Text", 12))
lb_c.place(x=10, y=50)

# caja de texto para el nombre
entry_c = Entry(frame_entrada, textvariable=name)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 10), width=30)
entry_c.focus_set()
entry_c.place(x=10,y=80)

# etiqueta para valor del codigo de estudiante
lb_c = Label(frame_entrada, text = "Codigo de estudiante")
lb_c.config(bg="white", fg="black", font=("MuseJazz Text", 12))
lb_c.place(x=10, y=105)

# caja de texto para el codigo de estudiante 
entry_c = Entry(frame_entrada, textvariable=cod)
entry_c.config(bg="white", fg="blue", font=("Times New Roman", 10), width=30)
entry_c.place(x=10,y=135)

# boton para abrir Toplevel para ingresar notas
# logo de la app
#logo = PhotoImage(file="img/temperatura.png")
#lb_logo = Label(frame_entrada, image=logo, bg="white")
#lb_logo.place(x=70,y=40)
notas = PhotoImage(file="notas.png")
bt_centigrados = Button(frame_entrada,image=notas ,text="Ingresar notas", command=abrir_toplevel_notas)
bt_centigrados.place(x=290, y=60, width=100)

# boton para abrir Toplevel para ingresar datos medicos
bt_medico = Button(frame_entrada, text="Ingresar datos", command=abrir_toplevel_notas)
bt_medico.place(x=430, y=60, width=100)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=580, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir
bt_convertir = Button(frame_operaciones,text="Promediar", command=promediar)
bt_convertir.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=580, height=280)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="white", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=560,height=160)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()