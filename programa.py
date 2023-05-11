#---------------------------------
# Desktop app -Estudiante 
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox, ttk

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel notas
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
    frame_notas = Frame(toplevel_notas)
    frame_notas.config(bg="snow2", width=380, height=140)
    frame_notas.place(x=10, y=50)

    # etiqueta para valor de la nota 1
    lb_notas = Label(frame_notas, text = "Nota 1 = ")
    lb_notas.config(bg="snow2", fg="black", font=("Helvetica", 18))
    lb_notas.place(x=10, y=20)

    # caja de texto para valor de la nota 1
    entry_notas = Entry(frame_notas, textvariable=notas)
    entry_notas.config(bg="white", fg="black", font=("Times New Roman", 18), width=6)
    entry_notas.focus_set()
    entry_notas.place(x=120,y=20)

        # etiqueta para valor de la nota 2
    lb_notas = Label(frame_notas, text = "Nota 2 = ")
    lb_notas.config(bg="snow2", fg="black", font=("Helvetica", 18))
    lb_notas.place(x=10, y=60)

    # caja de texto para valor de la nota 2
    entry_notas = Entry(frame_notas, textvariable=nota2)
    entry_notas.config(bg="white", fg="black", font=("Times New Roman", 18), width=6)
    entry_notas.place(x=120,y=60)

        # etiqueta para valor de la nota 3
    lb_notas = Label(frame_notas, text = "Nota 3 = ")
    lb_notas.config(bg="snow2", fg="black", font=("Helvetica", 18))
    lb_notas.place(x=10, y=100)

    # caja de texto para valor de la nota 3
    entry_notas = Entry(frame_notas, textvariable=nota3)
    entry_notas.config(bg="white", fg="black", font=("Times New Roman", 18), width=6)
    entry_notas.place(x=120,y=100)

    # lista para las materias
    cmb_materias = ttk.Combobox(frame_notas, textvariable=prom_selected, values=prom, font=("Helvetica", 12))
    cmb_materias.place(x=250, y=30, width= 100, height=30)

    # boton para aceptar 
    bt_aceptar = Button(frame_notas,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=250, y=70, width=100, height=30)


# aceptar
def aceptar():
    toplevel_notas.destroy()
    global nota
    global nota_2
    global nota_3
    nota = float(notas.get())
    nota_2 = float(nota2.get())
    nota_3 = float(nota3.get())

# abrir toplevel datos medicos
def abrir_toplevel_medico():
    global toplevel_medico
    toplevel_medico = Toplevel()
    toplevel_medico.title("Registro de datos medicos")
    toplevel_medico.resizable(False, False)
    toplevel_medico.geometry("400x220")
    toplevel_medico.config(bg="white")

    # etiqueta para el registro de notas
    lb_medico = Label(toplevel_medico, text = "Indice de masa corporal")
    lb_medico.config(bg="white", fg="dark khaki", font=("Helvetica", 18))
    lb_medico.place(x=10, y=10)

    #--------------------------------
    # frame entrada datos en el
    #--------------------------------
    frame_medico = Frame(toplevel_medico)
    frame_medico.config(bg="snow2", width=380, height=160)
    frame_medico.place(x=10, y=50)

    # etiqueta para valor de la nota 1
    lb_medico = Label(frame_medico, text = "Peso (En Kg) = ")
    lb_medico.config(bg="snow2", fg="black", font=("Helvetica", 16))
    lb_medico.place(x=10, y=20)

    # caja de texto para valor de la nota 1
    entry_medico = Entry(frame_medico, textvariable=kilo)
    entry_medico.config(bg="white", fg="black", font=("Times New Roman", 16), width=6)
    entry_medico.focus_set()
    entry_medico.place(x=160,y=16)

    # etiqueta para valor de la nota 2
    lb_medico = Label(frame_medico, text = "Estatura = ")
    lb_medico.config(bg="snow2", fg="black", font=("Helvetica", 16))
    lb_medico.place(x=10, y=60)

    # caja de texto para valor de la nota 2
    entry_medico = Entry(frame_medico, textvariable=estatura)
    entry_medico.config(bg="white", fg="black", font=("Times New Roman", 16), width=6)
    entry_medico.place(x=120,y=60)

    # boton para aceptar 
    bt_aceptar2 = Button(frame_medico,text="Aceptar", command=aceptar2)
    bt_aceptar2.place(x=10, y=110, width=100, height=30)
 
#aceptar2 
def aceptar2():
    toplevel_medico.destroy()
    global kilo1
    global estatura1
    global name
    global cod 
    kilo1 = float(kilo.get())
    estatura1 = float(estatura.get())
    

# convertir
def promediar():
    t_resultados.delete("1.0","end")
    if nota != 0 and nota_2 != 0 and nota_3 != 0:
        nota_final = (nota + nota_2 + nota_3) / 3
        t_resultados.insert("end", f"Sus notas en la asignatura {prom_selected.get()} fueron:\nNota 1 => {nota}\nNota 2 => {nota_2}\nNota 3 => {nota_3}\nPromedio => {nota_final}\n")
        messagebox.showinfo("Promedio de notas", "Promedio realizado")
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar notas para calcular el promedio")

def IMC():
    t_resultados2.delete("1.0","end")
    if estatura1 != 0 and kilo1 != 0:
        masa_corporal= kilo1/(estatura1 **2 )
        t_resultados2.insert("end", f"El estudiante {name.get()}, registrado con el codigo {cod.get()} posee un IMC de: \n{masa_corporal}\n")
        messagebox.showinfo("IMC", "IMC realizado")
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar dato para calcular el IMC")
    
# borrar
def borrar():
    messagebox.showinfo("Registro de estudiante", "Los datos serán borrados")
    prom_selected.set("")
    t_resultados.delete("1.0","end")
    t_resultados2.delete("1.0","end")
    
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
notas,nota2,nota3,name,cod,kilo, estatura = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
prom = StringVar()
prom = ["Fundamentos de programacion", "Calculo I", "Alegebra lineal", "Quimica Basica", "Taller de lenguaje"]
prom_selected = StringVar()
nota_final= StringVar()

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
lb_nombre = Label(frame_entrada, text = "Nombre")
lb_nombre.config(bg="white", fg="black", font=("MuseJazz Text", 12))
lb_nombre.place(x=10, y=50)

# caja de texto para el nombre
entry_nombre = Entry(frame_entrada, textvariable=name)
entry_nombre.config(bg="white", fg="black", font=("Times New Roman", 10), width=30)
entry_nombre.focus_set()
entry_nombre.place(x=10,y=80)

# etiqueta para valor del codigo de estudiante
lb_codigo = Label(frame_entrada, text = "Codigo de estudiante")
lb_codigo.config(bg="white", fg="black", font=("MuseJazz Text", 12))
lb_codigo.place(x=10, y=105)

# caja de texto para el codigo de estudiante 
entry_codigo = Entry(frame_entrada, textvariable=cod)
entry_codigo.config(bg="white", fg="black", font=("Times New Roman", 10), width=30)
entry_codigo.place(x=10,y=135)

# boton para abrir Toplevel para ingresar datos medicos
medico = PhotoImage(file="medico.png")
bt_medico = Button(frame_entrada,image=medico ,text="Ingresar datos", command=abrir_toplevel_medico)
bt_medico.config(bg="white")
bt_medico.place(x=430, y=60, width=100)

# boton para abrir Toplevel para ingresar notas
nota = PhotoImage(file="notas.png")
bt_nota = Button(frame_entrada,image=nota ,text="Ingresar notas", command=abrir_toplevel_notas)
bt_nota.config(bg="white")
bt_nota.place(x=290, y=60, width=100)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=580, height=100)
frame_operaciones.place(x=10, y=200)

# boton para promediar
bt_convertir = Button(frame_operaciones,text="Promediar", command=promediar)
bt_convertir.place(x=36, y=35, width=100, height=30)
# boton para el indice de masa corporal
bt_convertir = Button(frame_operaciones,text="Calcular", command=IMC)
bt_convertir.place(x=172, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=308, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(frame_operaciones,text="Salir", command=salir)
bt_salir.place(x=444, y=35, width=100, height=30)

#--------------------------------
# frame resultados
#--------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=580, height=280)
frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="white", fg="black", font=("Courier", 12))
t_resultados.place(x=10,y=10,width=265,height=260)

t_resultados2 = Text(frame_resultados)
t_resultados2.config(bg="white", fg="black", font=("Courier", 12))
t_resultados2.place(x=302,y=10,width=265,height=260)

# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()