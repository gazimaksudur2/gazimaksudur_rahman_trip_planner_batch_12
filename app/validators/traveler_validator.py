from re import match

from app.exceptions.business_exception import BusinessException


def validate_traveler_data(data):
    if not data:
        raise BusinessException("Request body cannot be empty")

    required_fields = ["name", "email"]

    for field in required_fields:
        if field not in data:
            raise BusinessException(f"Missing Field: {field}")

    name = data["name"]
    email = data["email"]

    if not isinstance(name, str):
        raise BusinessException("Name must be a string value")
    if len(name.strip()) < 2:
        raise BusinessException("Name must contain at least 2 characters")
    if not isinstance(email, str):
        raise BusinessException("Email must be a string value")

    email_pattern = (r"^[A-Za-z0-9._%+-]+@" r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    if not match(email_pattern, email):
        raise BusinessException("Invalid email format")

    return True
