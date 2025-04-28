import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.scooter_main)
    yield driver
    driver.quit()


