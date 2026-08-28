# Antigravity Custom Agents Repository (`agy_agents`)

This repository contains custom agent definitions and their complete bundled skills for **Google Antigravity (AGY)**.

Each agent is packaged as a self-contained unit along with the specialized skills, governance frameworks, scripts, and templates required for its operation.

---

## 🤖 Agents

### 1. [`senior-ai-advisor`](agents/senior-ai-advisor.md)
* **Role**: Senior Managing Director / Partner in AI Advisory & Principal Enterprise Architect.
* **Core Frameworks**:
  * **DIKW Knowledge Pyramid** (Data $\rightarrow$ Information $\rightarrow$ Knowledge $\rightarrow$ Wisdom)
  * **Decision Governance** (Bain RAPID® & DACI matrices)
  * **Tri-Governance Model** (Corporate, Data, and AI Governance)
* **Model**: Gemini Pro (`pro`)
* **Scope**: Main agent & subagent execution

---

## 🛠️ Bundled Skills

| Skill | Description | Location |
| :--- | :--- | :--- |
| **`ai-architecture-planner`** | C4/system architecture diagrams (Mermaid.js), compute/latency trade-offs, and Tri-Governance technical controls. | [`skills/ai-architecture-planner`](skills/ai-architecture-planner/) |
| **`strategic-roadmap-builder`** | 3-Horizon enterprise AI roadmaps, multi-workstream schedules, capability maturity matrices, and DIKW alignment. | [`skills/strategic-roadmap-builder`](skills/strategic-roadmap-builder/) |
| **`enterprise-transformation-advisor`** | Operating model redesign, organizational AI readiness assessments, change management, and executive alignment. | [`skills/enterprise-transformation-advisor`](skills/enterprise-transformation-advisor/) |
| **`training-workshop-designer`** | Curriculum design for executive masterclasses, prompt engineering bootcamps, and technical AI enablement. | [`skills/training-workshop-designer`](skills/training-workshop-designer/) |
| **`analyze-large-audio`** | Large audio file processing (>20MB) via Gemini Files REST API preserving multimodal context and timestamps. | [`skills/analyze-large-audio`](skills/analyze-large-audio/) |
| **`corporate_research`** | 10-year historical financial analysis, regulatory filings, and competitive benchmarking. | [`skills/corporate_research`](skills/corporate_research/) |

---

## 🚀 Installation & Usage

### Installing an Agent into an Antigravity Workspace
To use the `senior-ai-advisor` agent and its bundled skills in your Antigravity project workspace, clone the repository into your workspace `.agents/` folder:

```bash
# Clone the complete agent package into .agents/
mkdir -p .agents
git clone https://github.com/krax88/agy_agents.git .agents/custom_agents
```

Or copy the agent and skills directly into `.agents/`:
```bash
cp .agents/custom_agents/agents/senior-ai-advisor.md .agents/agents/
cp -r .agents/custom_agents/skills/* .agents/skills/
```

### Invoking the Custom Agent
Once installed, invoke the agent in your Antigravity conversation:
* In UI / Chat: Select `@senior-ai-advisor` or trigger via subagent delegation.
* In Python SDK / Config: Target `agent: senior-ai-advisor`.
