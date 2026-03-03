from sim import (
    Simulator,
    Config,
    WebServerSystem,
    RoundRobinScheduler,
    MetricsCollector,
    TraceLogger,
)

def load_config():
    """
    Load or construct a Config object.
    Later this will parse YAML/JSON.
    """
    config = Config()

    # TODO: populate config fields
    # config.num_cores = ...
    # config.num_users = ...
    # config.simulation_time = ...

    return config


def main():
    """
    Entry point for running a single simulation.
    """
    config = load_config()

    scheduler = RoundRobinScheduler()
    system = WebServerSystem(config, scheduler)
    metrics = MetricsCollector(warmup_time=config.warmup_time)
    tracer = TraceLogger(enabled=True)

    sim = Simulator(config, system, metrics, tracer)
    sim.run()

    # TODO: write metrics to file


if __name__ == "__main__":
    main()