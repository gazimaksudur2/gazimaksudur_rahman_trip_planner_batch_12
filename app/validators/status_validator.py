from app.exceptions.business_exception import BusinessException


ALLOWED_TRANSITIONS = {
    "PLANNED": ["ONGOING", "CANCELLED"],
    "ONGOING": ["COMPLETED", "CANCELLED"],
    "COMPLETED": [],
    "CANCELLED": []
}


def validate_status_transition(current_status, new_status):
    if new_status not in ALLOWED_TRANSITIONS.get(current_status, []):
        raise BusinessException(
            "Invalid status transition: " f"{current_status} -> {new_status}"
        )

    return True
