# 04 – Configuration

**Block:** 60 min | **Day 1**

---

## Three Configuration Levels

GitHub Copilot has three levels of configuration that build on each other:

```
Level 1 (Global):  VS Code User settings.json + global instructions
Level 2 (Project): .github/copilot-instructions.md + .vscode/settings.json
Level 3 (File):    .github/instructions/*.instructions.md (applyTo-specific)
```

> More specific settings always override more general ones.

---

## copilot-instructions.md – Project Context

**Location:** `.github/copilot-instructions.md`  
**Read automatically:** Always, for every chat in this project.  
**Format:** Markdown

**Recommended structure:**

```markdown
# GitHub Copilot Instructions

## Project Goal

[One sentence – what does the app do?]

## Tech Stack

[Languages, Frameworks, Libraries]

## Commands

[How to start/test the app]

## Do

[Active rules: use X, always do Y]

## Don't

[Prohibitions: never use Z, no X]

## Architecture

[Data flow, folder structure, key decisions]
```

**Important:** Keep under 80 lines! Longer files cost more tokens and reduce quality.

---

## .vscode/settings.json – All Copilot Options

```json
{
  // ── Code Generation ──────────────────────────────────────
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/instructions/python.instructions.md" },
    { "text": "Always write type annotations for new functions." }
  ],

  // ── Test Generation ───────────────────────────────────────
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Use pytest. Create: 1 happy path, 1 empty input, 1 edge case. Name: test_what_when_expected."
    }
  ],

  // ── Code Review ────────────────────────────────────────────
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": ".github/instructions/security.instructions.md" }
  ],

  // ── Commit Messages ────────────────────────────────────────
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "text": "Use Conventional Commits: feat/fix/chore/docs/test. Max 72 chars in subject. Reference issue number if available."
    }
  ],

  // ── Enable/Disable by Language ────────────────────────────
  "github.copilot.enable": {
    "*": true,
    "markdown": false,
    "plaintext": false
  },

  // ── Language for Copilot Responses ────────────────────────
  "github.copilot.chat.localeOverride": "en"
}
```

---

## Commit Message Generation

1. Open Source Control panel (`⌘ Shift G`)
2. Stage files (`git add`)
3. Click the ✨ sparkle icon in the commit message field
4. Copilot generates a commit message based on the diff

**Configure:**

```json
"github.copilot.chat.commitMessageGeneration.instructions": [
  {
    "text": "Use Conventional Commits. Max 72 chars. Reference issue number if available."
  }
]
```

---

## Language Settings

| Setting               | Options                     | Effect                              |
| --------------------- | --------------------------- | ----------------------------------- |
| `localeOverride`      | `"en"`, `"de"`, `"fr"`, … | Language for Copilot responses      |
| `copilot.enable`      | `true` / `false` per type  | Enable/disable Ghost Text per type  |

---

## Global vs. Project Settings

| Setting                   | Where                         | Applies to           |
| ------------------------- | ----------------------------- | -------------------- |
| `localeOverride`          | User settings.json            | All projects         |
| `copilot.enable`          | User or project settings.json | All or this project  |
| `codeGeneration.instructions` | Project `.vscode/settings.json` | This project only |
| `copilot-instructions.md` | `.github/` (committed to Git) | This project (team)  |
| `*.instructions.md`       | `.github/instructions/`       | Specific file types  |

---

## Checklist – New Project Setup

```
□ Create .github/copilot-instructions.md
  □ Project goal (1 sentence)
  □ Commands (start/test)
  □ Tech stack
  □ DOs and DON'Ts
  □ Max 80 lines

□ Create .vscode/settings.json
  □ codeGeneration.instructions
  □ testGeneration.instructions
  □ commitMessageGeneration.instructions
  □ localeOverride: "en"

□ Optional: .github/instructions/
  □ python.instructions.md (applyTo: **/*.py)
  □ security.instructions.md (applyTo: **)
  □ test.instructions.md (applyTo: **/test_*.py)
```
