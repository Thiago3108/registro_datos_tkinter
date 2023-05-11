from tkinter import *
from tkinter import ttk

root = Tk()

frame_operaciones = Frame(root, width=200, height=200)
frame_operaciones.pack()

# crea un objeto Style
style = ttk.Style()

# establece el estilo para los botones
style.configure('Circ.TButton', borderwidth=10, relief='ridge', bordercolor='gray', foreground='black')

# establece los bordes circulares
style.layout('Circ.TButton', [('Button.border', {'border': '10', 'sticky': 'nswe', 'bordercolor': 'gray', 'borderwidth': '10', 'borderradius': '20'}), ('Button.focus', {'border': '1', 'sticky': 'nswe'})])

# crea el botón
bt_convertir = ttk.Button(frame_operaciones, text="Notas", style='Circ.TButton')
bt_convertir.config(bg="goldenrod2", fg="black", font=("MuseJazz Text", 12))
bt_convertir.place(x=36, y=35, width=100, height=30)

root.mainloop()
