def validate_expense_data(data):
    if not data:
        raise ValueError("Expense data is required")

    required_fields = ["title", "amount"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"{field} is required")

    if not isinstance(data["title"], str):
        raise ValueError("Title must be a string")

    if len(data["title"].strip()) < 2:
        raise ValueError("Title must be at least 2 characters long")

    try:
        amount = float(data["amount"])
        if amount <= 0:
            raise ValueError("Amount must be a positive number")
    except (ValueError, TypeError):
        raise ValueError("Amount must be a valid number")

    return amount
