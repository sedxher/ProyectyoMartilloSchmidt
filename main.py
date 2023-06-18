import tkinter
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from scipy.stats import linregress
import pandas as pd

modes = ["Rebote a USC práctico","Comparador USC práctico y teórico"]
modelos = ["Modelo1","Modelo2"]

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 4.8]
filename = ''
## FUNCIONES
def abrir_dialogo():
    filename = filedialog.askopenfilenames()
    print(filename)
    df = pd.read_excel(filename)
    x = df["x"]
    y = df["y"]
    return filename, x, y

def plotter():
    xx = np.array(x)
    yy = np.array(y)
    slope, intercept, r_value, p_value, std_err = linregress(xx, yy)
    ax.plot(xx, yy, '.', label='Data')
    ax.plot(xx, intercept + slope * xx, 'r', label='Fitted line')
    eqn = f'y = {round(slope, 4)}x + {round(intercept, 4)}'
    r2 = f'R\u00b2 = {round(r_value**2, 4)}'
    ax.text(0.05, 0.9, eqn, transform=ax.transAxes)
    ax.text(0.05, 0.85, r2, transform=ax.transAxes)
    ax.legend(loc='lower right')
    canvas.draw()

def mostrar_ventana():
    tkinter.messagebox.showinfo("Mensaje", "Introduzca un nombre para su proyecto")

def guardar():
    texto_nombre = name_entry.get()
    if texto_nombre == '':
        mostrar_ventana()
    else:
        print(texto_nombre)
    return texto_nombre

ventana = tkinter.Tk()
#ventana.geometry('600x400')
ventana.title("USC a partir de Martillo Schmidt")

## MARCO INFORMACION
frame = tkinter.Frame(ventana)
frame.pack()

info_frame =tkinter.LabelFrame(frame)
info_frame.grid(row= 0, column=0, sticky="nsew", padx=20, pady=10)

# Nombre del proyecto
project_name = tkinter.Label(info_frame, text="Nombre del proyecto")
project_name.grid(row=0, column=0)
name_entry = tkinter.Entry(info_frame)
name_entry.grid(row=0, column=1)

# Modo
mode_label = tkinter.Label(info_frame, text="Modo")
mode_combobox = ttk.Combobox(info_frame, values=modes)
mode_label.grid(row=4, column=0)
mode_combobox.grid(row=4, column=1)

# Modelo
model_label = tkinter.Label(info_frame, text="Modelo")
model_combobox = ttk.Combobox(info_frame, values=modelos)
model_label.grid(row=6, column=0)
model_combobox.grid(row=6, column=1)

# Abrir
open_button = tkinter.Button(info_frame, text="Abrir", command=abrir_dialogo)
open_button.grid(row=5, column=4, sticky='E')

## MARCO FIGURA
figure_frame = tkinter.LabelFrame(frame)
figure_frame.grid(row=1, column=0, sticky="news", padx=20, pady=5)

# Crear figura de Matplotlib
fig = Figure(figsize=(4, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=figure_frame)
canvas.get_tk_widget().grid(row=0, column=0, sticky="news")

## MARCO ACCIONES
buttons_frame = tkinter.LabelFrame(frame)
buttons_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


run_button = tkinter.Button(buttons_frame, text="Calcular", command=plotter)
run_button.grid(row=0, column=0, sticky="sw", columnspan=2, padx=10, pady=10)

save_button = tkinter.Button(buttons_frame, text="Guardar", command=guardar)
save_button.grid(row=0, column=3, sticky="se", columnspan=5, padx=10, pady=10)

ventana.mainloop()