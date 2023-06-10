import pyautogui

def obtener_coordenadas_clic():
    while True:
        x, y = pyautogui.position()
        print(f"Coordenadas: X={x}, Y={y}")

obtener_coordenadas_clic()