# 🧠 Engine Design Questions & Blind Spots Checklist

This checklist tracks open architectural decisions and blind spots in the engine's design.
You can fill in answers as they become clearer, or link to design notes where needed.

---

## 🔬 1. Component Architecture

- [ ] **How are components stored internally?**
<details><summary>Answer</summary>
Since I want efficient parallelism and simulate large numbers of entities and components to compensate for Python's poor performance, I'll use SoA

Sources:
- https://chatgpt.com/share/67f59196-2fbc-8006-9a8c-51503e7cbd1c
- https://medium.com/@savas/nomad-game-engine-part-4-3-aos-vs-soa-storage-5bec879aa38c
</details>

- [ ] **Are you using SoA (struct-of-arrays), AoS (array-of-structs), or something else?**

<details><summary>Answer</summary>

...

</details>

- [ ] **Will components be centralized or distributed per type/store?**
<details><summary>Answer</summary>

...

</details>

---

## 🔁 2. Command System Internals

- [ ] **What is the lifecycle of a command? (When does it apply?)**
<details><summary>Answer</summary>

...

</details>

- [ ] **Do you queue/batch commands? Deduplicate them?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can commands fail, be rejected, or trigger errors?**
<details><summary>Answer</summary>

...

</details>

---

## 🧵 3. Parallelism & Data Safety

- [ ] **Do systems access snapshots or live data?**
<details><summary>Answer</summary>

...

</details>

- [ ] **How is concurrent mutation avoided or managed?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Do we enforce thread/process boundaries explicitly?**
<details><summary>Answer</summary>

...

</details>

---

## 🎨 4. Rendering Integration

- [ ] **How do systems interact with Ursina's renderer?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Is rendering treated as a system or special case?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can ECS components wrap or update Ursina objects?**
<details><summary>Answer</summary>

...

</details>

---

## 🌍 5. World / Scene Lifecycle

- [ ] **Do you support multiple simultaneous scenes or worlds?**
<details><summary>Answer</summary>

...

</details>

- [ ] **How are scene transitions handled?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can entities persist across scenes?**
<details><summary>Answer</summary>

...

</details>

---

## 🧱 6. Entity & Component Lifecycle

- [ ] **How are entities created and destroyed safely?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can we detect/remove invalid or orphaned components?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Do we support schema migration or versioning for components?**
<details><summary>Answer</summary>

...

</details>

---

## 🧮 7. Scheduler & Tick Order

- [ ] **How are systems prioritized or ordered?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can systems depend on other systems' results?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Are systems grouped into phases (input/simulation/rendering)?**
<details><summary>Answer</summary>

...

</details>

---

## 🧯 8. Error Handling & Fault Tolerance

- [ ] **What happens when a system throws an exception?**
<details><summary>Answer</summary>

...

</details>

- [ ] **How are invalid commands handled (e.g., on dead entities)?**
<details><summary>Answer</summary>

...

</details>

- [ ] **What should happen if a config is hot-reloaded with missing or broken data?**
<details><summary>Answer</summary>

...

</details>

---

## 🧩 9. Extensibility & Plugins

- [ ] **How do developers register custom systems/components/commands?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can mods override core systems cleanly?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Is there a registration lifecycle (e.g., init hooks, teardown)?**
<details><summary>Answer</summary>

...

</details>

---

## 🌐 10. Networking Support (Optional)

- [ ] **Do we support any kind of multiplayer networking?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Can the command/event model support rollback or sync?**
<details><summary>Answer</summary>

...

</details>

---

## 🧠 11. AI & Generative Behavior

- [ ] **Will generative AI logic be handled in systems or separate threads?**
<details><summary>Answer</summary>

...

</details>

- [ ] **Do AI modules need sandboxing or runtime separation?**
<details><summary>Answer</summary>

...

</details>

---

## 📜 12. Scripting Layer

- [ ] **How do we safely allow scripting of events, logic, etc.?**
<details><summary>Answer</summary>

...

</details>

- [ ] **How can we test scripted logic in isolation or dry-run mode?**
<details><summary>Answer</summary>

...

</details>

---

## ✅ Progress Tracking

Once answered, check the boxes! This list doubles as a design board and gap scanner.

