import allure
from selenium import webdriver

from pages.navigation_through_logos import ClickOnTheScooterLogo, ClickOnTheYandexLogo


class TestNavigationThroughLogos:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/order')

    @allure.title('Этот тест проверяет, что при переходе по логотипу "Самокат" происходит переход на главную страницу')
    def test_scooter_logo_transition(self):
        scooter_logo = ClickOnTheScooterLogo(self.driver)
        scooter_logo.click_scooter_logo()
        scooter_logo.wait_for_load_scooter_logo()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Этот тест проверяет, что при переходе по логотипу "Яндекс" происходит переход на главную страницу '
                  'яндекса')
    def test_yandex_logo_transition(self):
        yandex_logo = ClickOnTheYandexLogo(self.driver)
        yandex_logo.click_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[1])
        yandex_logo.wait_for_load_yandex_logo()
        url = self.driver.current_url
        assert url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
