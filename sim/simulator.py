import heapq


class Simulator:
    """
    Global discrete event simulator.
    Manages clock and future event list.
    """

    def __init__(self, config, system, metrics, tracer=None):
        self.config = config
        self.system = system
        self.metrics = metrics
        self.tracer = tracer

        self.current_time = 0.0
        self.event_queue = []

    def schedule_event(self, event):
        """Insert event into the future event list."""
        heapq.heappush(self.event_queue, (event.time, event))

    def run(self):
        """
        Main simulation loop.
        Pops events in time order and processes them.
        """
        while self.event_queue:
            time, event = heapq.heappop(self.event_queue)
            self.current_time = time

            if self.tracer:
                self.tracer.log_event(event, self.current_time)

            event.process(self)