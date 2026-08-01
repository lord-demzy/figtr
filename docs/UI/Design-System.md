# FIGTR — Design System

## Purpose

This document defines the design system for the FIGTR frontend. It establishes a consistent visual language, component standards, and UX guidelines to ensure a cohesive, professional, and accessible user experience across all roles and modules.

## Design Principles

1. **Clarity** — Interfaces are simple, intuitive, and reduce cognitive load.
2. **Consistency** — Reusable components and patterns are used consistently.
3. **Accessibility** — All interfaces are accessible (WCAG 2.1 AA as a target).
4. **Efficiency** — Common tasks are fast and require minimal steps.
5. **Brand Trust** — A professional, trustworthy visual identity appropriate for educational institutions.

## Technology

- **Framework:** Next.js (React) — placeholder, to be finalized.
- **Styling:** CSS Modules / Tailwind CSS / styled-components — **to be decided**.
- **Component Library:** Custom components built on the design tokens below — **to be decided**.

## Design Tokens

Design tokens are the foundational values (colors, typography, spacing) used across the UI.

### Color Palette

| Token            | Purpose                          | Value (placeholder) |
|------------------|----------------------------------|---------------------|
| `--color-primary`      | Primary actions, links      | `#2563EB` (blue)    |
| `--color-primary-hover`| Primary hover state        | `#1D4ED8`           |
| `--color-secondary`    | Secondary actions          | `#64748B` (slate)   |
| `--color-success`      | Success states             | `#16A34A` (green)   |
| `--color-warning`      | Warning states             | `#D97706` (amber)   |
| `--color-danger`       | Error/destructive states   | `#DC2626` (red)     |
| `--color-background`   | Page background            | `#F8FAFC`           |
| `--color-surface`      | Cards, panels             | `#FFFFFF`           |
| `--color-text`         | Primary text               | `#0F172A`           |
| `--color-text-muted`   | Secondary text             | `#64748B`           |
| `--color-border`       | Borders, dividers          | `#E2E8F0`           |

> **Note:** Final color values are placeholders and will be finalized during the design phase.

### Typography

| Token                | Purpose            | Value (placeholder) |
|----------------------|--------------------|---------------------|
| `--font-family`      | Default font       | System font stack   |
| `--font-size-xs`     | Small labels       | `12px`              |
| `--font-size-sm`     | Body secondary     | `14px`              |
| `--font-size-base`   | Body text          | `16px`              |
| `--font-size-lg`     | Section headings   | `20px`              |
| `--font-size-xl`     | Page headings      | `24px`              |
| `--font-size-2xl`    | Display            | `32px`              |

### Spacing

Use a **4px base spacing scale**:

| Token | Value |
|-------|-------|
| `--space-1` | `4px`  |
| `--space-2` | `8px`  |
| `--space-3` | `12px` |
| `--space-4` | `16px` |
| `--space-6` | `24px` |
| `--space-8` | `32px` |
| `--space-12`| `48px` |
| `--space-16`| `64px` |

### Border Radius

| Token | Value |
|-------|-------|
| `--radius-sm` | `4px`  |
| `--radius-md` | `8px`  |
| `--radius-lg` | `12px` |
| `--radius-full` | `9999px` |

### Shadows

| Token | Value |
|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.07)` |
| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` |

## Component Standards

### Buttons

- **Primary** — for main actions.
- **Secondary** — for alternative actions.
- **Danger** — for destructive actions.
- **Ghost/Text** — for low-emphasis actions.
- Include loading, disabled, and focus states.

### Forms & Inputs

- Consistent label, input, error, and helper text patterns.
- Clear focus states.
- Validation errors shown inline, near the field.
- Accessible labels and error announcements.

### Tables

- Used for structured data.
- Support sorting, filtering, and pagination.
- Clear column headers and consistent alignment.

### Cards

- Used to group related content.
- Consistent padding, border, and shadow.

### Modals & Dialogs

- Used for focused tasks or confirmations.
- Accessible focus management and keyboard support.
- Clear title, content, and action buttons.

### Navigation

- Consistent sidebar/topbar layout.
- Clear active states and hierarchy.

### Feedback

- **Toasts/Notifications** — for transient success/error messages.
- **Inline Alerts** — for persistent messages within a page.
- **Empty States** — helpful guidance when no data exists.

## Layout

- **Responsive** — mobile-first, works across breakpoints.
- **Breakpoints (placeholder):**
  - `sm`: 640px
  - `md`: 768px
  - `lg`: 1024px
  - `xl`: 1280px
- Consistent max-width container and grid spacing.

## Accessibility

- Semantic HTML (proper headings, landmarks).
- Keyboard navigable.
- Sufficient color contrast (WCAG AA).
- Focus states clearly visible.
- ARIA attributes where needed.

## Iconography

- Use a consistent icon set (e.g., Lucide, Heroicons — **to be decided**).
- Icons are decorative or have accessible labels.

## Theming & Multi-Tenant Branding

- Each tenant (school) may have custom branding (logo, primary color).
- The design system supports theming via CSS custom properties.
- Tenant branding is applied at the app level, not per-component.

## Implementation Guidelines

- All components are built as **reusable** components in the frontend.
- Design tokens are defined as CSS custom properties (or equivalent).
- Components follow the patterns in `docs/Architecture/Development-Standards.md`.

---

*This document is a living artifact and will be refined during the design phase.*