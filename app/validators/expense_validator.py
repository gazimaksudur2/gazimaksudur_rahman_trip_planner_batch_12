from app.exceptions.business_exception import BusinessException


def validate_expense_data(data):
    if not data:
        raise BusinessException("Expense data is required")

    required_fields = ["title", "amount"]
    for field in required_fields:
        if field not in data:
            raise BusinessException(f"{field} is required")

    if not isinstance(data["title"], str):
        raise BusinessException("Title must be a string")

    if len(data["title"].strip()) < 2:
        raise BusinessException("Title must be at least 2 characters long")

    try:
        amount = float(data["amount"])
        if amount <= 0:
            raise BusinessException("Amount must be a positive number")
    except (ValueError, TypeError):
        raise BusinessException("Amount must be a valid number")

    return amount
