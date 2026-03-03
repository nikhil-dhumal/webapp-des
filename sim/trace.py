class TraceLogger:
    """
    Centralized trace logger.
    """

    def __init__(self, enabled=True):
        self.enabled = enabled

    def log_event(self, event, time):
        if not self.enabled:
            return
        print(f"[T={time:.4f}] {event.__class__.__name__}")