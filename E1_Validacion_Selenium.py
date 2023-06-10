from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Drivers_Navegadores\Google Chrome\chromedriver")
driver.get("http://python.org")
driver.close()