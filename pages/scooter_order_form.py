import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class OrderFormInHeader:
    _button_order_in_header = [By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text() = 'Заказать']"]
    _button_order_in_body = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']"]
    _button_next = [By.XPATH, "//button[text() = 'Далее']"]
    _field_name = [By.XPATH, "//input[@placeholder = '* Имя']"]
    _field_last_name = [By.XPATH, "//input[@placeholder = '* Фамилия']"]
    _field_address = [By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"]
    _field_metro_station = [By.XPATH, "//input[@placeholder = '* Станция метро']"]
    _field_phone = [By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    _station_metro = "//div[text() = '%s']"
    _text_about_rent = [By.XPATH, "//div[text() = 'Про аренду']"]
    _field_date = [By.XPATH, "//*/input[@placeholder = '* Когда привезти самокат']"]
    _field_rental_period = [By.XPATH, "//*/div[@class = 'Dropdown-control']"]
    _rental_period = "//*/div[text() = '%s']"
    _scooter_color = [By.XPATH, "//*[@id = '%s']"]
    _field_comment_for_the_courier = [By.XPATH, "//input[@placeholder = 'Комментарий для курьера']"]
    _order_button_in_the_form = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text() = 'Заказать']"]
    _order_confirmation_button = [By.XPATH, "//button[text() = 'Да']"]
    _the_order_has_been_placed = [By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"]

    def __init__(self, driver):
        self.driver = driver

    def click_button_order_in_header(self):
        self.driver.find_element(*self._button_order_in_header).click()

    def click_button_order_in_body(self):
        self.driver.find_element(*self._button_order_in_body).click()

    def wait_for_load_button_next(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(self._button_next))

    def enter_a_name(self, name):
        self.driver.find_element(*self._field_name).send_keys(name)

    def enter_a_last_name(self, lastname):
        self.driver.find_element(*self._field_last_name).send_keys(lastname)

    def enter_the_address(self, address):
        self.driver.find_element(*self._field_address).send_keys(address)

    def click_field_metro_station(self):
        self.driver.find_element(*self._field_metro_station).click()

    def click_metro_station(self, metro):
        WebDriverWait(self.driver, 3).until(
            ec.visibility_of_element_located([By.XPATH, self._station_metro % metro])).click()

    def enter_the_phone(self, phone):
        self.driver.find_element(*self._field_phone).send_keys(phone)

    def click_button_next(self):
        self.driver.find_element(*self._button_next).click()

    def wait_for_load_text_rent(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(self._text_about_rent))

    def get_the_text_about_rent(self):
        return self.driver.find_element(*self._text_about_rent).text

    def get_the_order_has_been_placed_text(self):
        return self.driver.find_element(*self._the_order_has_been_placed).text

    def click_field_date(self):
        self.driver.find_element(*self._field_date).click()

    def input_field_date(self, date):
        self.driver.find_element(*self._field_date).send_keys(date, Keys.ENTER)

    def click_field_rental_period(self):
        self.driver.find_element(*self._field_rental_period).click()

    def click_rental_period(self, period):
        WebDriverWait(self.driver, 3).until(
            ec.visibility_of_element_located([By.XPATH, self._rental_period % period])).click()

    def click_scooter_color(self, color):
        locator, xpath = self._scooter_color
        self.driver.find_element(locator, xpath % color).click()

    def enter_comment(self, comment):
        self.driver.find_element(*self._field_comment_for_the_courier).send_keys(comment)

    def click_order_button_in_the_form(self):
        self.driver.find_element(*self._order_button_in_the_form).click()

    def click_order_confirmation_button(self):
        self.driver.find_element(*self._order_confirmation_button).click()

    def wait_for_load_the_order_has_been_placed(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(self._the_order_has_been_placed))

    def registration_with_the_first_data(self, name, lastname, address, metro, phone, date, period, color, comment):
        self.enter_a_name(name)
        self.enter_a_last_name(lastname)
        self.enter_the_address(address)
        self.click_field_metro_station()
        self.click_metro_station(metro)
        self.enter_the_phone(phone)
        self.click_button_next()
        self.wait_for_load_text_rent()
        self.click_field_date()
        self.input_field_date(date)
        self.click_field_rental_period()
        self.click_rental_period(period)
        self.click_scooter_color(color)
        self.enter_comment(comment)
        self.click_order_button_in_the_form()
        self.click_order_confirmation_button()

