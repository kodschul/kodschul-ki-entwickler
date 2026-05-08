---
name: code-fixer
description: Describe what this custom agent does and when to use it.
argument-hint: The inputs this agent expects, e.g., "a task to implement" or "a question to answer".

# Claude model options (Anthropic via GitHub Copilot):
# model: claude-sonnet-4-5      ← Claude Sonnet 4.5  (latest, fast + smart)
# model: claude-3-7-sonnet      ← Claude 3.7 Sonnet  (extended thinking)
# model: claude-3-5-sonnet      ← Claude 3.5 Sonnet  (stable)
# model: claude-opus-4          ← Claude Opus 4      (most powerful)
#
# Other available models:
# model: gpt-4o                 ← GPT-4o  (OpenAI)
# model: gpt-4.1                ← GPT-4.1 (OpenAI)
# model: o3                     ← o3      (OpenAI reasoning)
# model: gemini-2.0-flash       ← Gemini 2.0 Flash (Google)
model: claude-sonnet-4-5

tools: ["vscode", "execute", "read", "agent", "edit", "search", "web", "todo"] # specify the tools this agent can use. If not set, all enabled tools are allowed.
# tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo'] # specify the tools this agent can use. If not set, all enabled tools are allowed.
---

<!-- Tip: Use /create-agent in chat to generate content with agent assistance -->

Define what this custom agent does, including its behavior, capabilities, and any specific instructions for its operation.
