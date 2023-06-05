from infra.base import Base


class DeviceLocationAccess(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    DEVICE_LOCATION_ACCESS_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    DEVICE_LOCATION_ACCESS_ALLTIME_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    ALLOW_BUTTON = ('id', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    ALLOW_ALLTIME_BUTTON = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]')

    def device_location_access_here(self):
        self.is_visible(self.DEVICE_LOCATION_ACCESS_TITLE)

    def device_location_access_allow(self):
        self.click(self.ALLOW_BUTTON)

    def device_location_access_alltime_here(self):
        self.is_visible(self.DEVICE_LOCATION_ACCESS_ALLTIME_TITLE)

    def device_location_access_allow_alltime(self):
        self.click(self.ALLOW_ALLTIME_BUTTON)

