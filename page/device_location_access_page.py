from page.base_screen import BaseScreen


class DeviceLocationAccess(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# aos element
    DEVICE_LOCATION_ACCESS_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    DEVICE_LOCATION_ACCESS_ALLTIME_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    ALLOW_BUTTON = ('id', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    ALLOW_ALL_TIME_BUTTON = ('id', 'com.android.permissioncontroller:id/permission_allow_button')

    def device_location_access_here(self):
        self.is_visible(self.DEVICE_LOCATION_ACCESS_TITLE)

    def device_location_access_allow(self):
        self.click(self.ALLOW_BUTTON)

    def device_location_access_alltime_here(self):
        self.is_visible(self.DEVICE_LOCATION_ACCESS_ALLTIME_TITLE)

    def device_location_access_allow_all_time(self):
        self.click(self.ALLOW_ALL_TIME_BUTTON)

