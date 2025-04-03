# Execution Strategy and Scheduling Policy Design

## Overview
This document outlines the execution strategy and scheduling philosophy adopted for the ECS engine. It is designed to ensure predictability, scalability across hardware configurations, and empower system developers to make informed choices.

## Philosophy
The core principle is **developer-guided, hardware-aware execution**. The engine does not make runtime decisions about execution policy but instead commits to a single scheduling strategy per system after evaluating the underlying hardware at startup. Tick rates, however, can be adapted at runtime based on global performance metrics such as CPU utilization.

## Goals
- **Predictable Execution**: Systems behave consistently throughout runtime.
- **Developer Control**: System authors declare how their systems should run.
- **Hardware Awareness**: Engine adapts to different hardware configurations once at startup.
- **Simplified Debugging**: No runtime execution policy shifts means easier profiling and testing.
- **Dynamic Responsiveness**: Tick rates can adjust dynamically based on performance conditions.

## Definitions
- **Execution Policy**: The developer-declared or config-resolved preferred execution method for a system.
    - `sync`: Runs on the main thread.
    - `thread`: Runs in a thread pool.
    - `process`: Runs in a separate process.
    - `async`: Runs as an asyncio coroutine.

- **Tick Rate / Tick Range**: Determines how frequently a system is updated. Adjustable at runtime. Can be defined as:
    - Fixed interval (e.g., every 3 ticks)
    - Conditional interval based on performance metrics (e.g., adjust rate under high CPU load)

- **Auto-optimize Flag**: Optional hint for tick rate adjustment (not execution policy).

- **System Hardware Conditions**: Rules applied at startup for setting system execution policy based on hardware profile. Example conditions:
    - `low_core_count` for <= 2 cores
    - `low_memory` for < 4GB RAM
    - `battery_powered` (optional, platform-dependent)

- **Runtime Load Scenario Tags**: Named global performance conditions that can be mapped to CPU utilization bands (e.g., `low_load`, `high_cpu_scenario`) and used for synchronizing tick policy changes across systems.

## Design Decisions

### 1. Execution Policy Declaration
Each system can declare an execution policy map with hardware condition overrides. Example:
```python
@system(execution_policy={
    "low_core_count": "sync",
    "default": "process"
}, priority="high")
class AISystem(System):
    ...
```

### 2. One-Time Hardware Scan
At engine startup, hardware information is scanned:
- CPU core count
- RAM availability
- Platform info (optional: thermal or battery constraints)

This data is used to determine relevant conditions (e.g., `low_core_count`) and resolve each system’s final execution policy from its defined configuration.

### 3. No Runtime Execution Policy Changes
Execution mode is **finalized at startup** and will not change during runtime.
This ensures stable performance, consistent profiling, and avoids the need to write systems that behave correctly across multiple strategies.

### 4. Runtime Tick Rate Control (CPU-Aware)
Systems may define conditional tick multipliers tied to global performance tags or CPU utilization bands. The engine monitors overall CPU usage and dynamically activates one of the defined tick schedules.

Example:
```python
tick_policy = {
    "low_cpu_scenario": 4,
    "high_cpu_scenario": 1,
    "default": 2
}
```

These tags are resolved centrally based on runtime profiling and shared across all systems to ensure consistent tick scaling.

### 5. Central Configuration Base (Optional)
You may define a base class or configuration module such as `EngineStartupConfig` to hold:
- Finalized thread/process pool sizes
- Adjusted execution policies
- System classification
- Tick rate mappings for each performance band

### 6. Developer Profiling and Optimization Tools
To aid performance tuning and debugging, the engine will provide the following tools:

#### a. **System Execution Time Profiler**
Logs execution time (ms) per system per tick, including:
- System name
- Tick number
- Execution mode
- Tick multiplier
- Measured duration

#### b. **System Tick Trace Recorder**
Tracks whether each system ran or was skipped for every tick. Helps verify tick schedules and coordination.

#### c. **Tick Rate Transition Logger**
Logs when the global CPU scenario tag changes, including the new tick rates applied to systems.

#### d. **Command Execution Timeline**
Tracks when and which system emitted each command, along with its target entity. Useful for causal tracing and replay.

#### e. **Real-Time Monitoring Panel** (Optional)
A live dashboard that shows:
- Tick count per system
- Active tick multiplier
- Current performance scenario
- Pool/thread usage and average load

#### f. **Replayable Performance Sessions** (Optional)
Supports recording tick + execution data for offline replay or diagnosis.

## Sample Adjustments
```python
hardware_profile = detect_hardware()
if hardware_profile.core_count <= 2:
    hardware_flags.add("low_core_count")

resolved_policy = system.execution_policy.get("low_core_count") or system.execution_policy.get("default")
system.execution_mode = resolved_policy

# Later during runtime
current_scenario = evaluate_cpu_load()
tick_multiplier = system.tick_policy.get(current_scenario) or system.tick_policy.get("default")
```

## Benefits
- **Cross-device portability**
- **Stable development and debugging experience**
- **Improved scalability** while preserving developer intent
- **Synchronized tick scaling across systems under load**
- **Reduced CPU strain under dynamic load without full execution policy shifts**
- **Full visibility for profiling and tuning**

## Future Possibilities
This model supports gradual evolution:
- Add a benchmarking stage at startup
- Allow config overrides via CLI or launcher GUI
- Persist tuned settings across sessions
- Visualize tick rate changes and CPU conditions for debugging

## Summary
This execution policy model empowers developers to express how systems run, while also ensuring the engine remains responsive to varying hardware without introducing the complexity of runtime strategy shifts. It balances explicit control with startup-time intelligence for robust and scalable behavior.

Runtime tick multipliers can be adjusted based on global CPU load, using named performance scenarios that are evaluated centrally and applied across systems consistently. Developers are supported with profiling, execution tracing, and runtime debugging tools to fine-tune behavior and catch regressions early.

