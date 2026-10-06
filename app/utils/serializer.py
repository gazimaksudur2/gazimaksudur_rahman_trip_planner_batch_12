def trip_to_dict(trip):

    return {
        "id": trip.id,
        "destination": trip.destination,
        "start_date": str(trip.start_date),
        "end_date": str(trip.end_date),
        "budget": trip.budget,
        "max_travelers": trip.max_travelers,
        "status": trip.status
    }