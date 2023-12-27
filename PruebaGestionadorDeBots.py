import os
import time
import tkinter as tk
from tkinter import filedialog

def ejecutar_script(script_path):
    print(f"Ejecutando script: {script_path}")
    os.system(f"python {script_path}")

def ejecutar_manualmente():
    seleccion = lista_scripts.curselection()
    if seleccion:
        script_seleccionado = lista_scripts.get(seleccion)
        ejecutar_script(script_seleccionado)

def ejecutar_programado(hora, minuto):
    while True:
        ahora = time.localtime()
        if ahora.tm_hour == hora and ahora.tm_min == minuto:
            ejecutar_script(script_a_ejecutar)
            break
        time.sleep(60)  # Esperar un minuto antes de verificar de nuevo

def seleccionar_script():
    ruta_script = filedialog.askopenfilename(filetypes=[("Archivos de Python", "*.py")])
    if ruta_script:
        script_a_ejecutar.set(ruta_script)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Scripts")

# Etiqueta y lista de scripts
etiqueta = tk.Label(ventana, text="Scripts disponibles:")
etiqueta.pack()

lista_scripts = tk.Listbox(ventana, selectmode=tk.SINGLE)
lista_scripts.pack()

# Agregar scripts a la lista (puedes modificar esto según tus necesidades)
lista_scripts.insert(tk.END, "script1.py")
lista_scripts.insert(tk.END, "script2.py")
lista_scripts.insert(tk.END, "script3.py")

# Botón de selección de script
boton_seleccionar = tk.Button(ventana, text="Seleccionar Script", command=seleccionar_script)
boton_seleccionar.pack()

# Script a ejecutar programado
script_a_ejecutar = tk.StringVar()

# Etiqueta y entrada para la hora de ejecución programada
etiqueta_hora = tk.Label(ventana, text="Hora de ejecución (0-23):")
etiqueta_hora.pack()

entrada_hora = tk.Entry(ventana)
entrada_hora.pack()

# Etiqueta y entrada para el minuto de ejecución programada
etiqueta_minuto = tk.Label(ventana, text="Minuto de ejecución (0-59):")
etiqueta_minuto.pack()

entrada_minuto = tk.Entry(ventana)
entrada_minuto.pack()

# Botón de ejecución manual
boton_manual = tk.Button(ventana, text="Ejecutar Manualmente", command=ejecutar_manualmente)
boton_manual.pack()

# Botón de ejecución programada
boton_programar = tk.Button(ventana, text="Programar Ejecución", command=lambda: ejecutar_programado(int(entrada_hora.get()), int(entrada_minuto.get())))
boton_programar.pack()

ventana.mainloop()
