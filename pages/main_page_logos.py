from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPageLogoScooter:
    _scooter_logo = [By.XPATH, "//*/img[@alt = 'Scooter']"]

    def __init__(self, driver):
        self.driver = driver

    def click_scooter_logo(self):
        self.driver.find_element(*self._scooter_logo).click()

    def wait_for_load_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(self._scooter_logo))


class MainPageLogoYandex:
    _yandex_logo = [By.XPATH, "//*/img[@alt = 'Yandex']"]
    _find_button = [By.XPATH, "*//button[text() = 'Найти']"]

    def __init__(self, driver):
        self.driver = driver

    def click_yandex_logo(self):
        self.driver.find_element(*self._yandex_logo).click()

    def wait_for_load_yandex_logo(self):  # ожидание кликабельности кнопки "Найти" в поисковой строке яндекса
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self._find_button))
