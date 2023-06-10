import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from lxml import html 

XPATHSERIEHISTORICA = '/html/body/div[2]/div[1]/div/div/div[3]/div[6]/main/section/div/section[4]/div/div[1]/div[1]/div[2]/div/ul/li[1]/a'
XPATHTABLA = '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr[3]/td/table'

chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

# Inicializar el driver de Selenium
driver = None
try:
    driver = webdriver.Chrome(options=chrome_options)

    # Esperar a que aparezca un elemento
    wait = WebDriverWait(driver, 20)

    driver.get('https://www.banrep.gov.co/es/estadisticas/trm')

    # Encontrar la tabla en la página web
    xpathserie = wait.until(ec.element_to_be_clickable((By.XPATH, XPATHSERIEHISTORICA)))
    xpathserie.click()
    time.sleep(2)

    element = wait.until(ec.presence_of_element_located((By.XPATH, XPATHTABLA)))
    tabla_element = driver.find_element_by_xpath(XPATHTABLA)
    tabla = tabla_element.get_attribute('innerHTML')

    # Obtener el HTML de la tabla
    tabla_html = tabla
    print(tabla)

    # Leer la tabla con Pandas
    df = pd.read_html(tabla_html)[0]

    # Guardar la tabla en un archivo CSV
    df.to_csv('tabla.csv', index=False)

except Exception as e:
    print("Se produjo una excepción:", e)

finally:
    if driver:
        driver.quit()
