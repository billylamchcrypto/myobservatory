# `Weather forecast` Automation testing homework by Billy Lam

## Setup

Please run the poetry command to install the package:

```shell
poetry install
```
*You can create a new poetry python interpreter before running this project
## Input the information you want in method test_forecast()

config.yml
```yaml
platform: &platform
    platform: android

device_config: &device_config
    ios:
        platformName: 'ios'
        platformVersion: '13.5'
        deviceName: 'iPhone 11 Pro MT'
        automationName: 'XCUITest'
        appPackage: ''
        appActivity: ''
        noReset: True
        folder: '/Users/username/Library/Developer/Xcode/DerivedData/WordPress-bgx/Build/Products/Debug-iphonesimulator/WordPress.app'
    android:
        platformName: 'android'
        platformVersion: '12'
        deviceName: 'R5CT31Z18ZE'
        automationName: 'uiautomator2'
        appPackage: 'hko.MyObservatory_v1_0'
        app: '/Users/billylam/Desktop/apk/myobs.apk'
        noReset: False
        fullReset: True

production:
    <<: *platform
    <<: *device_config
```
If you change platform: to ios, it will use the ios capability to create driver. Since IOS element is not set up in this homework, it's ok to keep it in android.
Then please modify the **platformName**, **platformVersion** and **deviceName** according to your device information.

Also, I will send you the apk in another way, please move it to a certain directory and modify the path in **app**

*Its better use latest AOS version to perform the test. 
My first version is developed through AOS 9, but I found that some Android page is changed in 12.
Therefore, I made a change on it. Now it is developed based on AOS 12. 
## Run the file
```shell
pytest test/test_weather_forecast.py -vs
```
You will get the correct result like this. Every action it did will be recorded here
```output
Disclaimer page is opened
User agrees the disclaimer
User is redirected to the Privacy Policy Statements page
User agrees the Privacy Policy Statements
The user is redirected to the Background Access to Location Information page
User agrees background location access
The user is redirected to the Device location access page
The user clicks Allow only while using the app in Device Location Access page
The user is redirected to the location permission page
The user is redirected to the whats new page
The user click next in the whats new page
the user is redirected to the Traffic Information Tutorial page
the user clicks the close button in Traffic Information Tutorial page
the user is redirected to the Home page
the menu bar is opened
the user selects the 9 Days Forecast
the user is in the 9 Days Forecast page
PASSED

```
However, if the page is not accessed, you will get an assertion error here.
```output
Disclaimer page is opened
User agrees the disclaimer
User is redirected to the Privacy Policy Statements page
User agrees the Privacy Policy Statements
The user is redirected to the Background Access to Location Information page
User agrees background location access
FAILED

E       AssertionError: Failed to go to The Device location access page
```
