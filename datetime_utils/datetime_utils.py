from datetime import datetime, timedelta

def add_days(date: datetime, days: int) -> datetime:
    """Add a specified number of days to a date."""
    return date + timedelta(days=days)

def days_between(date1: datetime, date2: datetime) -> int:
    """Return the number of days between two dates."""
    return (date2 - date1).days
