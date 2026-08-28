---
name: design-tokens-and-theme
description: Generates high-end design token systems, OKLCH/P3 color palettes, dark/light surface logic, fluid typography, and spatial rules.
---

# Design Tokens & Visual Profile Engineering

## 1. Color Palette Philosophy (Crisp & High-End)
- Prefer `oklch()` or `hsl()` for perceptual uniformity across hues.
- Avoid pure black `#000000` backgrounds in dark mode. Use deep slate / neutral darks (`oklch(0.14 0.01 260)`) with elevated, subtly lighter layered surfaces.
- Use 1-pixel border hairlines (`border border-white/[0.08]` or `border-black/[0.06]`) to create depth without heavy drop-shadows.

### Example Design Token Matrix
```css
:root {
  /* Primitive Colors (Light Mode) */
  --bg-canvas: oklch(0.99 0.002 240);
  --bg-surface: oklch(0.96 0.005 240);
  --bg-surface-raised: oklch(1 0 0);
  
  --stroke-subtle: oklch(0.90 0.005 240);
  --stroke-strong: oklch(0.75 0.01 240);
  
  --text-primary: oklch(0.18 0.02 260);
  --text-secondary: oklch(0.45 0.02 260);
  --text-tertiary: oklch(0.65 0.01 260);
  
  --accent-primary: oklch(0.55 0.22 260);     /* Electric Indigo */
  --accent-primary-hover: oklch(0.48 0.24 260);
  
  /* Spacing Grid (8pt baseline with 4pt sub-grid) */
  --space-1: 0.25rem; /* 4px */
  --space-2: 0.5rem;  /* 8px */
  --space-3: 0.75rem; /* 12px */
  --space-4: 1.0rem;  /* 16px */
  --space-6: 1.5rem;  /* 24px */
  --space-8: 2.0rem;  /* 32px */
  
  /* Typography Scale */
  --font-sans: 'Inter\, -apple-system, BlinkMacSystemFont, 'Segoe UI\, Roboto, sans-serif;
  --font-mono: 'JetBrains Mono\, ui-monospace, monospace;
  
  --text-xs: 0.75rem;     /* 12px | Line-height: 1.0rem */
  --text-sm: 0.875rem;    /* 14px | Line-height: 1.25rem */
  --text-base: 1.0rem;     /* 16px | Line-height: 1.5rem */
  --text-lg: 1.125rem;    /* 18px | Line-height: 1.75rem */
  --text-xl: 1.25rem;     /* 20px | Line-height: 1.75rem */
  --text-2xl: 1.5rem;     /* 24px | Line-height: 2.0rem */
}

[data-theme="dark"] {
  --bg-canvas: oklch(0.12 0.01 260);
  --bg-surface: oklch(0.16 0.012 260);
  --bg-surface-raised: oklch(0.20 0.015 260);
  
  --stroke-subtle: oklch(0.24 0.01 260);
  --stroke-strong: oklch(0.35 0.015 260);
  
  --text-primary: oklch(0.96 0.005 240);
  --text-secondary: oklch(0.70 0.01 240);
  --text-tertiary: oklch(0.50 0.01 240);
}
```

## 2. Micro-Interactions & Animation Specs
- **Clickable Elements**: `transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1)`
- **Modals / Drawers**: `transition: transform 200ms cubic-bezier(0.32, 0.72, 0, 1), opacity 200ms ease`
- **Active / Press**: `transform: scale(0.98)` for tactile, physical push-down feedback.
