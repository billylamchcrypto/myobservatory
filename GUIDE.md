# Tour guide of this project

## weather_fore.feature

```text
Feature: Weather Forecast

  Scenario: Check tomorrow weather forecast from 9-day forecast screen
    Given the user is in Disclaimer page
    When the user clicks Agree button on the disclaimer page
    Then the user is redirected to the Privacy Policy Statements page
```
All the bdd steps are saved in this file
## page file (e.g: home.page.py)

All the elements and saved here and each of them is called by different utilities I set up in base screen
```python
class Home(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

# aos element only for AOS
    HOME_TITLE = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')
    MENU_BAR = ('xpath', '//android.widget.ImageButton[@content-desc="Navigate up"]')
    NINE_DAYS_FORECAST = ('xpath', '//*[contains(@text, "9-Day Forecast")]')
    MENU_CONTAINER = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout')

    def home_here(self):
        assert_that(self.is_visible(self.HOME_TITLE), "Failed to go to the Home page")

    def open_menu_bar(self):
        self.click(self.MENU_BAR)
```


## base_screen.py
Let me highlight some useful utilities

*This is an explicit wait which keeps finding elements until it is found and then returns the element for other utilities to perform action
```python
    def _wait(self, locator: Tuple[str, str], timeout: Optional[int] = None,
              expected_condition: EC = EC.visibility_of_element_located, ) -> WebElement:
        if not timeout:
            timeout = self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, timeout).until(expected_condition(locator))
```


*This is the scrolling method I made  for AOS. I will get the coordination of the scrolling area first. 
Then I will use mid-point theory to calculate the middle point of the container.
The destination Y2 is using y coordination of the middle point to multiply by 0.3 to get a upper position.
Then swipe from the middle point to the upper position. I am using a for loop here because I want to method to keep scrolling until the element is found by using explicit wait method.
```python
        def android_scroll(self, container_locator, target_locator):
        for _ in range(15):
            try:
                element = self._wait(container_locator)
                container = element.rect
                x = (container.get('width') / 2 + container.get('x'))
                y = (container.get('height') / 2 + container.get('y'))
                y2 = y - y * 0.3
                self.driver.swipe(x, y, x, y2, 250)

                value = self._wait(target_locator).is_displayed()
                if value is True:
                    break
            except NoSuchElementException:
                pass
```

## nine_days_forecast.py
*Here is the storage for all steps by using the utilities in base screen to call the element in page according to the bdd steps
```python
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
```

## test_weather_forecast.py
* The file stating withing test is the file for running the bdd steps in weather_forecast.feature with pytest
```
scenarios('../features/weather_forecast.feature')
```

## conftest.py
* The driver is initialised here by using fixture and called by different files by using __init__ method
```python
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
```

## settings.py
* This is worked with the config.yml. 
* When settings.py is imported, calling CONFIG[platform][<'parameters'>] in config.yml can output the device information to use in different in method.
```
if os.path.exists(os.path.dirname(__file__) + "/yml/config.yml"):
    env = os.environ.get('env', 'production')
    env = env.lower()

    CONFIG = yaml.safe_load(open(os.path.dirname(__file__) + "/yml/config.yml", 'r'))[env]

    if not CONFIG:
        raise ValueError("Invalid Environment")
else:
    raise FileNotFoundError("config.yml does not exists")

platform = (CONFIG['platform'])
```