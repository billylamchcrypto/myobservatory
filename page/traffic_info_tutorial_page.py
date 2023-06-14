from hamcrest import assert_that

from page.base_screen import BaseScreen


class TrafficInfoTutorial(BaseScreen):
    # aos element
    TRAFFIC_INFO_TITLE = ('id', 'txt')
    CLOSE_BUTTON = ('id', 'btn_friendly_reminder_skip')

    def traffic_info_tutorial_here(self):
        assert_that(self.is_visible(self.TRAFFIC_INFO_TITLE), "Failed to go to the Privacy Policy Statements page")

    def traffic_info_tutorial_close(self):
        self.click(self.CLOSE_BUTTON)
