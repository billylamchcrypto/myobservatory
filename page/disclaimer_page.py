from infra.base import Base


class Disclaimer(Base):

    def __init__(self, driver):
        super().__init__(driver)

# aos element
    DISCLAIMER_TITLE = ('id', 'hko.MyObservatory_v1_0:id/txt_title')
    AGREE_BUTTON = ('id', 'hko.MyObservatory_v1_0:id/btn_agree')
    CONTAINER = ('id', 'android:id/content')

    def disclaimer_agree(self):
        self.click(self.AGREE_BUTTON)

    def disclaimer_here(self):
        self.is_visible(self.DISCLAIMER_TITLE)



