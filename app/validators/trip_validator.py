from datetime import datetime

from app.exceptions.business_exception import BusinessException


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
            raise BusinessException(f"Missing field: {field}")
        
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
        raise BusinessException("Invalid date format. Follow YYYY-MM-DD")

    if end_date <= start_date:
        raise BusinessException("End date must be after start date")

    if data["budget"] <= 0:
        raise BusinessException("Budget must be greater than zero")

    if data["max_travelers"] <= 0:
        raise BusinessException("Maximum travelers must be greater than zero")

    return start_date, end_date
