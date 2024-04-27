import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import Urls


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.scooter_main)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def accept_cookie(driver):
    cookie_button = (By.XPATH, "//*[contains(@class,'App_CookieButton__3cvqF')]")
    driver.find_element(*cookie_button).click()
