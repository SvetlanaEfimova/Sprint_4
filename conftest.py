import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.find_element(By.XPATH, "//*[text() = 'да все привыкли']").click()
    yield driver
    driver.quit()


