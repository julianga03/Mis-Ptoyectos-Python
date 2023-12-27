from tiktokapi import TikTokApi

# Función para descargar el video
def descargar_video(url, guardar_en):
    api = TikTokApi.get_instance()
    try:
        tiktok = api.get_tiktok_by_url(url)
        video_url = tiktok["video"]["downloadAddr"]
        video_path = guardar_en + "/video.mp4"

        response = api.session.get(video_url, stream=True)
        response.raise_for_status()

        with open(video_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print("Video descargado exitosamente:", video_path)
        
    except Exception as e:
        print("Error al descargar el video:", str(e))

# Ejemplo de uso
video_url = "https://vm.tiktok.com/ZM2Qn5La6/"
carpeta_destino = "D:\MisCosas"

descargar_video(video_url, carpeta_destino)
