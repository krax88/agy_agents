# Antigravity Custom Agents Repository (`agy_agents`)

This repository contains custom agent definitions and their complete bundled skills for **Google Antigravity (AGY)**.

Each agent is packaged as a self-contained unit along with the specialized skills, governance frameworks, scripts, design systems, and templates required for its operation.

---

## 🤖 Agents Catalog

### 1. [`senior-ai-advisor`](agents/senior-ai-advisor.md)
* **Role**: Senior Managing Director / Partner in AI Advisory & Principal Enterprise Architect.
* **Core Frameworks**:
  * **DIKW Knowledge Pyramid** (Data $\rightarrow$ Information $\rightarrow$ Knowledge $\rightarrow$ Wisdom)
  * **Decision Governance** (Bain RAPID® & DACI matrices)
  * **Tri-Governance Model** (Corporate, Data, and AI Governance)
* **Model**: Gemini Pro (`pro`)
* **Scope**: Main agent & subagent execution
* **Dedicated Branch**: [`senior-ai-advisor`](../../tree/senior-ai-advisor)

### 2. [`ux-architect`](agents/ux-architect.md)
* **Role**: Principal UX & Product Design Director (Linear / Stripe / Apple / Raycast tier).
* **Core Competencies**:
  * Direct generation of self-contained, high-fidelity interactive HTML wireframes and visual showcases.
  * Perceptual color systems (`OKLCH`, `P3`), 1px hairline surfaces, and fluid typography.
  * 6-State Component Protocol (Empty, Loading, Partial, Ideal, Error, Destructive).
  * WCAG 2.2 AAA accessibility and crisp micro-interaction specifications (<150ms latency).
* **Model**: Inherit (`inherit`)
* **Scope**: Main agent & subagent execution with direct file writing
* **Dedicated Branch**: [`ux-architect`](../../tree/ux-architect)

---

## 🛠️ Bundled Skills Catalog

| Skill | Associated Agent | Description | Location |
| :--- | :--- | :--- | :--- |
| **`ai-architecture-planner`** | `senior-ai-advisor` | C4/system architecture diagrams (Mermaid.js), compute/latency trade-offs, and Tri-Governance technical controls. | [`skills/ai-architecture-planner`](skills/ai-architecture-planner/) |
| **`strategic-roadmap-builder`** | `senior-ai-advisor` | 3-Horizon enterprise AI roadmaps, multi-workstream schedules, capability maturity matrices, and DIKW alignment. | [`skills/strategic-roadmap-builder`](skills/strategic-roadmap-builder/) |
| **`enterprise-transformation-advisor`** | `senior-ai-advisor` | Operating model redesign, organizational AI readiness assessments, change management, and executive alignment. | [`skills/enterprise-transformation-advisor`](skills/enterprise-transformation-advisor/) |
| **`training-workshop-designer`** | `senior-ai-advisor` | Curriculum design for executive masterclasses, prompt engineering bootcamps, and technical AI enablement. | [`skills/training-workshop-designer`](skills/training-workshop-designer/) |
| **`analyze-large-audio`** | `senior-ai-advisor` | Large audio file processing (>20MB) via Gemini Files REST API preserving multimodal context and timestamps. | [`skills/analyze-large-audio`](skills/analyze-large-audio/) |
| **`corporate_research`** | `senior-ai-advisor` | 10-year historical financial analysis, regulatory filings, and competitive benchmarking. | [`skills/corporate_research`](skills/corporate_research/) |
| **`design-tokens-and-theme`** | `ux-architect` | High-end OKLCH/P3 color palettes, dark/light surface tokens, fluid typography, and 8pt/4pt spatial grids. | [`skills/design-tokens-and-theme`](skills/design-tokens-and-theme/) |
| **`ux-component-specs`** | `ux-architect` | Technical UI component blueprints, ARIA accessibility matrices, keyboard traps, and micro-interaction timings. | [`skills/ux-component-specs`](skills/ux-component-specs/) |
| **`ux-journey-and-flows`** | `ux-architect` | User journey state machines, cognitive load checklists (Fitts, Hick, Jakob, Miller), and the 6-state protocol. | [`skills/ux-journey-and-flows`](skills/ux-journey-and-flows/) |

---

## 🚀 Installation & Usage

### Installing Agents into an Antigravity Workspace
To use an agent and its bundled skills in your Antigravity project workspace, clone the repository or checkout the specific branch into your `.agents/` folder:

```bash
# Example: Install the complete ux-architect agent package into .agents/
mkdir -p .agents
git clone -b ux-architect https://github.com/krax88/agy_agents.git .agents/ux_bundle
cp -r .agents/ux_bundle/agents/* .agents/agents/
cp -r .agents/ux_bundle/skills/* .agents/skills/
```

### Invoking Agents
Once installed in `.agents/`, invoke the agents in your Antigravity conversation:
* In UI / Chat: Select `@ux-architect` or `@senior-ai-advisor`.
* In Subagent Delegation: Target `TypeName: ux-architect` or `TypeName: senior-ai-advisor`.
