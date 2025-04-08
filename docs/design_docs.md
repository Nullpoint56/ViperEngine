# 🧠 Engine Design Document: Vision & Philosophy

## 🧭 Overview

This engine is a **fully Python-based 3D game engine** designed from the ground up with an **Entity-Component-System (ECS)** core that supports **multi-core CPU utilization** across `sync`, `async`, `threaded`, and `process` systems. It integrates **Ursina** for rendering and prioritizes **performance, modding, and debuggability** without sacrificing clarity or Pythonic simplicity.

---

## 🎯 Core Objectives

| Area           | Goal                                                                 |
|----------------|----------------------------------------------------------------------|
| **Language**   | 100% Python; no native bindings or C++ integration                   |
| **ECS Design** | Command-based ECS with full lifecycle tracking and concurrency       |
| **Concurrency**| Multicore execution via thread/process/task scheduler                |
| **Rendering**  | Use Ursina as a plug-and-play backend for 2D/3D                      |
| **Modding**    | Allow deep low-level access via inheritance and scripting extensions |
| **Debugging**  | Transparent, replayable, and inspectable system with audit logs      |
| **Testing**    | Strong testability via system isolation and dry-runs                 |
| **Open Source**| Transparent, extensible, MIT-style licensed                          |

---

## 🔍 Deep Dive: Vision Pillars

### 🧪 1. Debugging & Replayability

The ECS engine's complexity, particularly in a multithreaded/multiprocess environment, demands **full observability**:

- Every **component/entity change** will be **recorded**.
- Changes are tagged with:
  - ✅ Tick number  
  - ✅ System name  
  - ✅ Command that initiated the change
- This data is logged **asynchronously** to file.
- Future tool: a **visual replay viewer** that replays tick-by-tick state changes.
- The replay system will support:
  - Setting breakpoints on specific ticks
  - Debug-stepping through system logic
  - Live comparison between current and recorded sessions
- **Goal**: Make ECS transparent and non-magical to developers.

📝 *TODO*: Define debug tooling for other engine parts (e.g., rendering, asset loading, input system).

---

### 📊 2. Profiling & Performance Analysis

Systems will be profiled via a decorator (or built-in wrapper), collecting:

- ⏱ Time-per-update  
- 🧠 Memory usage (RAM snapshot delta)  
- 🧮 CPU/GPU utilization (where accessible via Python)  
- 📊 Metrics are viewable in a UI tool: sortable by metric

**Challenges:**
- Accurate metrics in a multi-thread/process environment may need platform-dependent workarounds.
- Isolating systems for deeper profiling may require a sandbox mode.

📝 *TODO*: Evaluate `psutil`, `tracemalloc`, or `PyInstrument` for metric collection.  
📝 *TODO*: Decide how/if GPU usage can be profiled with Ursina or wrappers.

---

### ⚙️ 3. Configuration System

Three layers of configs:

1. **Low-level config**:
   - Read-only at runtime
   - Example: scheduler strategy, system execution model overrides
   - Stored in versioned JSON/YAML files

2. **Player-facing config**:
   - Resolution, audio volume, key bindings, etc.
   - Exposed via settings UI
   - Hot-reloadable
   - Systems must react to changes when paused

3. **Future CLI/scripting layer** (maybe):
   - Call engine functions at runtime (like developer consoles)
   - Change any config live, including system toggles and debug values
   - Too ambitious for now, but reserved as a stretch goal

📝 *TODO*: Research runtime injection/subscription model for config changes across threads.

---

### 🧩 4. Modding Support

- Modding supported at the **Python level**.
- Modders can define:
  - New systems (via `BaseSystem`)
  - New commands (via `BaseCommand`)
  - New components, and plug into scheduler
- Base architecture *expects* modding: all logic modular, registered dynamically.
- No sandboxing yet: full Python access is assumed.

📝 *TODO*: Future feature – mod manager for loading/priority/dependency management.

---

### 📁 5. Project Structure & Game Layout

🚧 *In Development – needs further brainstorming*

Early assumptions:

- /systems 
- /components
- /assets
- /configs
- /mods
- /scripts
- /entry.py


- Modders can override or extend systems via file injection or registration.
- Scenes/worlds should be serializable and reloadable.

📝 *TODO*: Define conventions for asset pipelines, game state saves, and scene management.

---

### 🧪 6. Testing & Dry Runs

Testing is core to the engine vision.

- **All systems are designed to be unit-testable**  
  - Pure logic in `update()` methods  
  - Must not directly mutate world state

- **Dry-run mode** will:  
  - Run systems and commands  
  - Apply no state changes  
  - Allow tracing of hypothetical game outcomes

To make this possible:

- Strict separation between `System` logic and command application
- Systems may optionally include `TestDataFactory` to generate mock input

📝 *TODO*: Define tooling or CLI for launching test mode per system.

---

### 🧠 7. AI Simulation Tools

Currently:

- No dedicated AI debugging planned
- AI logic will be tested via standard system unit testing + dry-runs

Future thoughts:

- For generative AI or behavior trees, might eventually visualize AI states or thought paths
- Unclear how much of that belongs in-engine vs as external tools

📝 *TODO*: Investigate testing/debugging for AI scripting layer

---

### 🔐 8. Scripting Layer (Future)

- Will allow scripted gameplay logic and events
- Must be sandboxed/testable
- *Open question*: How do we **test scripts** that interact with core ECS and command flow?

📝 *TODO*: Define safe scripting interfaces  
📝 *TODO*: Design hooks for simulation/test scripting

---