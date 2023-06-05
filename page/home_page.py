from infra.base import Base


class Home(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    HOME_TITLE = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')
    MENU_BAR = ('xpath', '//android.widget.ImageButton[@content-desc="Navigate up"]')
    NINE_DAYS_FORECAST = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[7]')

    def home_here(self):
        self.wait_visible(self.HOME_TITLE)

    def open_menu_bar(self):
        self.click(self.MENU_BAR)

    def scroll_menu_bar(self):
        self.android_scroll(self.NINE_DAYS_FORECAST)
