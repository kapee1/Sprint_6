import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    page_header = By.XPATH, ".//div[@class='Order_Header__BZXOb']"

    successful_order_header = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"

    first_name_field = By.XPATH, ".//input[@placeholder='* Имя']"
    last_name_field = By.XPATH, ".//input[@placeholder='* Фамилия']"
    address_field = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    phone_field = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    metro_station_field = By.XPATH, ".//input[@placeholder='* Станция метро']"
    metro_station_dropdown_list_item = By.XPATH, ".//div/ul/li[@data-index = '1']"
    start_rent_day_field = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    day_in_calender_item = By.XPATH, ".//div[text() = '15']"
    rent_duration_field = By.XPATH, ".//div[text() = '* Срок аренды']"
    duration_list_item = By.XPATH, ".//div[text() = 'сутки']"
    color_grey_in_colors_field = By.XPATH, ".//label/input[@id = 'grey']"
    color_black_in_colors_field = By.XPATH, ".//label/input[@id = 'black']"
    order_button = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM'][text() = 'Заказать']"
    yes_confirmation_button = By.XPATH, ".//button[text() = 'Да']"
    no_confirmation_button = By.XPATH, ".//button[text() = 'Нет']"
    check_order_status = By.XPATH, ".//button[text() = 'Посмотреть статус']"
    next_button = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"

    scooter_header_logo = By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']"
    yandex_header_logo = By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']"

    @allure.step('Заполняем страницу с личными данными')
    def set_personal_order_details(self, first_name, last_name, address, phone):
        self.wait_and_find_element(self.first_name_field).send_keys(first_name)
        self.wait_and_find_element(self.last_name_field).send_keys(last_name)
        self.wait_and_find_element(self.address_field).send_keys(address)
        self.wait_and_find_element(self.phone_field).send_keys(phone)

    @allure.step('Заполняем поле станциия метро')
    def set_metro_station_input(self):
        metro_station_input = self.wait_and_find_element(self.metro_station_field)
        metro_station_input.click()
        metro_station_in_list = self.wait_and_find_element(self.metro_station_dropdown_list_item)
        metro_station_in_list.click()

    @allure.step('Нажимаем кнопку далее')
    def click_next_button(self):
        button = self.wait_and_find_element(self.next_button)
        button.click()

    @allure.step('Заполняем поле "Когда привести самокат"')
    def set_start_day_input(self):
        start_day_input = self.wait_and_find_element(self.start_rent_day_field)
        start_day_input.click()
        self.wait_and_find_element(self.day_in_calender_item).click()

    @allure.step('Заполняем поле срок аренды')
    def rent_duration_input(self):
        rent_duration_input = self.wait_and_find_element(self.rent_duration_field)
        rent_duration_input.click()
        self.wait_and_find_element(self.duration_list_item).click()

    @allure.step('Заполняем поле цвет самоката = серый')
    def color_input_gray(self):
        color = self.wait_and_find_element(self.color_grey_in_colors_field)
        color.click()

    @allure.step('Заполняем поле цвет самоката = черный')
    def color_input_black(self):
        color = self.wait_and_find_element(self.color_black_in_colors_field)
        color.click()

    @allure.step('Заполняем поле цвет самоката = два варианта')
    def color_input_both(self):
        gray_color = self.wait_and_find_element(self.color_grey_in_colors_field)
        gray_color.click()
        black_color = self.wait_and_find_element(self.color_black_in_colors_field)
        black_color.click()

    @allure.step('Нажимаем кнопку заказать после полей ввода')
    def order_button_click(self):
        button = self.wait_and_find_element(self.order_button)
        button.click()

    @allure.step('Подтверждение оформления заказа кнопкой "да" во всплывающем окне')
    def confirmation_button_click(self):
        button = self.wait_and_find_element(self.yes_confirmation_button)
        button.click()





