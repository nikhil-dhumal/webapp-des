class MetricsCollector:
    """
    Collects raw simulation measurements.
    """

    def __init__(self, warmup_time=0.0):
        self.warmup_time = warmup_time

        self.response_times = []
        self.completed = 0
        self.timed_out = 0
        self.dropped = 0

    def record_completion(self, request, current_time):
        pass

    def record_timeout(self, request):
        pass

    def record_drop(self):
        pass