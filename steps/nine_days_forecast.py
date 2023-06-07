from time import sleep

from page.disclaimer_page import Disclaimer
from page.background_location_access_page import BackgroundLocationAccess
from page.device_location_access_page import DeviceLocationAccess
from page.home_page import Home
from page.privacy_policy_statements_page import PrivacyPolicyStatements
from page.nine_days_forecast_page import NineDaysForecast
from page. traffic_info_tutorial_page import TrafficInfoTutorial
from page.whats_new_page import WhatsNew
from pytest_bdd import scenario, given, when, then
from selenium.common.exceptions import NoSuchElementException


@given('the user is in Disclaimer page')
def in_disclaimer_page(driver):
    driver = Disclaimer(driver)
    try:
        Disclaimer.disclaimer_here(driver)
        print("\nDisclaimer page is opened")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Agree button on the disclaimer page')
def clicks_agree_button_on_the_disclaimer_page(driver):
    driver = Disclaimer(driver)
    try:
        Disclaimer.disclaimer_agree(driver)
        print("User agrees the disclaimer")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Privacy Policy Statements page')
def in_privacy_policy_statements_page(driver):
    driver = PrivacyPolicyStatements(driver)
    try:
        PrivacyPolicyStatements.statements_here(driver)
        print("User is redirected to the Privacy Policy Statements page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Agree button on the Privacy Policy Statements page')
def clicks_agree_button_on_the_statements_page(driver):
    driver = PrivacyPolicyStatements(driver)
    try:
        PrivacyPolicyStatements.statements_agree(driver)
        print("User agrees the Privacy Policy Statements")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Background Access to Location Information page')
def in_background_access_to_location_information_page(driver):
    driver = BackgroundLocationAccess(driver)
    try:
        BackgroundLocationAccess.background_location_access_here(driver)
        print("The user is redirected to the Background Access to Location Information page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks OK button')
def clicks_ok_button(driver):
    driver = BackgroundLocationAccess(driver)
    try:
        BackgroundLocationAccess.background_location_access_ok(driver)
        print("User agrees background location access")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the device location access page')
def in_device_location_access_page(driver):
    driver = DeviceLocationAccess(driver)
    try:
        DeviceLocationAccess.device_location_access_here(driver)
        print("The user is redirected to the Device location access page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Allow only while using the app')
def clicks_allow_only_while_using_the_app(driver):
    driver = DeviceLocationAccess(driver)
    try:
        DeviceLocationAccess.device_location_access_allow(driver)
        sleep(3)
        print("The user clicks Allow only while using the app in Device Location Access page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the device location access page with time factor')
def in_device_location_access_page_with_time(driver):
    driver = DeviceLocationAccess(driver)
    try:
        DeviceLocationAccess.device_location_access_alltime_here(driver)
        print("The user is redirected to the Device location access page with time factor")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Allow all the time')
def clicks_allow_all_the_time_in_device_location_access_page_with_time(driver):
    driver = DeviceLocationAccess(driver)
    try:
        DeviceLocationAccess.device_location_access_allow_all_time(driver)
    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Whats new page')
def in_whats_new_page(driver):
    driver = WhatsNew(driver)
    try:
        WhatsNew.whats_new_here(driver)
        print("The user is redirected to the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the next button in whats new page')
def clicks_next_in_whats_new_page(driver):
    driver = WhatsNew(driver)
    try:
        WhatsNew.whats_new_next(driver)
        print("The user click next in the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Traffic Information Tutorial page')
def in_traffic_info_tutorial_page(driver):
    driver = TrafficInfoTutorial(driver)
    try:
        TrafficInfoTutorial.traffic_info_tutorial_here(driver)
        print("the user is redirected to the Traffic Information Tutorial page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the close button in Traffic Information Tutorial page')
def close_the_traffic_info_tutorial_page(driver):
    driver = TrafficInfoTutorial(driver)
    try:
        TrafficInfoTutorial.traffic_info_tutorial_close(driver)
        print("the user clicks the close button in Traffic Information Tutorial page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Home page')
def in_home_page(driver):
    driver = Home(driver)
    try:
        Home.go(driver)
        Home.home_here(driver)
        print("the user is redirected to the Home page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the menu bar')
def clicks_menu_bar(driver):
    driver = Home(driver)
    try:
        Home.open_menu_bar(driver)
        print("the menu bar is opened")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user scroll down in menu bar and clicks the "9-Day Forecast" from the menu bar')
def scroll_down_menu_bar_and_click_nine_days_forecast(driver):
    driver = Home(driver)
    try:
        Home.scroll_menu_bar(driver)
        sleep(5)
        Home.select_nine_days_forecast(driver)
        print("the user selects the 9 Days Forecast")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user can see the "9-Day Forecast"')
def in_nine_days_forecast(driver):
    driver = NineDaysForecast(driver)
    try:
        NineDaysForecast.nine_days_forecast_here(driver)
        print("the user is in the 9 Days Forecast page")
    except NoSuchElementException as e:
        print("Failed", e)
