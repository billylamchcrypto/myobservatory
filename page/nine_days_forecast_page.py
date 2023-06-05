from infra.base import Base


class NineDaysForecast(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    NINE_DAYS_FORECAST_TITLE = ('id', 'hko.MyObservatory_v1_0:id/txt_title')

    def nine_days_forecast_here(self):
        self.wait_visible(self.NINE_DAYS_FORECAST_TITLE)