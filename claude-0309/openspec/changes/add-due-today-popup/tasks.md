## 1. Backend: compute due-today todos

- [ ] 1.1 In `app.py`'s `index()` view, compute `due_today` (incomplete todos whose `due_date` equals today's date, using the same `today` value already used for `overdue`) and pass it to `render_template`
- [ ] 1.2 Verify by adding a test in `test_app.py` that creates a todo with `due_date` set to today and asserts the response context/HTML reflects it is due today (and a done todo with the same due date is excluded)

## 2. Frontend: popup markup

- [ ] 2.1 In `templates/index.html`, add a `<dialog open>` block, rendered only `{% if due_today %}`, listing each due-today todo's text, with a `<form method="dialog"><button>Close</button></form>` to dismiss it without JavaScript
- [ ] 2.2 Verify by running the dev server (`FLASK_DEBUG=1 python app.py`), adding a todo due today, reloading `/`, and confirming the popup appears listing it and the "Close" button dismisses it without a page reload

## 3. Regression checks

- [ ] 3.1 Verify no popup appears when no todo is due today (existing todos with past/future due dates only) — manual check plus a `test_app.py` case
- [ ] 3.2 Verify no popup appears when the only todo due today is marked done — manual check plus a `test_app.py` case
- [ ] 3.3 Run the full test suite (`python -m pytest`) and confirm all tests pass, including the pre-existing `overdue`/edit/add/delete tests
