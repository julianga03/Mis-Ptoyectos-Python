# Importar el módulo tkinter
import tkinter as tk
# Importar el módulo ttk para usar widgets temáticos
from tkinter import ttk

# Crear una ventana principal
window = tk.Tk()
# Establecer el título de la ventana
window.title("Gestion De Bots")
# Establecer el tamaño mínimo de la ventana
window.minsize(400, 300)

# Crear un marco superior para contener los widgets
top_frame = tk.Frame(window)
# Empaquetar el marco superior en la parte superior de la ventana
top_frame.pack(side=tk.TOP, fill=tk.X)

# Crear un widget Label para mostrar el título de la interfaz
title_label = tk.Label(top_frame, text="Gestion De Bots", font=("Arial", 16))
# Empaquetar el widget Label en el centro del marco superior
title_label.pack(side=tk.TOP, anchor=tk.CENTER, pady=10)

# Crear un widget Label para mostrar el indicador de estado general
status_label = tk.Label(top_frame, text="Estado General:", font=("Arial", 12))
# Empaquetar el widget Label en la izquierda del marco superior
status_label.pack(side=tk.LEFT, anchor=tk.W, padx=10)

# Crear un widget Button para mostrar el icono de verificación verde
green_button = tk.Button(top_frame, text="✔", fg="green", font=("Arial", 12))
# Empaquetar el widget Button en la derecha del marco superior
green_button.pack(side=tk.RIGHT, anchor=tk.E, padx=10)

# Crear un widget Button para mostrar el icono de cruz roja
red_button = tk.Button(top_frame, text="✘", fg="red", font=("Arial", 12))
# Empaquetar el widget Button en la derecha del marco superior
red_button.pack(side=tk.RIGHT, anchor=tk.E, padx=10)

# Crear un marco inferior para contener los widgets
bottom_frame = tk.Frame(window)
# Empaquetar el marco inferior en la parte inferior de la ventana
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Crear una lista de nombres de archivos ejecutables
executables = ["bot_1.exe", "bot_2.exe", "bot_3.exe"]
# Crear una lista de estados de archivos ejecutables
states = ["En curso", "No iniciado", "Fallido"]
# Crear una lista de colores de estados
colors = ["green", "gray", "red"]

# Recorrer la lista de archivos ejecutables
for i in range(len(executables)):
    # Crear un marco interno para contener los widgets relacionados con cada archivo ejecutable
    inner_frame = tk.Frame(bottom_frame)
    # Empaquetar el marco interno en la parte superior del marco inferior
    inner_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

    # Crear un widget Label para mostrar el nombre del archivo ejecutable
    executable_label = tk.Label(inner_frame, text=executables[i], font=("Arial", 12))
    # Empaquetar el widget Label en la izquierda del marco interno
    executable_label.pack(side=tk.LEFT, anchor=tk.W, padx=10)

    # Crear un widget Label para mostrar el estado del archivo ejecutable
    state_label = tk.Label(inner_frame, text=states[i], font=("Arial", 12), fg=colors[i])
    # Empaquetar el widget Label en la derecha del marco interno
    state_label.pack(side=tk.RIGHT, anchor=tk.E, padx=10)

    # Crear un widget Progressbar para mostrar el progreso del archivo ejecutable
    progressbar = ttk.Progressbar(inner_frame, orient=tk.HORIZONTAL, length=200, mode="determinate")
    # Establecer el valor del widget Progressbar según el índice del archivo ejecutable
    progressbar["value"] = (i + 1) * 25
    # Empaquetar el widget Progressbar en el centro del marco interno
    progressbar.pack(side=tk.RIGHT, anchor=tk.E, padx=10)

# Iniciar el bucle principal de la ventana
window.mainloop()
