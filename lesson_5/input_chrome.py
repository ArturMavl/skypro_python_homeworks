from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servChrom = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service = servChrom)

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Нашли элемент поля ввода и записали в переменную
input = driver.find_element(By.TAG_NAME, "Input")

№ Ввод 1000
input.send_keys("1000")
sleep(2)

# Очистили поле
input.clear()
sleep(2)

№ Ввод 999
input.send_keys("999")
sleep(2)