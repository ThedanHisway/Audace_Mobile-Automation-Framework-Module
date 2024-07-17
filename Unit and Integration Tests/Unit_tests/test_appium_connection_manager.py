import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from typing import Dict
#from appium_automation_framework.appium_connection_manager import AppiumConnectionManager
# Correct import statement
from appium_automation_framework.appium_connection_manager import AppiumConnectionManager

@pytest.fixture(scope="module")
def appium_manager() -> AppiumConnectionManager:
    # Assuming Appium server is running with desired capabilities configured
    manager = AppiumConnectionManager()
    yield manager
    manager.stop_appium_server()

class TestAppiumConnectionManager:
    def test_start_appium_server(self, appium_manager: AppiumConnectionManager):
        assert appium_manager.start_appium_server(), "Failed to start Appium server"

    def test_create_driver_session(self, appium_manager: AppiumConnectionManager):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '9xy5756xfquckj95',  # Replace with your device ID
            'appPackage': 'com.example.myapp',  # Replace with your app's package name
            'appActivity': '.MainActivity',  # Replace with your app's main activity
            'automationName': 'UiAutomator2'
        }
        driver = appium_manager.create_driver_session(desired_caps)
        assert isinstance(driver, WebDriver), "Driver session creation failed"

    def test_check_session_health(self, appium_manager: AppiumConnectionManager):
        health_status = appium_manager.check_session_health()
        assert health_status, "Session health check failed"

    def test_recover_session(self, appium_manager: AppiumConnectionManager):
        recovered = appium_manager.recover_session()
        assert recovered, "Session recovery failed"

if __name__ == "__main__":
    pytest.main()
