from sim import (
    Simulator,
    Config,
    WebServerSystem,
    RoundRobinScheduler,
    MetricsCollector,
)

def run_experiment(num_cores, max_threads):
    """
    Run simulation for a given system size.
    """
    config = Config()
    config.num_cores = num_cores
    config.max_threads = max_threads

    scheduler = RoundRobinScheduler()
    system = WebServerSystem(config, scheduler)
    metrics = MetricsCollector(warmup_time=config.warmup_time)

    sim = Simulator(config, system, metrics)
    sim.run()

    return metrics


def main():
    """
    Scalability what-if experiments.
    """
    core_values = [1, 2, 4, 8]

    for c in core_values:
        metrics = run_experiment(num_cores=c, max_threads=2*c)
        # TODO: store results


if __name__ == "__main__":
    main()