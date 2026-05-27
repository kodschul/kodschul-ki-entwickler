def func_format_due_date(due_date_str):
    """
    Formats an ISO date (YYYY-MM-DD) for display.

    - Returns "No date" if due_date_str is empty/None
    - Returns "Overdue" if the date is in the past
    - Otherwise: returns "Due on DD.MM.YYYY"

    Args:
        due_date_str: ISO date string or None
    Returns:
        Formatted string for the UI
    """
    if not due_date_str:
        return "No date"

    from datetime import datetime, date

    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    today = date.today()

    if due_date < today:
        return "Overdue"
    else:
        return f"Due on {due_date.strftime('%d.%m.%Y')}"
