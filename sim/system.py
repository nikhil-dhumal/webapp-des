class Core:
    """Represents a CPU core."""

    def __init__(self, core_id):
        self.core_id = core_id
        self.busy = False
        self.busy_time = 0.0


class Thread:
    """Represents a worker thread."""

    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.current_request = None


class WebServerSystem:
    """
    Multi-core, multi-threaded web server model.
    """

    def __init__(self, config, scheduler):
        self.config = config
        self.scheduler = scheduler

        self.cores = [Core(i) for i in range(config.num_cores)]
        self.threads = [Thread(i) for i in range(config.max_threads)]

        self.waiting_queue = []
        self.ready_threads = []

    def admit_request(self, request):
        """
        Admit a request into the system or drop it.
        """
        pass

    def assign_thread(self):
        """
        Assign a thread to a waiting request if possible.
        """
        pass

    def release_thread(self, thread):
        """
        Release thread after request completion.
        """
        pass