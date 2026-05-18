# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

A minimal todo web app for learning purposes — built with Flask and plain HTML forms. Users can create, edit, toggle, and delete todos. Keep it simple and beginner-friendly.

## Commands

```bash
FLASK_DEBUG=1 python app.py   # dev server
pip install flask              # install dependency
```

## Do

- Use standard HTML form POSTs with redirect (Post/Redirect/Get pattern)
- Keep all backend logic in `app.py` — no extra modules unless necessary
- Store data in `todos.json` — no database
- Use Tailwind CDN for styling

## Don't

- Don't add a REST API or JavaScript fetch calls — this app uses full page reloads by design
- Don't introduce a database or ORM
- Don't split into multiple Python files or add frameworks beyond Flask
- Don't add authentication or user accounts
