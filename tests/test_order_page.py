import pytest
from data import Urls, RegistrationData
import allure
from pages.order_page import OrderPage
from conftest import driver


class TestOrder:
    @allure.title("Оформление заказа")
    @allure.description("todo")
    @pytest.mark.parametrize('first_name, last_name, address, phone', [RegistrationData.registration_data_1,
                                                                       RegistrationData.registration_data_2])
    def test_place_new_order_success(self, driver, first_name, last_name, phone, address):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.set_personal_order_details(first_name, last_name, address, phone)
        order_page.set_metro_station_input()
        order_page.click_next_button()
        order_page.set_start_day_input()
        order_page.rent_duration_input()
        order_page.color_input_both()
        order_page.order_button_click()
        order_page.confirmation_button_click()

        assert 'Заказ оформлен' in order_page.get_header_text_from_order_form()


class TestRedirect:

    @allure.title("Переход на страницу Дзена")
    @allure.description("После клика на слово Яндекс в хедере со страницы оформления заказа")
    def test_redirect_to_dzen_from_header_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_yandex_logo()
        order_page.switch_driver()
        order_page.wait_until_url_changes(Urls.dzen_redirect)
        assert order_page.get_current_url() == Urls.dzen_redirect

    @allure.title("Переход на главную страницу")
    @allure.description("После клика на лого Самоката со страницы оформления заказа")
    def test_redirect_main_after_click_on_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_scooters_logo()
        order_page.wait_until_url_changes(Urls.scooter_main)
        assert order_page.get_current_url() == Urls.scooter_main
