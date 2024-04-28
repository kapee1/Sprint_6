import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data import AnswersText


class MainPage(BasePage):

    question_1 = By.XPATH, ".//div[@id='accordion__heading-0']"
    answer_1 = By.XPATH, ".//div[@id='accordion__panel-0']"

    question_2 = By.XPATH, ".//div[@id='accordion__heading-1']"
    answer_2 = By.XPATH, ".//div[@id='accordion__panel-1']"

    question_3 = By.XPATH, ".//div[@id='accordion__heading-2']"
    answer_3 = By.XPATH, ".//div[@id='accordion__panel-2']"

    question_4 = By.XPATH, ".//div[@id='accordion__heading-3']"
    answer_4 = By.XPATH, ".//div[@id='accordion__panel-3']"

    question_5 = By.XPATH, ".//div[@id='accordion__heading-4']"
    answer_5 = By.XPATH, ".//div[@id='accordion__panel-4']"

    question_6 = By.XPATH, ".//div[@id='accordion__heading-5']"
    answer_6 = By.XPATH, ".//div[@id='accordion__panel-5']"

    question_7 = By.XPATH, ".//div[@id='accordion__heading-6']"
    answer_7 = By.XPATH, ".//div[@id='accordion__panel-6']"

    question_8 = By.XPATH, ".//div[@id='accordion__heading-7']"
    answer_8 = By.XPATH, ".//div[@id='accordion__panel-7']"

    list_of_questions = [
        [question_1, answer_1, AnswersText.answer_how_much_text],
        [question_2, answer_2, AnswersText.answer_multiple_text],
        [question_3, answer_3, AnswersText.answer_calc_time_text],
        [question_4, answer_4, AnswersText.answer_order_today_text],
        [question_5, answer_5, AnswersText.answer_prolongation_text],
        [question_6, answer_6, AnswersText.answer_charger_text],
        [question_7, answer_7, AnswersText.answer_cancel_text],
        [question_8, answer_8, AnswersText.answer_across_MKAD_text]
    ]

    order_button_in_header = By.XPATH, ".//button[@class = 'Button_Button__ra12g']"
    order_button_in_middle = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']"

    @allure.step('Кликаем на кнопку заказать в хедере')
    def click_order_button_in_header(self):
        self.click(self.order_button_in_header)

    @allure.step('Кликаем на кнопку заказать в середине страницы')
    def click_order_button_in_middle(self):
        self.click(self.order_button_in_middle)








