class Scheduler:
    """Base scheduling policy."""

    def select_thread(self, ready_threads):
        raise NotImplementedError


class RoundRobinScheduler(Scheduler):
    """Round-robin scheduling."""

    def __init__(self):
        self.last_index = 0

    def select_thread(self, ready_threads):
        pass


class FIFOScheduler(Scheduler):
    """FIFO scheduling."""

    def select_thread(self, ready_threads):
        pass