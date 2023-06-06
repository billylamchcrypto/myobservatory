from time import sleep

from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import By
import os
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from settings import *
from appium.webdriver.extensions import location


class PageUtils:
    def __init__(self, driver):
        self.driver = driver

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

    def get_element_by_type(self, method, value) ->WebElement:
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

    def is_visible(self, locator):
        try:
            self.get_element(locator).is_displayed()
            return True
        except NoSuchElementException:
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
        element = self.wait_visible(locator)
        element.click()

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
                temp = element.rect
                x = (temp.get('width')/2 + temp.get('x'))
                y = (temp.get('height')/2 + temp.get('y'))
                y2 = y-y*0.3
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

    def get_rect(self, locator):
        element = self.wait_visible(locator)
        temp = element.rect
        x = (temp.get('width')+temp.get('x')/2)
        y = (temp.get('height')+temp.get('y')/2)



