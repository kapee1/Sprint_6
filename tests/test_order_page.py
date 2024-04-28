import pytest
from data import Urls, RegistrationData
from conftest import driver, accept_cookie
import allure

from pages.order_page import OrderPage


class TestOrder:
    @allure.title("Оформление заказа")
    @allure.description("todo")
    @pytest.mark.parametrize('first_name, last_name, address, phone', [RegistrationData.registration_data_1,
                                                                       RegistrationData.registration_data_2])
    def test_place_new_order_success(self, driver, accept_cookie, first_name, last_name, phone, address):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.scooter_order)
        order_page.wait_and_find_element(OrderPage.first_name_field)
        order_page.set_personal_order_details(first_name, last_name, address, phone)
        order_page.set_metro_station_input()
        order_page.click_next_button()
        order_page.wait_and_find_element(OrderPage.start_rent_day_field)
        order_page.set_start_day_input()
        order_page.rent_duration_input()
        order_page.color_input_both()
        order_page.order_button_click()
        order_page.confirmation_button_click()

        assert 'Заказ оформлен' in order_page.get_text(order_page.successful_order_header)


class TestRedirect:

    @allure.title("Переход на страницу Дзена")
    @allure.description("После клика на слово Яндекс в хедере со страницы оформления заказа")
    def test_redirect_to_dzen_from_header_logo(self, driver, accept_cookie):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.scooter_order)
        order_page.wait_until_url_changes(Urls.scooter_order)
        order_page.click(OrderPage.yandex_header_logo)
        order_page.switch_driver()
        order_page.wait_until_url_changes(Urls.dzen_redirect)
        assert order_page.get_current_url() == Urls.dzen_redirect

    @allure.title("Переход на главную страницу")
    @allure.description("После клика на лого Самоката со страницы оформления заказа")
    def test_redirect_main_after_click_on_logo(self, driver, accept_cookie):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.scooter_order)
        order_page.wait_until_url_changes(Urls.scooter_order)
        order_page.click(OrderPage.scooter_header_logo)
        order_page.wait_until_url_changes(Urls.scooter_main)
        assert order_page.get_current_url() == Urls.scooter_main
