from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

servFF = FirefoxService(GeckoDriverManager().install())
driver = webdriver.firefox(service = servFF)

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/login")

# Нашли элемент поля ввода и записали в переменную
username = driver.find_element(By.ID, "username")

# Ввод tomsmith
username.send_keys("tomsmith")
sleep(3)

# Нашли элемент поля ввода и записали в переменную
password = driver.find_element(By.ID, "password")

# Ввод SuperSecretPassword!
password.send_keys("SuperSecretPassword!")
sleep(3)

button = driver.find_element(By.CSS_SELECTOR, "radius")
button.click()
sleep(3)