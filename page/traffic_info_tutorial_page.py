from page.base_screen import BaseScreen


class TrafficInfoTutorial(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    TRAFFIC_INFO_TITLE = ('id', 'hko.MyObservatory_v1_0:id/txt')
    CLOSE_BUTTON = ('id', 'hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip')

    def traffic_info_tutorial_here(self):
        self.is_visible(self.TRAFFIC_INFO_TITLE)

    def traffic_info_tutorial_close(self):
        self.click(self.CLOSE_BUTTON)
