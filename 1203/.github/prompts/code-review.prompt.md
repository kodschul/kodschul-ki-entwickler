---
name: code-review
description: CUSTOM when reviewing code, use this prompt to generate comprehensive feedback and suggestions for improvement.

# Claude model options (Anthropic via GitHub Copilot):
# model: claude-sonnet-4-5      ← Claude Sonnet 4.5  (latest, fast + smart)
# model: claude-3-7-sonnet      ← Claude 3.7 Sonnet  (extended thinking)
# model: claude-3-5-sonnet      ← Claude 3.5 Sonnet  (stable)
# model: claude-opus-4          ← Claude Opus 4      (most powerful)
#
# Other available models:
# model: gpt-4o                 ← GPT-4o  (OpenAI)
# model: gpt-4.1                ← GPT-4.1 (OpenAI)
# model: GPT-4.1 (copilot)      ← GPT-4.1 via Copilot (original value here)
# model: o3                     ← o3      (OpenAI reasoning)
# model: gemini-2.0-flash       ← Gemini 2.0 Flash (Google)
model: claude-sonnet-4-5
---

<!-- Tip: Use /create-prompt in chat to generate content with agent assistance -->

check if the code is readable and follows best practices for naming, formatting, and organization.

- Provide specific examples of any issues found and suggest improvements.
- Consider edge cases and potential bugs that may arise from the current implementation.

add the suggestions directly as code comments in the provided code snippet, using clear and concise language to explain the reasoning behind each suggestion.
