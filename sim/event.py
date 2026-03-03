class Event:
    """
    Base class for all simulation events.
    """

    def __init__(self, time):
        self.time = time

    def process(self, sim):
        raise NotImplementedError


class RequestArrivalEvent(Event):
    """A new request arrives at the system."""

    def __init__(self, time, user):
        super().__init__(time)
        self.user = user

    def process(self, sim):
        pass


class RequestStartEvent(Event):
    """A request starts execution on a thread."""

    def __init__(self, time, request):
        super().__init__(time)
        self.request = request

    def process(self, sim):
        pass


class RequestCompletionEvent(Event):
    """A request completes execution."""

    def __init__(self, time, request):
        super().__init__(time)
        self.request = request

    def process(self, sim):
        pass


class RequestTimeoutEvent(Event):
    """A request times out."""

    def __init__(self, time, request):
        super().__init__(time)
        self.request = request

    def process(self, sim):
        pass


class ContextSwitchEvent(Event):
    """Models context switching overhead."""

    def __init__(self, time, thread):
        super().__init__(time)
        self.thread = thread

    def process(self, sim):
        pass