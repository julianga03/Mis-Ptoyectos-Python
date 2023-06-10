from pytube import YouTube
import requests

def descargar_video(url, ruta_destino):
    try:
        # Crear objeto YouTube
        video = YouTube(url)

        # Obtener la mejor resolución disponible
        video_stream = video.streams.get_highest_resolution()

        # Obtener el tamaño total del archivo
        response = requests.get(video_stream.url, stream=True)
        total_size = int(response.headers.get("Content-Length"))

        # Descargar el video en la ruta especificada
        with open(ruta_destino, "wb") as file:
            bytes_descargados = 0
            chunk_size = 4096

            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
                bytes_descargados += len(chunk)

                # Calcular el progreso de descarga
                progreso = (bytes_descargados / total_size) * 100

                # Mostrar el progreso actual
                print(f"Progreso de descarga: {progreso:.2f}%")

        print("Video descargado correctamente.")
    except Exception as e:
        print("Error al descargar el video:", str(e))

# URL del video de YouTube que deseas descargar
url_video = "https://www.youtube.com/watch?v=HiXLkL42tMU"

# Ruta de destino donde se guardará el video descargado
ruta_destino = "D:\PyUniversity\Git y Github - Curso Práctico de Git y Github Desde Cero.mp4"

# Llamar a la función para descargar el video
descargar_video(url_video, ruta_destino)
