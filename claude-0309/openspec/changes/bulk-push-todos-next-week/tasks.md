## 1. Backend: bulk reschedule route

- [ ] 1.1 In `app.py`, add `POST /push-week`: read `request.form.getlist("ids")`, load todos, for each todo whose `id` is in that list set `due_date` to 7 days after its current `due_date` (using `date.fromisoformat` + `timedelta(days=7)`), save, redirect to `/`
- [ ] 1.2 Verify with a `test_app.py` case: create two todos with distinct due dates, select one by id, POST to `/push-week`, and assert only the selected todo's `due_date` shifted by 7 days while the other is unchanged

## 2. Frontend: selection checkboxes and submit button

- [ ] 2.1 In `templates/index.html`, add `<form id="push-week-form" action="{{ url_for('push_week') }}" method="post">` with a "Push to next week" submit button, placed above the todo list
- [ ] 2.2 Add a checkbox to each todo row's view-mode markup: `<input type="checkbox" name="ids" value="{{ todo.id }}" form="push-week-form">`, without nesting it inside the existing per-row delete `<form>`
- [ ] 2.3 Verify by running the dev server (`FLASK_DEBUG=1 python app.py`), checking two of several todos, clicking "Push to next week", and confirming only those two todos' due dates moved forward by a week after the redirect

## 3. Edge cases and regression checks

- [ ] 3.1 Verify submitting the bulk form with no checkboxes selected is a no-op (test in `test_app.py`: POST `/push-week` with no `ids`, assert `todos.json` unchanged, no error)
- [ ] 3.2 Verify a selected id that no longer exists is ignored without error, while a valid id in the same submission still gets rescheduled (test in `test_app.py`)
- [ ] 3.3 Run the full test suite (`python -m pytest`) and confirm all tests pass, including pre-existing add/edit/delete/overdue tests
