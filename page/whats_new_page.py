from hamcrest import assert_that

from page.base_screen import BaseScreen


class WhatsNew(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    WHATS_NEW_TITLE = ('id', 'hko.MyObservatory_v1_0:id/whatsNewTitle')
    NEXT_BUTTON = ('id', 'hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip')

    def whats_new_here(self):
        assert_that(self.is_visible(self.WHATS_NEW_TITLE), "Failed to go to the Privacy Policy Statements page")

    def whats_new_next(self):
        self.click(self.NEXT_BUTTON)
