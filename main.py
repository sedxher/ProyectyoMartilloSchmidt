import os
import tkinter
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from scipy.stats import linregress
import pandas as pd
import ecuaciones_ucs

actual_path = os.path.dirname(os.path.abspath(__file__))

modes = ["Rebote a USC práctico","Comparador USC práctico y teórico"]
models = ["Deere & Miller (1966)","Aufmuth (1973)","Yasar & Erdogan (2004)"]

filename = []

## FUNCIONES
def abrir_dialogo():
    name = filedialog.askopenfilename(initialdir=actual_path)
    filename.append(name)
    return

def plotter():   
    ax.clear()
    if filename == []:
        tkinter.messagebox.showwarning("Mensaje", "Seleccione su archivo .xlsx")
    excel_file = pd.read_excel(filename[0], engine="openpyxl")
    d = excel_file["d (kN/m3)"] * 0.1019717684
    r_l = excel_file["r_l"]
    ucs_dato = excel_file["ucs_dato (MPa)"]
    modo_seleccionado = mode_combobox.get()
    modelo_seleccionado = model_combobox.get()
    if modelo_seleccionado == models[0]:
        ucs_reb = ecuaciones_ucs.deeremillerusc(r_l, d)
    elif modelo_seleccionado == models[1]:
        ucs_reb = ecuaciones_ucs.aufmuthusc(r_l, d)
    elif modelo_seleccionado == models[2]:
        ucs_reb = ecuaciones_ucs.yasarerdoganusc(r_l, d)
    else:
        tkinter.messagebox.showwarning("Mensaje", "Seleccione un modelo de correlación")
        print("Seleccione un modelo de correlación")
    if modo_seleccionado == modes[0]:
        xx = np.array(r_l)
        ax.set_xlabel("Número de rebotes")
    elif modo_seleccionado == modes[1]:
        xx = np.array(ucs_dato)
        ax.set_xlabel("UCS Real")
    else:
        tkinter.messagebox.showwarning("Mensaje", "Seleccione un modo de ejecución")
        print("Seleccione un modo de ejecución")
    yy = np.array(ucs_reb)
    slope, intercept, r_value, p_value, std_err = linregress(xx, yy)
    ax.plot(xx, yy, '.', label='Mediciones')
    ax.plot(xx, intercept + slope * xx, 'r', label='Ajuste lineal')
    model_name = f'Modelo de {modelo_seleccionado}'
    ax.text(0.03, 0.95, model_name, transform=ax.transAxes)
    eqn = f'y = {round(slope, 4)}x + {round(intercept, 4)}'
    r2 = f'R\u00b2 = {round(r_value**2, 4)}'
    ax.text(0.03, 0.9, eqn, transform=ax.transAxes)
    ax.text(0.03, 0.85, r2, transform=ax.transAxes)
    ax.legend(loc='lower right')
    ax.set_ylabel("UCS Aproximado [MPa]")
    canvas.draw()

def guardar():
    texto_nombre = name_entry.get()
    if texto_nombre == '':
        tkinter.messagebox.showwarning("Mensaje", "Introduzca un nombre para su proyecto")
    else:
        i = 0
        while os.path.exists('{}{:d}.png'.format(texto_nombre, i)):
            i += 1
        fig.savefig('{}{:d}.png'.format(texto_nombre, i))
    return

ventana = tkinter.Tk()
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
model_combobox = ttk.Combobox(info_frame, values=models)
model_label.grid(row=6, column=0)
model_combobox.grid(row=6, column=1)

# Abrir
open_button = tkinter.Button(info_frame, text="Abrir", command=abrir_dialogo)
open_button.grid(row=5, column=7, sticky='E')

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