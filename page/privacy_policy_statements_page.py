from page.base_screen import BaseScreen


class PrivacyPolicyStatements(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    STATEMENTS_TITLE = ('id', 'hko.MyObservatory_v1_0:id/txt_title')
    AGREE_BUTTON = ('id', 'hko.MyObservatory_v1_0:id/btn_agree')

    def statements_here(self):
        self.is_visible(self.STATEMENTS_TITLE)

    def statements_agree(self):
        self.click(self.AGREE_BUTTON)
