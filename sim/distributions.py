class Distribution:
    """Base distribution class."""

    def sample(self):
        raise NotImplementedError


class ConstantDistribution(Distribution):
    def __init__(self, value):
        self.value = value

    def sample(self):
        pass


class UniformDistribution(Distribution):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def sample(self):
        pass


class ExponentialDistribution(Distribution):
    def __init__(self, mean):
        self.mean = mean

    def sample(self):
        pass