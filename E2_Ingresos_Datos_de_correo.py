import time
import traceback
import psutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

URL = 'https://community.cloud.automationanywhere.digital/#/login?'
XPATH_USERNAME = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div/div/div/input"
XPATH_PASSWORD = "//input[@name='password']"
XPATH_LOGIN_BUTTON = "//*[@id]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/div/button"
XPATH_AUTOMATION = "/html/body/div[1]/div[1]/div[2]/div/nav[1]/ol/li[4]/a"
XPATH_BOT_AUTOMATION = "/html/body/div[1]/div[1]/div[4]/div/div[2]/div[2]/div/div[3]/div[3]/div[2]/div/div[4]/div[3]/div/a/span"
XPATH_RUN = "/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div[5]/button/span/span[1]"
XPATH_CLOSE = "/html/body/div[4]/div[1]/div/div/div/div[2]/div/div/button"
XPATH_TITLE = "/html/body/div[4]/div[1]/div/div/div/div[1]/div/header/div/span[2]"

USERNAME = 'juliangalindo3214@gmail.com'
PASSWORD = 'Julian0309/*-'

def main():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    try:
        username_input = wait.until(ec.visibility_of_element_located((By.XPATH, XPATH_USERNAME)))
        password_input = wait.until(ec.visibility_of_element_located((By.XPATH, XPATH_PASSWORD)))
        login_button = wait.until(ec.element_to_be_clickable((By.XPATH, XPATH_LOGIN_BUTTON)))

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        login_button.click()
        time.sleep(2)

        modulo_automation = wait.until(ec.element_to_be_clickable((By.XPATH, XPATH_AUTOMATION)))
        modulo_automation.click()
        time.sleep(2)

        bot_hola_mundo = wait.until(ec.element_to_be_clickable((By.XPATH, XPATH_BOT_AUTOMATION)))
        bot_hola_mundo.click()
        time.sleep(2)

        runear_hola = wait.until(ec.element_to_be_clickable((By.XPATH, XPATH_RUN)))
        runear_hola.click()
        time.sleep(3)
        

        """for process in psutil.process_iter(['name']):
        	if process.info['name'] == 'javaw.exe':
        		# Cerrar el proceso
        		process.kill()
        		
        		time.sleep(10)
        """

        esperar_title = wait.until(ec.presence_of_element_located((By.XPATH, XPATH_TITLE)))
        texto = esperar_title
        print(texto, "Linea 62")

        cerrar_automation = wait.until(ec.element_to_be_clickable((By.XPATH, XPATH_CLOSE)))
        cerrar_automation.click()
        time.sleep(2)

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
    
    finally:
    	driver.quit()
    	     
if __name__ == '__main__':
    main()







