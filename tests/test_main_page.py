import pytest
from data import Urls
import allure
from pages.main_page import MainPage
from conftest import driver


class TestAnswers:

    @allure.title("Блок вопросов и ответов")
    @allure.description("Кликаем по полю вопроса должен отобразить ответ")
    @pytest.mark.parametrize('question, answer, answer_text', MainPage.list_of_questions)
    def test_questions_opens_successful(self, driver, question, answer, answer_text):
        main_page = MainPage(driver)
        main_page.click_to_accept_cookie()
        main_page.scroll(question)
        main_page.wait_and_find_element(question)
        main_page.click(question)
        assert main_page.get_text(answer) == answer_text


class TestOrderButtons:

    @allure.title("Кнопка заказать в хедере")
    @allure.description("Клик по кнопке должен открывать страницу оформления заказа")
    def test_order_button_in_header_opens_order_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_accept_cookie()
        main_page.wait_and_find_element(MainPage.order_button_in_header)
        main_page.click_order_button_in_header()
        assert main_page.get_current_url() == Urls.scooter_order

    @allure.title("Кнопка заказать в середине страницы")
    @allure.description("Клик по кнопке должен открывать страницу оформления заказа")
    def test_order_button_in_middle_opens_order_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_accept_cookie()
        main_page.scroll(MainPage.order_button_in_middle)
        main_page.click_order_button_in_middle()
        assert main_page.get_current_url() == Urls.scooter_order
