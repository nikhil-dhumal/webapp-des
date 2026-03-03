# Web Application Discrete Event Simulation

This project implements a **Discrete Event Simulation (DES)** of a multi-core, multi-threaded web application server.

The goal is to study **performance behavior under load** and answer “what-if” questions that are difficult to analyze using only theoretical queueing models.

This project is done as part of **CS 681: Performance Evaluation of Computer Systems and Networks** at IIT Bombay, and is implemented by a team of two members.

---

## What This Simulator Models

The simulator models a realistic web server environment with:

- A multi-core server
- A thread-per-request execution model
- A limit on the maximum number of threads
- Round-robin scheduling (with alternative policies)
- Context switching overhead
- Closed-loop users (users think, then issue another request)
- Request timeouts and retries
- Overload control mechanisms

The simulation is **event-driven**:

- The simulation clock jumps from one event to the next
- All state changes occur via explicit event handlers

---

## Performance Metrics

The simulator is designed to measure the following metrics:

- Average response time
- Throughput
- Goodput (requests completed before timeout)
- Badput (requests completed after timeout)
- Request drop rate
- Average core utilization
- Tail latency (95th / 99th percentile response time)

At least one metric is reported with **confidence intervals** using
independent simulation runs.

---

## How the Simulation Works (High-Level)

1. Users generate requests after a think time
2. Requests arrive at the web server
3. If threads are available, a request starts execution
4. Requests are scheduled on cores using a scheduling policy
5. Requests either:
   - complete successfully
   - time out
   - are dropped due to overload

6. Metrics are collected during the run
7. The initial transient (warm-up period) is discarded

---

## How to Run (Current State)

At this stage, the repository contains **boilerplate code**.

---

## Planned Extensions Beyond the Assignment Baseline

In addition to the required features, the simulator is designed to support:

- Explicit context switch events
- Request retry policies
- Overload control mechanisms (e.g., queue-based dropping)
- Alternative scheduling policies (FIFO vs Round-Robin)
- Tail latency analysis
- Warm-up sensitivity studies
- Scalability what-if experiments

These extensions are intended to strengthen analysis and improve grading.

---

## TODO List

### Core Simulation

- [] Implement the event queue and simulation clock
- [] Implement request arrival, execution, completion, and timeout events
- [] Add explicit context switch events

### System Model

- [] Implement thread allocation and release logic
- [] Track per-core utilization
- [] Implement overload control policies

### Scheduling

- [] Implement round-robin scheduling
- [] Implement FIFO scheduling for comparison

### Workload Model

- [] Implement closed-loop user behavior
- [] Add configurable think-time distributions
- [] Implement request retry logic

### Metrics & Statistics

- [] Record response times per request
- [] Compute throughput, goodput, and badput
- [] Compute tail latency (p95, p99)
- [] Implement confidence interval computation

### Experiments & Analysis

- [] Vary number of users
- [] Perform warm-up (transient) sensitivity analysis
- [] Perform scalability studies
- [] Compare simulation results with MVA predictions

### Final Submission

- [] Generate plots for all metrics
- [] Prepare PDF slides describing:
  - [] system assumptions
  - [] simulation design
  - [] experiments
  - [] results and insights

---

## Notes for the Demo

- [] Trace logging is supported to show event execution order
- [] During the demo, we will:
  - [] explain event traces
  - [] justify modeling assumptions
  - [] reason about correctness using sample traces

---

## Dependencies

Install required Python packages using:

```bash
pip install -r requirements.txt
```
