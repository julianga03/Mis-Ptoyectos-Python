import os
import sys
import time
from pywinauto import Application

# Esperar un momento antes de comenzar la automatización
time.sleep(5)

# Ruta del archivo ejecutable de Microsoft Word
word_path = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'

# Crear una instancia de la aplicación Microsoft Word
word_app = Application(backend='uia').start(word_path)

# Esperar a que la aplicación se abra completamente
word_app.wait_cpu_usage_lower(threshold=1, timeout=10, usage_interval=1)

# Obtener la ventana principal de Word
main_window = word_app.window(title_re='.*Word')

# Imprimir los identificadores de control en la consola
#main_window.print_control_identifiers()

#Imprimir los identificadores de control en un txt__________
# Crear un archivo de texto para guardar la salida
output_file = 'C:\AutomationPy\identificadores.txt'

# Redirigir la salida estándar a un archivo
with open(output_file, 'w') as file:
    sys.stdout = file
    main_window.print_control_identifiers()

# Restaurar la salida estándar
sys.stdout = sys.__stdout__

# Cerrar Microsoft Word
main_window.close()
