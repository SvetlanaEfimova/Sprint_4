import allure
from pages.main_page import MainPageQuestions, MainPageAnswers


class TestMainPage:

    @allure.title('Этот тест проверяет корректный ответ на первый вопрос в блоке: "Вопросы о важном"')
    def test_questions_one(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_one()
        answer_page.wait_for_load_answer_one()
        answer_from_header = answer_page.get_the_text_of_the_first_response()
        assert answer_from_header == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Этот тест проверяет корректный ответ на второй вопрос в блоке: "Вопросы о важном"')
    def test_questions_two(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_two()
        answer_page.wait_for_load_answer_two()
        answer_from_header = answer_page.get_the_text_of_the_second_response()
        assert answer_from_header == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с ' \
                                     'друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Этот тест проверяет корректный ответ на третий вопрос в блоке: "Вопросы о важном"')
    def test_questions_three(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_three()
        answer_page.wait_for_load_answer_three()
        answer_from_header = answer_page.get_the_text_of_the_third_response()
        assert answer_from_header == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение ' \
                                     'дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ ' \
                                     'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 ' \
                                     'мая в 20:30.'

    @allure.title('Этот тест проверяет корректный ответ на четвертый вопрос в блоке: "Вопросы о важном"')
    def test_questions_fourth(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_four()
        answer_page.wait_for_load_answer_four()
        answer_from_header = answer_page.get_the_text_of_the_fourth_response()
        assert answer_from_header == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Этот тест проверяет корректный ответ на пятый вопрос в блоке: "Вопросы о важном"')
    def test_questions_fifth(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_five()
        answer_page.wait_for_load_answer_five()
        answer_from_header = answer_page.get_the_text_of_the_fifth_response()
        assert answer_from_header == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по ' \
                                     'красивому номеру 1010.'

    @allure.title('Этот тест проверяет корректный ответ на шестой вопрос в блоке: "Вопросы о важном"')
    def test_questions_sixth(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_six()
        answer_page.wait_for_load_answer_six()
        answer_from_header = answer_page.get_the_text_of_the_sixth_response()
        assert answer_from_header == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже ' \
                                     'если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Этот тест проверяет корректный ответ на седьмой вопрос в блоке: "Вопросы о важном"')
    def test_questions_seventh(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_seven()
        answer_page.wait_for_load_answer_seven()
        answer_from_header = answer_page.get_the_text_of_the_seventh_response()
        assert answer_from_header == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не ' \
                                     'попросим. Все же свои.'

    @allure.title('Этот тест проверяет корректный ответ на восьмой вопрос в блоке: "Вопросы о важном"')
    def test_questions_eighth(self, driver):
        answer_page = MainPageAnswers(driver)
        questions_about_important = MainPageQuestions(driver)
        questions_about_important.click_questions_eight()
        answer_page.wait_for_load_answer_eight()
        answer_from_header = answer_page.get_the_text_of_the_eight_response()
        assert answer_from_header == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


