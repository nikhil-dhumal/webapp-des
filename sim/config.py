class Config:
    """
    Holds all simulation parameters.
    Loaded once per experiment.
    """

    def __init__(self):
        # System parameters
        self.num_cores = None
        self.max_threads = None
        self.context_switch_overhead = None

        # Workload parameters
        self.num_users = None
        self.think_time_dist = None
        self.service_time_dist = None
        self.timeout_dist = None

        # Retry policy
        self.enable_retries = False
        self.max_retries = 0
        self.retry_delay = 0.0

        # Overload control
        self.enable_overload_control = False
        self.queue_limit = None

        # Scheduling
        self.scheduler_type = "RR"

        # Simulation control
        self.simulation_time = None
        self.warmup_time = None