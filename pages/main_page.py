from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPageQuestions:
    _cookie = [By.XPATH, "//*[text() = 'да все привыкли']"]
    _questions_one = [By.XPATH, "//*[text() = 'Сколько это стоит? И как оплатить?']"]
    _questions_two = [By.XPATH, "//*[text() = 'Хочу сразу несколько самокатов! Так можно?']"]
    _questions_three = [By.XPATH, "//*[text() = 'Как рассчитывается время аренды?']"]
    _questions_four = [By.XPATH, "//*[text() = 'Можно ли заказать самокат прямо на сегодня?']"]
    _questions_five = [By.XPATH, "//*[text() = 'Можно ли продлить заказ или вернуть самокат раньше?']"]
    _questions_six = [By.XPATH, "//*[text() = 'Вы привозите зарядку вместе с самокатом?']"]
    _questions_seven = [By.XPATH, "//*[text() = 'Можно ли отменить заказ?']"]
    _questions_eight = [By.XPATH, "//*[text() = 'Я жизу за МКАДом, привезёте?']"]

    def __init__(self, driver):
        print(driver)
        self.driver = driver

    def click_questions_one(self):
        self.driver.find_element(*self._questions_one).click()

    def click_questions_two(self):
        self.driver.find_element(*self._questions_two).click()

    def click_questions_three(self):
        self.driver.find_element(*self._questions_three).click()

    def click_questions_four(self):
        self.driver.find_element(*self._questions_four).click()

    def click_questions_five(self):
        self.driver.find_element(*self._questions_five).click()

    def click_questions_six(self):
        self.driver.find_element(*self._questions_six).click()

    def click_questions_seven(self):
        self.driver.find_element(*self._questions_seven).click()

    def click_questions_eight(self):
        self.driver.find_element(*self._questions_eight).click()


class MainPageAnswers:  # методы класса ожидают появление ответа и получают текст
    the_answer_to_the_first_question = [By.XPATH, "//*[@id='accordion__panel-0']/p"]
    the_answer_to_the_second_question = [By.XPATH, "//*[@id='accordion__panel-1']/p"]
    the_answer_to_the_third_question = [By.XPATH, "//*[@id='accordion__panel-2']/p"]
    the_answer_to_the_fourth_question = [By.XPATH, "//*[@id='accordion__panel-3']/p"]
    the_answer_to_the_fifth_question = [By.XPATH, "//*[@id='accordion__panel-4']/p"]
    the_answer_to_the_sixth_question = [By.XPATH, "//*[@id='accordion__panel-5']/p"]
    the_answer_to_the_seventh_question = [By.XPATH, "//*[@id='accordion__panel-6']/p"]
    the_answer_to_the_eighth_question = [By.XPATH, "//*[@id='accordion__panel-7']/p"]

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_answer_one(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_first_question))

    def wait_for_load_answer_two(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_second_question))

    def wait_for_load_answer_three(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_third_question))

    def wait_for_load_answer_four(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_fourth_question))

    def wait_for_load_answer_five(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_fifth_question))

    def wait_for_load_answer_six(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_sixth_question))

    def wait_for_load_answer_seven(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_seventh_question))

    def wait_for_load_answer_eight(self):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.the_answer_to_the_eighth_question))

    def get_the_text_of_the_first_response(self):
        return self.driver.find_element(*self.the_answer_to_the_first_question).text

    def get_the_text_of_the_second_response(self):
        return self.driver.find_element(*self.the_answer_to_the_second_question).text

    def get_the_text_of_the_third_response(self):
        return self.driver.find_element(*self.the_answer_to_the_third_question).text

    def get_the_text_of_the_fourth_response(self):
        return self.driver.find_element(*self.the_answer_to_the_fourth_question).text

    def get_the_text_of_the_fifth_response(self):
        return self.driver.find_element(*self.the_answer_to_the_fifth_question).text

    def get_the_text_of_the_sixth_response(self):
        return self.driver.find_element(*self.the_answer_to_the_sixth_question).text

    def get_the_text_of_the_seventh_response(self):
        return self.driver.find_element(*self.the_answer_to_the_seventh_question).text

    def get_the_text_of_the_eight_response(self):
        return self.driver.find_element(*self.the_answer_to_the_eighth_question).text
