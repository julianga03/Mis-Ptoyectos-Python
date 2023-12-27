from selenium import webdriver

# Crear una instancia de WebDriver (en este caso, Chrome)
driver = webdriver.Chrome()

# Obtener la versión del controlador
driver_version = driver.capabilities['chrome']['chromedriverVersion']

# Imprimir la versión del controlador
print("Versión del controlador de Chrome:", driver_version)

# Cerrar el navegador
driver.quit()
