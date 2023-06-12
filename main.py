import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class InterfazGrafica:
    def __init__(self, master):
        self.master = master
        master.title("UCS a partir de Schmidt")
        
        # Crear entrada de texto en la parte superior
        self.entrada = tk.Entry(master)
        self.entrada.grid(column=0, row=0)

        # Crear menú desplegable
        self.menu_desplegable = tk.Menubutton(master, text="Opciones")
        self.menu_desplegable.menu = tk.Menu(self.menu_desplegable, tearoff=0)
        self.menu_desplegable["menu"] = self.menu_desplegable.menu
        self.menu_desplegable.menu.add_command(label="Opción 1", command=self.opcion1)
        self.menu_desplegable.menu.add_command(label="Opción 2", command=self.opcion2)
        self.menu_desplegable.menu.add_command(label="Opción 3", command=self.opcion3)
        self.menu_desplegable.grid(column=1, row=1)

        # Crear botones en la parte superior
        self.button1 = tk.Button(master, text="Archivo", command=self.abrir_dialogo)
        self.button1.grid(column=0, row=1)
        self.button2 = tk.Button(master, text="Calcular", command=self.plot_grafico)
        self.button2.grid(column=0, row=2)

        # Crear figura de Matplotlib
        self.figura = Figure(figsize=(5, 5), dpi=100)
        self.grafico = self.figura.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figura, master=master)
        self.canvas.get_tk_widget().grid(column=2, row=2)
        
        # Crear botones en la parte superior
        self.button3 = tk.Button(master, text="Guardar", command=self.guardar)
        self.button3.grid(column=3, row=3)

    def plot_grafico(self):
        # Generar grafica
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 1, 4, 2]
        self.grafico.plot(x, y)
        self.canvas.draw()

    def limpiar_grafico(self):
        # Limpiar grafico de Matplotlib
        self.grafico.clear()
        self.canvas.draw()
        
    def opcion1(self):
        self.menu_desplegable.config(text="Modelo 1")

    def opcion2(self):
        self.menu_desplegable.config(text="Modelo 2")

    def opcion3(self):
        self.menu_desplegable.config(text="Modelo 3")
        
    def abrir_dialogo(self):
        # Abrir el diálogo de selección de archivo
        carpeta = tk.filedialog.askdirectory()
    
    def guardar(self):
        texto_nombre = self.entrada.get()
        if texto_nombre == '':
            self.mostrar_ventana()
        else:
            print(texto_nombre)
            
    def mostrar_ventana(self):
        # Mostrar un mensaje en la ventana emergente
        tk.messagebox.showinfo("Mensaje", "Introduzca un nombre para su proyecto")

root = tk.Tk()
mi_interfaz = InterfazGrafica(root)
root.mainloop()
