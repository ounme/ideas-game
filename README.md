# ideas-game

*Agent‑based simulation of idea propagation through personality psychology*

## 🗺️ Quick Navigation

```text
┌─────────────────────────────────────────────────────────┐
│                     ideas-game                           │
│            Ideas Propagation Simulator                   │
└─────────────────────────────────────────────────────────┘

📖 BELIVEME.md  →  What is this? (Concept & Vision)
📘 README.md    →  How to use?  (This file)
🤝 HELPME.md    →  How to help? (Contribute)
💻 main.py      →  Source code  (Implementation)
```

**🌍 Available Languages:**
[English](README.md) | [Русский](BELIVEME.md#beliveme) | [Deutsch](README-Deutsch.md) | [Français](README-Français.md) | [Español](README-Español.md) | [中文](README-中文.md) | [日本語](README-日本語.md) | [한국어](README-한국어.md) | [עברית](README-עברית.md)


## Overview

**ideasgame** models how ideas spread, transform, and shape communities. The engine combines:
- **Personality traits** (OCEAN + Intelligence);  
- **Idea dynamics** (content, emotional tone, distortion);  
- **Social mechanisms** (influence, adaptation, evolution).

## Key Components

### 1. `Idea` Class
Represents a propagable concept with:
- `core`: textual essence;  
- `effects`: parameter impacts (e.g., `{'C': +8, 'A': +5}`);  
- `complexity`: 0–100 (affects distortion during transmission);  
- `emotion`: emotional tone (e.g., "reverence");  
- `weight`: idea’s strength in the community (grows with adoption).

### 2. `Agent` Class
Each agent has 6 traits (0–100):
- **O** (Openness) — receptiveness to new experiences;  
- **C** (Conscientiousness) — rule‑following, reliability;  
- **E** (Extraversion) — social activity;  
- **A** (Agreeableness) — empathy, kindness;  
- **N** (Neuroticism) — sensitivity to threats;  
- **I** (Intelligence) — critical thinking.

**Core methods**:
- `calculate_social_weight()`: computes influence (E×0.4 + C×0.3 + I×0.3);  
- `transmit_idea()`: sends idea with distortion and adaptation;  
- `adapt_idea()`: modifies idea based on source/recipient traits;  
- `receive_idea()`: applies effects with filters (e.g., high C resists negative changes);  
- `evolve_idea()`: updates idea complexity and emotion post‑transmission.

### 3. `Community` Class
Manages the agent population and simulation:
- `add_idea()`: injects new ideas into the system;  
- `step()`: runs one simulation cycle (source → recipient selection → transmission → update);  
- `update_history()`: records average trait values;  
- `plot_history()`: visualizes parameter trends.

## Simulation Workflow

1. **Initialization**  
   - Create `Community(size=N)`;  
   - Add initial `Idea` instances.

2. **Cycle (`step()`)**  
   a. Random **source agent** selected (must hold ideas);  
   b. Random **idea** chosen from source’s beliefs;  
   c. **Recipient** selected via weighted probability (source’s E × recipient’s A);  
   d. **Transmission**:  
      - Distortion applied (based on idea complexity and source I);  
      - Idea adapted to source/recipient traits;  
      - Recipient updates traits and adopts idea;  
      - Idea evolves (complexity/emotion changes).  
   e. Trait averages logged.

3. **Termination**  
   - After `num_steps`, plot results and print statistics.


## Output

1. **Console Log**  
   ```
   Шаг 0: средний O=49.4, C=48.9, E=50.0  
   ...  
   Симуляция завершена (100 шагов).
   ```

2. **Graphs**  
   - Line chart of average OCEAN+I values over steps.

3. **Final Statistics**  
   - Mean/min/max for each trait across agents;  
   - Idea adoption rates (e.g., *"Соблюдай завет": 22/30 agents*);  
   - Top 5 social leaders (by `social_weight`).


## Usage

1. **Install dependencies**  
   ```bash
   pip install matplotlib
   ```

2. **Run simulation**  
   ```bash
   python main.py
   ```

3. **Customize**  
   - Modify `Community(size)` and initial ideas in the `__main__` block;  
   - Adjust idea `effects`, `complexity`, and `emotion` values.

## Parameters & Tuning

- **Agent traits**: Initialized randomly within ranges (e.g., O: 30–70);  
- **Distortion**: `±0.1 × (complexity / 100)`, reduced by source I, increased by recipient N;  
- **Adaptation rules**:  
  - High A (source) → softens core text;  
  - Low O (recipient) → lowers complexity;  
  - High N (recipient) → intensifies emotion;  
- **Idea evolution**: `weight × 1.01` per transmission; complexity ±5% based on source O.


## License

MIT License. See `LICENSE` file.  
Copyright (c) 2024 Nickita Panin  
*Dedicated to the glory of God.*


## Contributing

See `HELPME.md` for ways to improve code, documentation, or share the project.


---

## MIT License

Copyright (c) 2024 Nickita Panin  
This project is dedicated to the glory of God.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
