"""
Core discrete event simulation package for web application modeling.
"""

# Core simulator
from .simulator import Simulator
from .config import Config

# Events
from .event import (
    Event,
    RequestArrivalEvent,
    RequestStartEvent,
    RequestCompletionEvent,
    RequestTimeoutEvent,
    ContextSwitchEvent,
)

# System model
from .system import WebServerSystem, Core, Thread

# Scheduling
from .scheduler import Scheduler, RoundRobinScheduler, FIFOScheduler

# Workload
from .user import User
from .request import Request

# Distributions
from .distributions import (
    Distribution,
    ConstantDistribution,
    UniformDistribution,
    ExponentialDistribution,
)

# Metrics & tracing
from .metrics import MetricsCollector
from .trace import TraceLogger

__all__ = [
    # Core
    "Simulator",
    "Config",

    # Events
    "Event",
    "RequestArrivalEvent",
    "RequestStartEvent",
    "RequestCompletionEvent",
    "RequestTimeoutEvent",
    "ContextSwitchEvent",

    # System
    "WebServerSystem",
    "Core",
    "Thread",

    # Scheduling
    "Scheduler",
    "RoundRobinScheduler",
    "FIFOScheduler",

    # Workload
    "User",
    "Request",

    # Distributions
    "Distribution",
    "ConstantDistribution",
    "UniformDistribution",
    "ExponentialDistribution",

    # Metrics
    "MetricsCollector",
    "TraceLogger",
]