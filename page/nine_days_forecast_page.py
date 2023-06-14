from hamcrest import assert_that

from page.base_screen import BaseScreen


class NineDaysForecast(BaseScreen):
    # aos element
    NINE_DAYS_FORECAST_TITLE = ('xpath', '//android.widget.LinearLayout[@content-desc="9-Day Forecast"]/android.widget.TextView')

    def nine_days_forecast_here(self):
        assert_that(self.is_visible(self.NINE_DAYS_FORECAST_TITLE), "Failed to go to the 9-Days Forecast page")