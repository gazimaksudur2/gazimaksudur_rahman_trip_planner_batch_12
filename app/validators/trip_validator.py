from datetime import datetime


def validate_trip_data(data):
    required_fields = [
        "destination",
        "start_date",
        "end_date",
        "budget",
        "max_travelers"
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")
        
    try:
        start_date = datetime.strptime(
            data["start_date"],
            "%Y-%m-%d"
        ).date()

        end_date = datetime.strptime(
            data["end_date"],
            "%Y-%m-%d"
        ).date()

    except ValueError:
        raise ValueError("Invalid date format. Follow YYYY-MM-DD")

    if end_date <= start_date:
        raise ValueError("End date must be after start date")

    if data["budget"] <= 0:
        raise ValueError("Budget must be greater than zero")

    if data["max_travelers"] <= 0:
        raise ValueError("Maximum travelers must be greater than zero")

    return start_date, end_date