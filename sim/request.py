class Request:
    """
    Represents a single web request.
    """

    def __init__(self, user, arrival_time):
        self.user = user
        self.arrival_time = arrival_time

        self.start_time = None
        self.completion_time = None
        self.timeout_time = None

        self.retries = 0
        self.completed = False
        self.timed_out = False