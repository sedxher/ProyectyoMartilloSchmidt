import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

modelos = ["Modelo1","Modelo2"]

## FUNCIONES

def plotter():
        # Generar grafica
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 1, 4, 2]
        grafico.plot(x, y)
        canvas.draw()

def abrir_dialogo():
        carpeta = tkinter.filedialog.askdirectory()

def mostrar_ventana():
        tkinter.messagebox.showinfo("Mensaje", "Introduzca un nombre para su proyecto")

def guardar():
        texto_nombre = entrada_nombre_proyecto.get()
        if texto_nombre == '':
            mostrar_ventana()
        else:
            print(texto_nombre)

ventana = tkinter.Tk()
#ventana.geometry('600x400')
ventana.title("USC a partir de Martillo Schmidt")

## MARCO INFORMACION
frame = tkinter.Frame(ventana)
frame.pack()
informacion_modelo =tkinter.LabelFrame(frame, text="Información del modelo")
informacion_modelo.grid(row= 0, column=0, sticky="news", padx=40, pady=20)

# Nombre del proyecto
nombre_proyecto = tkinter.Label(informacion_modelo, text="Nombre del proyecto")
nombre_proyecto.grid(row=0, column=0, columnspan=5)
entrada_nombre_proyecto = tkinter.Entry(informacion_modelo)
entrada_nombre_proyecto.grid(row=1, column=0, columnspan=5)

# Modo
mode_label = tkinter.Label(informacion_modelo, text="Modo")
mode_combobox = ttk.Combobox(informacion_modelo, values=modelos)
mode_label.grid(row=4, column=0)
mode_combobox.grid(row=5, column=0)

# Modelo
model_label = tkinter.Label(informacion_modelo, text="Modelo")
model_combobox = ttk.Combobox(informacion_modelo, values=modelos)
model_label.grid(row=6, column=0)
model_combobox.grid(row=7, column=0)

# Abrir
open_button = tkinter.Button(informacion_modelo, text="Abrir", command=abrir_dialogo)
open_button.grid(row=4, column=2, sticky="news", padx=20, pady=10)

## MARCO FIGURA
figure_frame = tkinter.LabelFrame(frame)
figure_frame.grid(row=1, column=0, sticky="news", padx=20, pady=5)

# Crear figura de Matplotlib
figura = Figure(figsize=(4, 4), dpi=100)
grafico = figura.add_subplot(111)
canvas = FigureCanvasTkAgg(figura, master=figure_frame)
canvas.get_tk_widget().grid(row=0, column=0,rowspan=3, columnspan=3, sticky="news")

## MARCO ACCIONES
buttons_frame = tkinter.LabelFrame(frame)
buttons_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


run_button = tkinter.Button(buttons_frame, text="Calcular", command=plotter)
run_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

save_button = tkinter.Button(buttons_frame, text="Guardar", command=guardar)
save_button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

ventana.mainloop()