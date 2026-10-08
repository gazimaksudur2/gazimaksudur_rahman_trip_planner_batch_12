def create_test_trip(client):

    response = client.post(
        "/api/v1/trips",
        json={
            "destination": "Cox Bazar",
            "start_date": "2026-01-01",
            "end_date": "2026-01-05",
            "budget": 5000,
            "max_travelers": 5
        }
    )

    assert response.status_code == 201

    return response.json["id"]


def test_trip_summary(client):

    trip_id = create_test_trip(client)

    response = client.get(
        f"/api/v1/trips/{trip_id}/summary"
    )

    assert response.status_code == 200

    data = response.json

    assert "number_of_travelers" in data
    assert "total_expenses" in data
    assert "remaining_budget" in data
    assert "available_seats" in data