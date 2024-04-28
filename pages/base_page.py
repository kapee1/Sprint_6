from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By


class BasePage:

    cookie_button = (By.XPATH, "//*[contains(@class,'App_CookieButton__3cvqF')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Найти и дождаться появляения элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти элемент и получить текст')
    def get_text(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step('Дождаться смены страницы')
    def wait_until_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Скролл до элемента')
    def scroll(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        self.wait_and_find_element(locator).click()

    @allure.step('Переключение драйвера на другую вкладку')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Кликнуть по кнопке принятия куки')
    def click_to_accept_cookie(self):
        self.click(self.cookie_button)

