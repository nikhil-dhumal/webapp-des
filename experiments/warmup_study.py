from sim import (
    Simulator,
    Config,
    WebServerSystem,
    RoundRobinScheduler,
    MetricsCollector,
)

def run_with_warmup(warmup_time):
    """
    Run a simulation with a given warm-up time.
    """
    config = Config()
    config.warmup_time = warmup_time

    scheduler = RoundRobinScheduler()
    system = WebServerSystem(config, scheduler)
    metrics = MetricsCollector(warmup_time=warmup_time)

    sim = Simulator(config, system, metrics)
    sim.run()

    return metrics


def main():
    """
    Compare metrics across different warm-up periods.
    """
    warmup_values = [0, 50, 100, 200]

    for w in warmup_values:
        metrics = run_with_warmup(w)
        # TODO: store and compare results


if __name__ == "__main__":
    main()