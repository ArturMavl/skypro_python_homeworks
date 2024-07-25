from selenium.webdriver.common.by import By
from configuration import *


def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)
    chrome_browser.find_element(by.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(by.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(by.ID, "login-button").click()
    chrome_browser.find_element(by.ID, "add-to-card-sauce-labs-backpack").click()
    chrome_browser.find_element(by.ID, "add-to-card-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(by.ID, "add-to-card-sauce-labs-onesie").click()
    chrome_browser.find_element(by.ID, "shopping_cart_container").click()
    chrome_browser.find_element(by.ID, "checkout").click()
    chrome_browser.find_element(by.ID, "first-name").send_keys("Artur")
    chrome_browser.find_element(by.ID, "last-name").send_keys("Mavlikaev")
    chrome_browser.find_element(by.ID, "postal-code").send_keys("620000")
    chrome_browser.find_element(by.ID, "continue").click()
    total_price = chrome_browser.find_element(By.CLASS_NAME, 'sumary_total_label')
    total = total_price.text.strip().replace("Total: $", "")

    expected_total "58.29"
    assert total == expected_total # проверяем что итоговая сумма равна 58.29%
    print(f"Итоговая сумма равна ${total}") # выводим сообщение в случае успешного выполнения