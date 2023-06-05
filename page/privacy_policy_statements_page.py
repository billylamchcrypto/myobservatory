from infra.base import Base


class PrivacyPolicyStatements(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    STATEMENTS_TITLE = ('id', 'hko.MyObservatory_v1_0:id/txt_title')
    AGREE_BUTTON = ('id', 'hko.MyObservatory_v1_0:id/btn_agree')

    def statements_here(self):
        self.wait_visible(self.STATEMENTS_TITLE)

    def statements_agree(self):
        self.click(self.AGREE_BUTTON)
