from infra.base import Base
from hamcrest import assert_that, equal_to


class WhatsNew(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    WHATS_NEW_TITLE = ('id', 'hko.MyObservatory_v1_0:id/whatsNewTitle')
    NEXT_BUTTON = ('id', 'hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip')

    def whats_new_here(self):
        self.is_visible(self.WHATS_NEW_TITLE)

    # def whats_new_check_ver(self):
    #     assert_that(self.get_text(self.WHATS_NEW_TITLE), equal_to

    def whats_new_next(self):
        self.click(self.NEXT_BUTTON)
