import os
import os

def combinar_archivos_txt(entrada_folder, salida_folder, nombre_salida):
    # Obtener la lista de archivos en la carpeta de entrada
    lista_archivos = [f for f in os.listdir(entrada_folder) if f.endswith('.txt')]

    # Verificar si hay archivos para combinar
    if not lista_archivos:
        print("No hay archivos para combinar.")
        return

    # Crear el path completo para el archivo de salida
    path_salida = os.path.join(salida_folder, nombre_salida)

    # Abrir el archivo de salida en modo de escritura, especificando el conjunto de caracteres UTF-8
    with open(path_salida, 'w', encoding='utf-8') as archivo_salida:
        # Iterar sobre la lista de archivos de entrada
        for nombre_archivo in lista_archivos:
            # Crear el path completo para el archivo de entrada
            path_entrada = os.path.join(entrada_folder, nombre_archivo)

            # Abrir el archivo de entrada en modo de lectura, especificando el conjunto de caracteres UTF-8
            with open(path_entrada, 'r', encoding='utf-8') as archivo_entrada:
                # Leer el contenido del archivo de entrada y escribirlo en el archivo de salida
                contenido = archivo_entrada.read()
                archivo_salida.write(contenido)

    print(f"Archivos combinados en {path_salida}")

# Especifica las carpetas de entrada y salida, y el nombre del archivo de salida
carpeta_entrada = r'C:\Users\julia\OneDrive\Desktop\inputs'
carpeta_salida = r'C:\Users\julia\Downloads'
nombre_archivo_salida = 'archivo_combinado.txt'

# Llama a la función para combinar archivos
combinar_archivos_txt(carpeta_entrada, carpeta_salida, nombre_archivo_salida)

