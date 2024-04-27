from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By


class BasePage:

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
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Дождаться смены страницы')
    def wait_until_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))


    @allure.step('Дождаться появления элемента')
    def wait_until_visible(self, element):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))


    @allure.step('Скролл до элемента')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем по элементу с нужным локатором')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step('Переключение драйвера на другую вкладку')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
