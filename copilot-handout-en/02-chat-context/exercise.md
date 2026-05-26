# Exercise: Chat & Context Variables

**Time:** 90 min | **Project:** `1205/todo-app/`

---

## Task 1 – Explore Context Variables (20 min)

Open Copilot Chat. Try the following prompts and observe the quality of responses:

**Without context:**

```
Explain how the todos are stored.
```

**With #file:**

```
Explain how the todos are stored. #file:app.py
```

**With #sym:**

```
Explain #sym:func_load_todos and #sym:func_save_todos
```

**Compare:** How do the answers differ?

---

## Task 2 – Using @workspace (20 min)

```
@workspace Where is todos.json read and where is it written?
```

```
@workspace Which Flask routes exist and which ones have tests?
```

```
@workspace Are there code duplicates between app.py and utils.py?
```

**Observe:** What does `@workspace` find that a normal prompt doesn't?

---

## Task 3 – Inline Chat (20 min)

1. Open `app.py`
2. Go to the `/add` route
3. Press `⌘ I` / `Ctrl I`
4. Enter:

```
Add input validation: title must not be empty and not longer than 200 characters.
On error: flash message and redirect back to the form.
```

5. Check the diff – is it correct?
6. `⌘ Enter` to accept or `Esc` to reject

---

## Task 4 – #terminalLastCommand (15 min)

```bash
# Run in terminal:
python -m pytest test_app.py -v
```

If tests fail → in Copilot Chat:

```
#terminalLastCommand
Why is this test failing? How do I fix it?
```

If all tests pass → intentionally break one test:

```python
# test_app.py – temporarily change:
def test_add_todo(client):
    assert False, "Intentional failure"
```

---

## Task 5 – #changes for Code Review (15 min)

Make a small change in `app.py` (e.g. add a comment).  
Then in Copilot Chat:

```
Do a brief code review of my changes. #changes
Are there any issues or suggestions for improvement?
```

---

## Bonus – @github (if repo is on GitHub)

```
@github What open issues are there for this repository?

@github What was last changed in this project?

@github Create a summary of the last 5 commits.
```
