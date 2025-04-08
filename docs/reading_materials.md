# 🧠 ECS Deep Dive Study Plan (Reading-First with Practice Anchors)

This plan merges essential ECS literature, talks, and system documentation with structured thematic chapters and practical goals to build a solid conceptual foundation before implementation.

---

## 📘 Chapter 1: ECS Design & Motivation

**📚 Read:**
- [Game Programming Patterns – Component Pattern](https://gameprogrammingpatterns.com/component.html)
- [The Entity System is the Future of Game Development (Tony Albrecht)](https://www.gamedevs.org/blog/the-entity-system-is-the-future/)
- [Bitsquid on ECS](https://bitsquid.blogspot.com/2015/01/the-entity-component-system-is-dead.html)

**📝 Focus Points:**
- Why do games need ECS over traditional OOP hierarchies?
- What is the core value of decoupling data and behavior?

**🧪 Practice Goal:**
> Sketch the "ideal ECS loop" in pseudocode. Don't code yet—just visualize how systems, entities, and components flow in a tick.

---

## 📘 Chapter 2: Data-Oriented Design & Memory Layout

**📚 Read:**
- [Data-Oriented Design Book by Richard Fabian](https://www.dataorienteddesign.com/dodbook/)
- [Bevy ECS Book (Rust)](https://bevyengine.org/learn/book/introduction/)
- [Flecs Manual](https://github.com/SanderMertens/flecs/blob/master/docs/Manual.md)
- [Specs ECS Guidebook (Rust)](https://slide-rs.github.io/specs/)

**🎥 Watch:**
- [Handmade Hero: ECS and DOD (Casey Muratori)](https://www.youtube.com/watch?v=rX0ItVEVjHc)
- [Flecs ECS Internals (CppCon)](https://www.youtube.com/watch?v=sJ7x9Xb0MXY)

**📝 Focus Points:**
- SoA vs AoS: when and why?
- How do archetypes improve access speed?
- Why is cache coherence critical in ECS?

**🧪 Practice Goal:**
> Draw a small entity/component matrix using both AoS and SoA layouts. Annotate where iteration performance would differ.

---

## 📘 Chapter 3: Component Storage, Querying & Archetypes

**📚 Read:**
- [Making an ECS in C++ (EnTT)](https://skypjack.github.io/2020-08-02-ecs-baf-part-1/)
- [EnTT Wiki](https://github.com/skypjack/entt/wiki)
- [Legion ECS Docs](https://docs.rs/legion/latest/legion/index.html)
- [Artemis-ODB Wiki](https://github.com/junkdog/artemis-odb/wiki)

**📝 Focus Points:**
- How do different ECS engines organize storage?
- What makes query systems fast?
- Sparse sets vs archetypes?

**🧪 Practice Goal:**
> Describe or sketch how your ECS would filter entities with [Position, Velocity] using SoA or archetypes.

---

## 📘 Chapter 4: System Scheduling & Parallel Execution

**📚 Read:**
- [Unity Entities 1.4 – Concepts & Scheduling](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/concepts-intro.html)
- [Bevy Book – Scheduling Systems](https://bevyengine.org/learn/book/introduction/)
- [Flecs ECS Articles](https://www.flecs.dev/flecs/articles/)

**🎥 Watch:**
- [Unity DOTS ECS Architecture (GDC 2019)](https://www.youtube.com/watch?v=p65Yt20pw0g)
- [Inkle Studios – Data-Oriented Design 101 (GDC)](https://www.youtube.com/watch?v=rzb6O8jcMUg)

**📝 Focus Points:**
- How do ECS systems run in parallel safely?
- What are system dependencies and sync points?
- What’s a system graph / DAG?

**🧪 Practice Goal:**
> Draw a simple system graph (nodes = systems, edges = order or data conflict). Mark which can run in parallel.

---

## 📘 Chapter 5: Commands, Versioning, and Change Tracking

**📚 Read:**
- [Shipyard ECS Internals](https://leudz.github.io/shipyard/current/shipyard/index.html)
- [Specs ECS Guidebook](https://slide-rs.github.io/specs/)

**📝 Focus Points:**
- What are command buffers?
- Why apply commands at end-of-frame?
- How does versioning help avoid work?

**🧪 Practice Goal:**
> Draft a flow diagram: system runs → emits commands → world applies them → component versions update.

---

## 📘 Chapter 6: Async, Timesteps, Events & Desync

**📚 Read:**
- [Real-Time Rendering – ECS + DOD principles](http://www.realtimerendering.com/)
- [Game Engine Architecture (Jason Gregory) – Game Object Models](https://www.gameenginebook.com/)

**🎥 Watch:**
- [How Unity’s DOTS ECS Works – Code Monkey](https://www.youtube.com/watch?v=ILfZIEQba3s)

**📝 Focus Points:**
- Which systems need to run every frame?
- How can you run AI or audio less frequently?
- What’s the fixed timestep loop?

**🧪 Practice Goal:**
> Pick 5 common systems in a game and assign how often they should realistically run (e.g. Physics: 60Hz, AI: 5Hz).

---

## 📘 Chapter 7: Python Performance & Tooling Essentials

**📚 Read:**
- [Python threading module](https://docs.python.org/3/library/threading.html)
- [multiprocessing shared_memory](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
- [asyncio – Python Docs](https://docs.python.org/3/library/asyncio.html)
- [Cython Docs](https://cython.readthedocs.io/en/latest/)

**📝 Focus Points:**
- GIL limitations for CPU-bound tasks
- When to use async vs threads vs processes
- Native-speed extensions (Cython, NumPy)

**🧪 Practice Goal:**
> Write out what parts of your eventual ECS should be parallelized (and *how*—threads, procs, async, or native).

---