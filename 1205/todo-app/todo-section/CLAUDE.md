# CLAUDE.md

## Project Goal

A minimal todo web app section — Flask backend, plain HTML forms, Tailwind CSS via CDN. Supports create, edit, toggle, and delete. Beginner-friendly.

## Commands

```bash
cd todo-section
FLASK_DEBUG=1 python app.py   # runs on port 5001
pip install flask
```

## Do

- Use Post/Redirect/Get pattern for all form submissions
- Keep all logic in `app.py`
- Store todos in `todos.json`
- Use Tailwind CDN for styling

## Don't

- Don't add a REST API or JavaScript fetch calls
- Don't add a database or ORM
- Don't split into multiple Python files
- Don't add authentication
