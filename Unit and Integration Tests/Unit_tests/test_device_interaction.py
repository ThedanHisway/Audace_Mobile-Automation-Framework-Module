import unittest
from unittest.mock import MagicMock
from appium.webdriver.common.touch_action import TouchAction
from ..appium_connection_manager import AppiumConnectionManager
from ..device_interaction import DeviceInteraction

class TestDeviceInteraction(unittest.TestCase):
    
    def setUp(self):
        # Mocking AppiumConnectionManager
        self.connection_manager = MagicMock(spec=AppiumConnectionManager)
        self.driver_mock = MagicMock()
        self.connection_manager.driver = self.driver_mock
        self.device_interaction = DeviceInteraction(self.connection_manager)

    def test_perform_tap(self):
        # Mocking TouchAction and action.tap
        action_mock = MagicMock(spec=TouchAction)
        self.connection_manager.recover_session.side_effect = [None]  # Mock successful session recovery
        TouchAction.return_value = action_mock

        # Testing perform_tap method
        self.device_interaction.perform_tap(100, 200)

        # Asserting that action.tap(x=100, y=200) was called once
        action_mock.tap.assert_called_once_with(x=100, y=200)

    def test_perform_swipe(self):
        # Mocking TouchAction and action.press
        action_mock = MagicMock(spec=TouchAction)
        self.connection_manager.recover_session.side_effect = [None]  # Mock successful session recovery
        TouchAction.return_value = action_mock

        # Testing perform_swipe method
        self.device_interaction.perform_swipe(100, 200, 300, 400)

        # Asserting that action.press(x=100, y=200).move_to(x=300, y=400).release().perform() was called once
        action_mock.press.assert_called_once_with(x=100, y=200)
        action_mock.move_to.assert_called_once_with(x=300, y=400)
        action_mock.release.assert_called_once()

    def test_perform_text_typing(self):
        # Mocking switch_to.active_element and send_keys
        element_mock = MagicMock()
        self.driver_mock.switch_to.active_element = element_mock
        self.connection_manager.recover_session.side_effect = [None]  # Mock successful session recovery

        # Testing perform_text_typing method
        self.device_interaction.perform_text_typing("Hello, world!")

        # Asserting that send_keys("Hello, world!") was called once
        element_mock.send_keys.assert_called_once_with("Hello, world!")

    def test_reset_application_state(self):
        self.connection_manager.recover_session.side_effect = [None]  # Mock successful session recovery

        # Testing reset_application_state method
        self.device_interaction.reset_application_state()

        # Add assertions as per implementation

if __name__ == "__main__":
    unittest.main()
