def func_get_overdue_todos(todos_list):
    """
    Gibt alle Todos zurück, deren due_date vor heute liegt.

    Args:
        todos_list: Liste von Todo-Dicts mit optionalem 'due_date' (ISO-Format)
    Returns:
        Liste von überfälligen Todos
    """
    today = date.today()
    overdue_todos = []
    for todo in todos_list:
        due_date_str = todo.get("due_date")
        if due_date_str:
            try:
                due_date = date.fromisoformat(due_date_str)
                if due_date < today:
                    overdue_todos.append(todo)
            except ValueError:
                continue
    return overdue_todos
