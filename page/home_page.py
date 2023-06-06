from infra.base import Base
from settings import*


class Home(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    HOME_TITLE = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')
    MENU_BAR = ('xpath', '//android.widget.ImageButton[@content-desc="Navigate up"]')
    NINE_DAYS_FORECAST = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[8]')
    MENU_CONTAINER = ('xpath', '//*[contains(@text, "9-Day Forecast")]')

    def home_here(self):
        self.is_visible(self.HOME_TITLE)

    def open_menu_bar(self):
        self.click(self.MENU_BAR)

    def go(self):
        self.driver.terminate_app(CONFIG[platform]['appPackage'])
        self.driver.activate_app(CONFIG[platform]['appPackage'])

    def scroll_menu_bar(self):
        self.scrolling(self.MENU_CONTAINER, self.NINE_DAYS_FORECAST)

    def select_nine_days_forecast(self):
        self.click(self.NINE_DAYS_FORECAST)
