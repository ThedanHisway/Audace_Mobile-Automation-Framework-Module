from appium.webdriver.common.touch_action import TouchAction
from .appium_connection_manager import AppiumConnectionManager  

class DeviceInteraction:
    def __init__(self, connection_manager: AppiumConnectionManager):
        self.connection_manager = connection_manager

    def perform_tap(self, x, y):
        try:
            driver = self.connection_manager.driver
            action = TouchAction(driver)
            action.tap(x=x, y=y).perform()
            print(f"Tapped at coordinates ({x}, {y}) successfully.")
        except Exception as e:
            print(f"Failed to perform tap action: {str(e)}")
