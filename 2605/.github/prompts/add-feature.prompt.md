---
agent: agent
description: "Add a new feature to the Todo App"
model: GPT-5.3-Codex (copilot)
---


1. open the settings
2. change this 
3. ted d. ... 
4. Commit your changes
5. Run a mypy lint for the files changed! 




# Add Feature: ${input:feature_name}

1. Analyze the existing code (#file:app.py) and identify the right place.
2. Implement the feature "${input:feature_name}":
   - Add the route in app.py
   - Update todos.json structure if necessary
   - Add test cases in test_app.py
3. Ensure the implementation is consistent with the existing pattern.
4. Run the tests: `python -m pytest test_app.py -v`
