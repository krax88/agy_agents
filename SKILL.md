---
name: ai-architecture-planner
description: Designs technical enterprise AI architectures, generates Mermaid.js C4/system diagrams, calculates model latency and compute/token trade-offs, and enforces DIKW data flows and Tri-Governance technical controls.
---

# AI Architecture Planning & Diagramming Skill

## Core Directives
1. **DIKW Architecture Mapping**: Clearly delineate how data moves through the architecture:
   - *Data Layer*: Source systems, document stores, raw event queues.
   - *Information Layer*: ETL, chunking, embedding generation, vector indices.
   - *Knowledge Layer*: Context routing, semantic caching, agentic orchestration, RAG retrieval.
   - *Wisdom Layer*: Guardrail enforcement, human-in-the-loop feedback, business logic integration.

2. **Tri-Governance Technical Controls**:
   - *Data Governance*: Integration with data catalogs, PII anonymization, lineage tracking.
   - *AI Governance*: Guardrail filters (LlamaGuard, NeMo), hallucination evaluators (Ragas, TruLens), model audit logs.
   - *Corporate Governance*: Zero-data retention agreements, tenant isolation, disaster recovery.

3. **Mermaid Diagram Standards**:
Always produce clear Mermaid diagrams showing data flow and governance checkpoints:

```mermaid
flowchart TB
    subgraph Data_Layer ["1. Data Layer (Raw Assets)"]
        RawDocs[("Unstructured Files / S3")]
        CorpDB[("Enterprise ERP / SQL")]
    end

    subgraph Information_Layer ["2. Information Layer (Structured Context)"]
        Parser["Parser & PII Masking Engine"]
        Embeddings["Embedding Model"]
        VectorDB[("Vector & Graph Store")]
    end

    subgraph Knowledge_Layer ["3. Knowledge Layer (Reasoning & Orchestration)"]
        Orchestrator["Agent Orchestrator"]
        LLM["Foundation Model Tier"]
    end

    subgraph Wisdom_Layer ["4. Wisdom Layer (Governance & Action)"]
        Guardrails{"AI Guardrails & Compliance"}
        ExecAction["Business Outcome / Decision API"]
        AuditLog[("Immutable Audit & Lineage Log")]
    end

    RawDocs --> Parser --> Embeddings --> VectorDB
    CorpDB --> Parser
    VectorDB --> Orchestrator
    Orchestrator <--> LLM
    Orchestrator --> Guardrails
    Guardrails -->|Passed| ExecAction
    Guardrails -->|Telemetry| AuditLog
```
