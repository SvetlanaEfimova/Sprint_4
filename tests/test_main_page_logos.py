import allure

from pages.main_page_logos import MainPageLogoScooter, MainPageLogoYandex


class TestMainPageLogos:

    @allure.title('Этот тест проверяет, что при переходе по логотипу "Самокат" происходит переход на главную страницу')
    def test_scooter_logo_transition(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        scooter_logo = MainPageLogoScooter(driver)
        scooter_logo.click_scooter_logo()
        scooter_logo.wait_for_load_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Этот тест проверяет, что при переходе по логотипу "Яндекс" происходит переход на главную страницу '
                  'яндекса')
    def test_yandex_logo_transition(self, driver):
        yandex_logo = MainPageLogoYandex(driver)
        yandex_logo.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        yandex_logo.wait_for_load_yandex_logo()
        url = driver.current_url
        assert url == 'https://dzen.ru/?yredirect=true'
