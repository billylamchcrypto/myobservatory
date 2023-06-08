from time import sleep
from typing import Optional, Tuple

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *


class PageUtils:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def _wait(self, locator: Tuple[str, str], timeout: Optional[int] = None,
              expected_condition: EC = EC.visibility_of_element_located, ) -> WebElement:
        if not timeout:
            timeout = self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout).until(expected_condition(locator))

    def get_element(self, locator):
        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_element_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_elements_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_element_by_type(self, method, value) -> WebElement:
        if method == 'accessibility_id':
            return self.driver.find_element_by_accessibility_id(value)
        elif method == 'android':
            return self.driver.find_element_by_android_uiautomator('new UiSelector().%s' % value)
        elif method == 'ios':
            return self.driver.find_element_by_ios_uiautomation(value)
        elif method == 'class_name':
            return self.driver.find_element_by_class_name(value)
        elif method == 'id':
            return self.driver.find_element(By.ID, value)
        elif method == 'xpath':
            return self.driver.find_element(By.XPATH, value)
        elif method == 'name':
            return self.driver.find_element_by_name(value)
        else:
            raise Exception('Invalid locator method.')

    def get_elements(self, locator):

        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.get_elements_by_type(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.get_elements_by_type(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def get_elements_by_type(self, method, value):
        if method == 'accessibility_id':
            return self.driver.find_elements_by_accessibility_id(value)
        elif method == 'android':
            return self.driver.find_elements_by_android_uiautomator(value)
        elif method == 'ios':
            return self.driver.find_elements_by_ios_uiautomation(value)
        elif method == 'class_name':
            return self.driver.find_elements_by_class_name(value)
        elif method == 'id':
            return self.driver.find_elements(By.ID, value)
        elif method == 'xpath':
            return self.driver.find_element(By.XPATH, value)
        elif method == 'name':
            return self.driver.find_elements_by_name(value)
        else:
            raise Exception('Invalid locator method.')

        # element visible

    def is_visible(self, locator) -> bool:
        try:
            return self._wait(locator).is_displayed()
        except Exception:
            return False

    def wait_visible(self, locator, timeout=25):
        i = 0
        while i != timeout:
            try:
                self.is_visible(locator)
                return self.get_element(locator)
            except NoSuchElementException:
                sleep(1)
                i += 1
        raise Exception('Element never became visible: %s (%s)' % (locator[0], locator[1]))

        # clicks and taps

    def click(self, locator):
        self._wait(locator).click()

    def tap(self, locator):
        element = self.wait_visible(locator)
        element.tap()

    def hide_keyboard(self):
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def send_keys(self, locator, text):
        element = self.wait_visible(locator)
        element.send_keys(text)
        sleep(0.5)

    def clear(self, locator):
        element = self.wait_visible(locator)
        element.clear()
        sleep(0.5)

        # android scroll

    def android_scroll(self, container_locator, target_locator):
        for _ in range(15):
            try:
                element = self.wait_visible(container_locator)
                container = element.rect
                x = (container.get('width') / 2 + container.get('x'))
                y = (container.get('height') / 2 + container.get('y'))
                y2 = y - y * 0.3
                self.driver.swipe(x, y, x, y2, 300)

                value = self.get_element(target_locator).is_displayed()
                if value is True:
                    break
            except NoSuchElementException:
                pass

    def ios_scroll(self, locator):
        el = self.wait_visible(locator)
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})

        # common method to scroll in android & ios

    def scrolling(self, container_locator, target_locator):
        if platform == 'ios':
            self.ios_scroll(container_locator, target_locator)
        else:
            self.android_scroll(container_locator, target_locator)

        # get text

    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text
