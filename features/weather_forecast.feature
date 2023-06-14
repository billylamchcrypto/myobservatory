# Created by billylam at 1/6/2023
Feature: Weather Forecast

  Scenario: Check tomorrow weather forecast from 9-day forecast screen
    Given the user is in Disclaimer page
    When the user clicks Agree button on the disclaimer page
    Then the user is redirected to the Privacy Policy Statements page
    When the user clicks Agree button on the Privacy Policy Statements page
    Then the user is redirected to the Background Access to Location Information page
    When the user clicks OK button
    Then the user is redirected to the new Location Access page
    When the user clicks While using the app button
    Then the user is redirected to the Location Permission page
    When the user clicks the Back button
#These are only for AOS version 9
#    Then the user is redirected to the device location access page
#    When the user clicks Allow only while using the app
#    Then the user is redirected to the device location access page with time factor
#    When the user clicks Allow all the time
    Then the user is redirected to the Whats new page
    When the user clicks the next button in whats new page
    Then the user is redirected to the Traffic Information Tutorial page
    When the user clicks the close button in Traffic Information Tutorial page
    Then the user is redirected to the Home page
    When the user clicks the menu bar
    Then the user scroll down in menu bar and clicks the "9-Day Forecast" from the menu bar
    And the user can see the "9-Day Forecast"
