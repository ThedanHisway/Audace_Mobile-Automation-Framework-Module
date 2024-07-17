from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.touch_action import TouchAction
import time

class AppiumConnectionManager:
    def __init__(self, appium_server_url='http://localhost:4723/wd/hub'):
        self.appium_server_url = appium_server_url
        self.appium_service = None
        self.driver = None
    
    def start_appium_server(self):
    
        self.appium_service = AppiumService()
        self.appium_service.start()

    def stop_appium_server(self):
        
        if self.appium_service:
            self.appium_service.stop()

    def create_driver_session(self, desired_capabilities):
        
        try:
            self.driver = webdriver.Remote(self.appium_server_url, desired_capabilities)
            return self.driver
        except Exception as e:
            print(f"Failed to create Appium session: {str(e)}")
            return None

    def check_session_health(self):
        
        if self.driver:
            return self.driver.session
        return None

    def recover_session(self):
        
        if self.driver:
            current_activity = self.driver.current_activity
            if current_activity:
                
                print(f"Recovering session. Current activity: {current_activity}")
                
                self.reset_application_state()
                return True
            else:
                print("No current activity found. Cannot recover session.")
        return False

    def close_driver_session(self):
        
        if self.driver:
            self.driver.quit()
            self.driver = None

    def perform_tap(self, x, y):
        
        action = TouchAction(self.driver)
        action.tap(x=x, y=y).perform()

    def reset_application_state(self):
        try:
            self.driver.start_activity(app_package=self.app_package, app_activity=self.app_activity)
        
        
            self.log_out()
        
        
            self.driver.reset()
        
        

            print("Application state reset successfully.")
        except Exception as e:
            print(f"Failed to reset application state: {str(e)}")



if __name__ == "__main__":
    manager = AppiumConnectionManager()
    manager.start_appium_server()
    
    
    device_id = '9xy5756xfquckj95'
    desired_caps = {
    'platformName': 'Android',
    'deviceName': '9xy5756xfquckj95',  
    'appPackage': 'com.example.myapplication',  
    'appActivity': '.MainActivity',  
    'automationName': 'UiAutomator2',  
    'autoGrantPermissions': True,  
    'noReset': False,  
    'fullReset': False,  
    'newCommandTimeout': 6000  
    }

    
    driver = manager.create_driver_session(desired_caps)
    if driver:
        print("Appium session created successfully.")
        
        
        manager.perform_tap(100, 200)
        
        time.sleep(2)  
        
        manager.close_driver_session()
    else:
        print("Failed to create Appium session.")
    
    manager.stop_appium_server()
