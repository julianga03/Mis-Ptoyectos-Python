import tkinter as tk
from tkinter import ttk
import pandas as pd
from datetime import date

class Registro():
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de Clientes")

        #Variables para almacenar los datos del formulario
        self.fecha = tk.StringVar(value=date.today().strftime('%d-%m-%Y'))
        self.nombre_completo = tk.StringVar()
        self.celular = tk.StringVar()
        self.nombre_empresa = tk.StringVar()

        #Etiquetas y entradas del formulario
        fecha_label = ttk.Label(self.master, text="Fecha:")
        fecha_label.grid(column=0, row=0, padx=5, pady=5)
        fecha_entry = ttk.Entry(self.master, textvariable=self.fecha, state='readonly')
        fecha_entry.grid(column=1, row=0, padx=5, pady=5)

        nombre_label = ttk.Label(self.master, text="Nombre Completo:")
        nombre_label.grid(column=0, row=1, padx=5, pady=5)
        nombre_entry = ttk.Entry(self.master, textvariable=self.nombre_completo)
        nombre_entry.grid(column=1, row=1, padx=5, pady=5)

        celular_label = ttk.Label(self.master, text="Celular:")
        celular_label.grid(column=0, row=2, padx=5, pady=5)
        celular_entry = ttk.Entry(self.master, textvariable=self.celular)
        celular_entry.grid(column=1, row=2, padx=5, pady=5)

        empresa_label = ttk.Label(self.master, text="Nombre Empresa:")
        empresa_label.grid(column=0, row=3, padx=5, pady=5)
        empresa_entry = ttk.Entry(self.master, textvariable=self.nombre_empresa)
        empresa_entry.grid(column=1, row=3, padx=5, pady=5)

        #Botones
        registrar_button = ttk.Button(self.master, text="Registrar", command=self.registrar)
        registrar_button.grid(column=0, row=4, padx=5, pady=5)

        editar_button = ttk.Button(self.master, text="Editar", command=self.editar)
        editar_button.grid(column=1, row=4, padx=5, pady=5)

        eliminar_button = ttk.Button(self.master, text="Eliminar", command=self.eliminar)
        eliminar_button.grid(column=2, row=4, padx=5, pady=5)

        descargar_button = ttk.Button(self.master, text="Descargar Excel", command=self.descargar_excel)
        descargar_button.grid(column=1, row=5, padx=5, pady=5)

        #Tabla
        self.tree = ttk.Treeview(self.master, columns=("fecha", "nombre", "celular", "empresa"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("nombre", text="Nombre Completo")
        self.tree.heading("celular", text="Celular")
        self.tree.heading("empresa", text="Nombre Empresa")
        self.tree.grid(column=0, row=6, columnspan=3, padx=5, pady=5)

    #Función para registrar los datos en la tabla
    def registrar(self):
        #Obtener el último ID registrado
        if self.tree.get_children():
            last_id = int(self.tree.get_children()[-1][1:])
        else:
            last_id = 0
        

        #Agregar los datos del formulario a la tabla
        self.tree.insert("", "end", f"item{last_id + 1}", text=f"{last_id + 1}",
                         values=(self.fecha.get(), self.nombre_completo.get(),
                                 self.celular.get(), self.nombre_empresa.get()))

        #Limpiar los campos del formulario
        self.fecha.set(date.today().strftime('%d-%m-%Y'))
        self.nombre_completo.set("")
        self.celular.set("")
        self.nombre_empresa.set("")

    #Función para editar los datos en la tabla
    def editar(self):
        #Obtener el item seleccionado en la tabla
        item = self.tree.selection()[0]

        #Obtener los nuevos datos del formulario
        fecha = self.fecha.get()
        nombre_completo = self.nombre_completo.get()
        celular = self.celular.get()
        nombre_empresa = self.nombre_empresa.get()

        #Actualizar los valores del item seleccionado
        self.tree.item(item, values=(fecha, nombre_completo, celular, nombre_empresa))

        #Limpiar los campos del formulario
        self.fecha.set(date.today().strftime('%d-%m-%Y'))
        self.nombre_completo.set("")
        self.celular.set("")
        self.nombre_empresa.set("")

    #Función para eliminar un item de la tabla
    def eliminar(self):
        #Obtener el item seleccionado en la tabla
        item = self.tree.selection()[0]

        #Eliminar el item seleccionado
        self.tree.delete(item)

    #Función para descargar los datos de la tabla en un archivo de Excel
    def descargar_excel(self):
        #Crear un DataFrame con los datos de la tabla
        data = []
        for child in self.tree.get_children():
            values = self.tree.item(child)["values"]
            data.append(values)
        df = pd.DataFrame(data, columns=["Fecha", "Nombre Completo", "Celular", "Nombre Empresa"])

        #Guardar el DataFrame en un archivo de Excel
        df.to_excel("registro_clientes.xlsx", index=False)

#Crear la ventana de la aplicación
root = tk.Tk()
app = Registro(root)
root.mainloop()




