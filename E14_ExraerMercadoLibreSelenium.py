from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(chrome_options=opts)

driver.get('https://listado.mercadolibre.com.co/computacion/portatiles-accesorios/portatiles/asus-vivobook-intel-core-i7-portatiles-mas-de-15.6-pulgadas_NoIndex_True')

WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '//h2'))
)

while True:
    links_productos = driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element shops__items-group-details ui-search-link"]')
    links_de_la_pagina = []

    for tag_a in links_productos:
        links_de_la_pagina.append(tag_a.get_attribute("href"))

    for link in links_de_la_pagina:
        try:
            driver.get(link)

            titulo = driver.find_element('xpath', '//h1').text
            Precio = driver.find_element('xpath', '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]').text

            print(titulo)
            print(Precio)

            driver.back() #lleva a la pagina donde estaba antes

            WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@class="ui-search-layout__item shops__layout-item"]'))
            )

        except Exception as e:
            print(e)
            print("Error")
            driver.back()

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="andes-pagination__link shops__pagination-link ui-search-link"]'))
        )
        boton_siguiente = driver.find_element('xpath','//a[@class="andes-pagination__link shops__pagination-link ui-search-link"]')
        boton_siguiente.get_attribute("href")
        driver.get(boton_siguiente.get_attribute("href"))
        print("Cambia Pagina")

    except Exception as e:
        print(e)
        break