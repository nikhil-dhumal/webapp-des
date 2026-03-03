class User:
    """
    Closed-loop user.
    """

    def __init__(self, user_id, think_time_dist):
        self.user_id = user_id
        self.think_time_dist = think_time_dist

    def sample_think_time(self):
        """Return think time before next request."""
        pass