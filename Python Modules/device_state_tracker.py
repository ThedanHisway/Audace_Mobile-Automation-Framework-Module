class DeviceStateTracker:
    def __init__(self):
        self.expected_state = {}

    def update_expected_state(self, key, value):
        self.expected_state[key] = value
        print(f"Updated expected state: {self.expected_state}")

    def verify_state(self, actual_state):
        for key, value in self.expected_state.items():
            if key not in actual_state or actual_state[key] != value:
                print(f"State verification failed for {key}. Expected: {value}, Actual: {actual_state.get(key)}")
                return False
        print("State verification passed.")
        return True
