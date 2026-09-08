def fine_tier(days_overdue: int) -> str:
    """
    Map the number of days a book is overdue to a fine tier.

    Args:
        days_overdue: Number of days overdue (non-negative integer)

    Returns:
        Tier label: 'None', 'Low', 'Medium', 'High', or 'Severe'

    Raises:
        ValueError: If days_overdue is negative
    """
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")

    if days_overdue == 0:
        return 'None'
    elif 1 <= days_overdue <= 7:
        return 'Low'
    elif 8 <= days_overdue <= 14:
        return 'Medium'
    elif 15 <= days_overdue <= 30:
        return 'High'
    else:  # days_overdue >= 31
        return 'Severe'