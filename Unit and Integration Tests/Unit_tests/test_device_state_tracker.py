import unittest
from ..device_state_tracker import DeviceStateTracker

class TestDeviceStateTracker(unittest.TestCase):

    def setUp(self):
        self.state_tracker = DeviceStateTracker()

    def test_update_expected_state(self):
        # Test updating expected state
        self.state_tracker.update_expected_state("key1", "value1")
        self.assertEqual(self.state_tracker.expected_state["key1"], "value1")

        # Test updating another key-value pair
        self.state_tracker.update_expected_state("key2", "value2")
        self.assertEqual(self.state_tracker.expected_state["key2"], "value2")

    def test_verify_state(self):
        # Set up initial expected state
        self.state_tracker.update_expected_state("key1", "value1")
        self.state_tracker.update_expected_state("key2", "value2")

        # Test case where actual state matches expected state
        actual_state = {"key1": "value1", "key2": "value2"}
        self.assertTrue(self.state_tracker.verify_state(actual_state))

        # Test case where actual state does not match expected state
        actual_state["key2"] = "value3"  # Change key2 to simulate a mismatch
        self.assertFalse(self.state_tracker.verify_state(actual_state))

if __name__ == "__main__":
    unittest.main()
