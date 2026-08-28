---
name: ux-component-specs
description: Technical UI/UX specifications for engineering handoff, accessibility checklists, ARIA roles, and component layout matrices.
---

# Technical UX & Engineering Handoff Specifications

## 1. Specification Template
When documenting a UI component or page layout, output the specification in this standardized schema:

### Component: `[Component Name]`

#### 1. Visual Layout Blueprint (ASCII / Schematic)
```text
+-----------------------------------------------------------------------+
| [Icon] Title Header                             [Badge] [Close Button]|
+-----------------------------------------------------------------------+
| Body Content Area (Dense, clear hierarchy)                            |
| • Subtext label: 14px / text-secondary                                |
| • Primary data point: 24px / tabular-nums / text-primary              |
+-----------------------------------------------------------------------+
| [ Secondary Action (Ghost) ]              [ Primary Action (Solid) ]  |
+-----------------------------------------------------------------------+
```

#### 2. Layout & Spacing Matrix
- **Container**: `padding: 24px`, `border-radius: 12px`, `border: 1px solid var(--stroke-subtle)`
- **Gap**: `16px` between logical sections.
- **Action Cluster**: Right-aligned, `gap: 8px`.

#### 3. State & Micro-Interaction Rules
| State | Visual Behavior | Transition |
|---|---|---|
| **Rest** | Surface background, subtle stroke | — |
| **Hover** | Surface lifts (`var(--bg-surface-raised)`), stroke intensifies | 150ms `ease-out` |
| **Active** | `scale(0.98)`, slight inset shadow | 80ms `ease-out` |
| **Focus-Visible** | 2px solid `var(--accent-primary)`, `offset: 2px` | Instant |
| **Disabled** | `opacity: 0.4`, `cursor: not-allowed` | — |

#### 4. Accessibility & Semantics (WCAG 2.2 AAA Compliance)
- **ARIA Roles**: `role="dialog"` or `role="region"`, `aria-labelledby="[id]"`.
- **Keyboard Navigation**:
  - `Tab` / `Shift+Tab`: Cycles through interactive elements within focus trap.
  - `Escape`: Closes modal / cancels active state and restores focus to triggering element.
  - `Enter` / `Space`: Activates primary CTA.
- **Screen Reader Announcements**: `aria-live="polite"` on status or error changes.
