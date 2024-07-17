import time

class PerformanceMonitor:
    def __init__(self):
        self.actions_count = 0
        self.success_count = 0
        self.total_recovery_time = 0.0

    def track_action(self, success=True):
        self.actions_count += 1
        if success:
            self.success_count += 1

    def track_recovery_time(self, start_time):
        end_time = time.time()
        recovery_time = end_time - start_time
        self.total_recovery_time += recovery_time
        print(f"Recovery time for last session: {recovery_time} seconds")

    def get_success_rate(self):
        if self.actions_count == 0:
            return 0.0
        return (self.success_count / self.actions_count) * 100

    def get_average_recovery_time(self):
        if self.actions_count == 0:
            return 0.0
        return self.total_recovery_time / self.actions_count
