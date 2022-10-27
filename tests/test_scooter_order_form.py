import allure
import pytest
from pages.scooter_order_form import OrderFormInHeader


class TestScooterOrderFormInHeader:

    @pytest.mark.parametrize('name,lastname,address,metro,phone,date,period,color,comment',
                             [('Светлана', 'Ефимова', 'Ленина, 45', 'Бульвар Рокоссовского', '89089746574',
                               '30.12.2022', 'сутки', 'black', 'Комментарий'),
                              ('Вася', 'Пупкин', 'Нескучная, 3', 'Динамо', '89089486574',
                               '31.10.2022', 'двое суток', 'grey', 'Комментарий два')])
    @allure.title('Тест проверяет оформление заказа по кнопке вверху страницы с 2 наборами данных')
    def test_login(self, driver, name, lastname, address, metro, phone, date, period, color, comment):
        order_form_in_header = OrderFormInHeader(driver)
        order_form_in_header.click_button_order_in_header()
        order_form_in_header.registration_with_the_first_data(name, lastname, address, metro, phone, date, period,
                                                              color, comment)
        text = order_form_in_header.get_the_order_has_been_placed_text().split()
        assert (text[1]) == 'оформлен'

    @pytest.mark.parametrize('name,lastname,address,metro,phone,date,period,color,comment',
                             [('Стас', 'Басов', 'Фрунзе, 554', 'Лубянка', '+79189746574',
                               '11.11.2022', 'шестеро суток', 'black', 'Без комментариев')])
    @allure.title('Тест проверяет оформление заказа по кнопке в центре страницы с 1 набором данных')
    def test_login_in_body(self, driver, name, lastname, address, metro, phone, date, period, color, comment):
        order_form_in_header = OrderFormInHeader(driver)
        order_form_in_header.click_button_order_in_body()
        order_form_in_header.registration_with_the_first_data(name, lastname, address, metro, phone, date, period,
                                                              color, comment)
        text = order_form_in_header.get_the_order_has_been_placed_text().split()
        assert (text[1]) == 'оформлен'

