import pytest
from page import Pages
from settings import*
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def driver():
    capabilities = {
        'platformName': (CONFIG[platform]['platformName']),
        'platformVersion': (CONFIG[platform]['platformVersion']),
        'deviceName': (CONFIG[platform]['deviceName']),
        'automationName': (CONFIG[platform]['automationName']),
        'appPackage': (CONFIG[platform]['appPackage']),
        'app': (CONFIG[platform]['app']),
        'noReset': (CONFIG[platform]['noReset']),
        'fullReset': (CONFIG[platform]['fullReset'])

    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    yield driver
    driver.quit()


@pytest.fixture(scope="class", autouse=True)
def pages(driver):
    pages = Pages(driver)
    return pages

