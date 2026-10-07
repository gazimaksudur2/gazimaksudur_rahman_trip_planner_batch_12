from re import match


def validate_traveler_data(data):
    if not data:
        raise ValueError("Request body cannot be empty")

    required_fields = ["name", "email"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing Field: {field}")

    name = data["name"]
    email = data["email"]

    if not isinstance(name, str):
        raise ValueError("Name must be a string value")
    if len(name.strip()) < 2:
        raise ValueError("Name must contain at least 2 characters")
    if not isinstance(email, str):
        raise ValueError("Email must be a string value")

    email_pattern = (r"^[A-Za-z0-9._%+-]+@" r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

    if not match(email_pattern, email):
        raise ValueError("Invalid email format")

    return True
