from time import sleep
from page import Pages
from pytest_bdd import given, when, then
from selenium.common.exceptions import NoSuchElementException


@given('the user is in Disclaimer page')
def in_disclaimer_page(pages: Pages):
    try:
        pages.disclaimer.disclaimer_here()
        print("\nDisclaimer page is opened")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Agree button on the disclaimer page')
def clicks_agree_button_on_the_disclaimer_page(pages: Pages):
    try:
        pages.disclaimer.disclaimer_agree()
        print("User agrees the disclaimer")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Privacy Policy Statements page')
def in_privacy_policy_statements_page(pages: Pages):
    try:
        pages.privacy_policy_statements.statements_here()
        print("User is redirected to the Privacy Policy Statements page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Agree button on the Privacy Policy Statements page')
def clicks_agree_button_on_the_statements_page(pages: Pages):
    try:
        pages.privacy_policy_statements.statements_agree()
        print("User agrees the Privacy Policy Statements")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Background Access to Location Information page')
def in_background_access_to_location_information_page(pages: Pages):
    try:
        pages.background_location_access.background_location_access_here()
        print("The user is redirected to the Background Access to Location Information page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks OK button')
def clicks_ok_button(pages: Pages):
    try:
        pages.background_location_access.background_location_access_ok()
        print("User agrees background location access")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the new Location Access page')
def in_new_location_access_page(pages: Pages):
    try:
        pages.device_location_access.new_device_location_access_here()
        print("The user is redirected to the Device location access page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks While using the app button')
def clicks_while_using_the_app(pages: Pages):
    try:
        pages.device_location_access.while_using_the_app()
        print("The user clicks Allow only while using the app in Device Location Access page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Location Permission page')
def in_location_permission(pages: Pages):
    try:
        pages.device_location_access.location_permission_here()
        print("The user is redirected to the location permission page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the Back button')
def clicks_back_button_in_location_permission(pages: Pages):
    try:
        pages.device_location_access.device_back()
    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the device location access page')
def in_device_location_access_page(pages: Pages):
    try:
        pages.device_location_access.device_location_access_here()
        print("The user is redirected to the Device location access page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Allow only while using the app')
def clicks_allow_only_while_using_the_app(pages: Pages):
    try:
        pages.device_location_access.device_location_access_allow()
        sleep(3)
        print("The user clicks Allow only while using the app in Device Location Access page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the device location access page with time factor')
def in_device_location_access_page_with_time(pages: Pages):
    try:
        pages.device_location_access.device_location_access_alltime_here()
        print("The user is redirected to the Device location access page with time factor")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks Allow all the time')
def clicks_allow_all_the_time_in_device_location_access_page_with_time(pages: Pages):
    try:
        pages.device_location_access.device_location_access_allow_all_time()
    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Whats new page')
def in_whats_new_page(pages: Pages):
    try:
        pages.whats_new.whats_new_here()
        print("The user is redirected to the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the next button in whats new page')
def clicks_next_in_whats_new_page(pages: Pages):
    try:
        pages.whats_new.whats_new_next()
        print("The user click next in the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Traffic Information Tutorial page')
def in_traffic_info_tutorial_page(pages: Pages):
    try:
        pages.traffic_info_tutorial.traffic_info_tutorial_here()
        print("the user is redirected to the Traffic Information Tutorial page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the close button in Traffic Information Tutorial page')
def close_the_traffic_info_tutorial_page(pages: Pages):
    try:
        pages.traffic_info_tutorial.traffic_info_tutorial_close()
        print("the user clicks the close button in Traffic Information Tutorial page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user is redirected to the Home page')
def in_home_page(pages: Pages):
    try:
        # pages.home.go()
        pages.home.home_here()
        print("the user is redirected to the Home page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('the user clicks the menu bar')
def clicks_menu_bar(pages: Pages):
    try:
        pages.home.open_menu_bar()
        print("the menu bar is opened")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user scroll down in menu bar and clicks the "9-Day Forecast" from the menu bar')
def scroll_down_menu_bar_and_click_nine_days_forecast(pages: Pages):
    try:
        pages.home.scroll_menu_bar()
        pages.home.select_nine_days_forecast()
        print("the user selects the 9 Days Forecast")

    except NoSuchElementException as e:
        print("Failed", e)


@then('the user can see the "9-Day Forecast"')
def in_nine_days_forecast(pages: Pages):
    try:
        pages.nine_days_forecast.nine_days_forecast_here()
        print("the user is in the 9 Days Forecast page")
    except NoSuchElementException as e:
        print("Failed", e)

