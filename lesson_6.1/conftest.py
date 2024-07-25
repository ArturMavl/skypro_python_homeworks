import pytest
from selenium import webdriver # импорт драйвера для взаимодействия с браузером


@pytest.fixture()
def chrome_browser():
    driver = webdriver.chrome()
    driver.maximize_window()
    yield driver
    driver.quit()