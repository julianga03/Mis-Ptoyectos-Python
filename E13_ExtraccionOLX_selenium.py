import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://www.olx.com.co/portatiles-laptops_c1018')
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@class="_2Ks63"]'))
)

#Todos los anuncios en una lista


for i in range(3):
    try:
        boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))#Espera 10 segundos hasta que el elemento exista
        )
        boton.click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@class="_2Ks63"]'))#Espera que se cargue todos los anuncios
        )
    except:
        break

compus = driver.find_elements('xpath', '//li[@data-aut-id="itemBox"]')#find_elements me devuelce un listado de varios elementos

for laptop in compus:
    precio = laptop.find_element('xpath', './/span[@class="_2Ks63"]').text
    descripcion = laptop.find_element('xpath', './/span[@class="_2poNJ"]').text
    print(precio)
    print(descripcion)


