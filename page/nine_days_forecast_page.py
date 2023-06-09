from page.base_screen import BaseScreen


class NineDaysForecast(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    NINE_DAYS_FORECAST_TITLE = ('xpath', '//android.widget.LinearLayout[@content-desc="9-Day Forecast"]/android.widget.TextView')

    def nine_days_forecast_here(self):
        self.is_visible(self.NINE_DAYS_FORECAST_TITLE)