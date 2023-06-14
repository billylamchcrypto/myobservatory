from hamcrest import assert_that

from page.base_screen import BaseScreen


class WhatsNew(BaseScreen):
    # aos element
    WHATS_NEW_TITLE = ('id', 'whatsNewTitle')
    NEXT_BUTTON = ('id', 'btn_friendly_reminder_skip')

    def whats_new_here(self):
        assert_that(self.is_visible(self.WHATS_NEW_TITLE), "Failed to go to the Privacy Policy Statements page")

    def whats_new_next(self):
        self.click(self.NEXT_BUTTON)
