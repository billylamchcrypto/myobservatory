from page.disclaimer_page import Disclaimer
from page.background_location_access_page import BackgroundLocationAccess
from page.device_location_access_page import DeviceLocationAccessPage
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