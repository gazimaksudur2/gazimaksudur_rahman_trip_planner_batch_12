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


def test_add_expense_success(client):

    trip_id = create_test_trip(client)

    response = client.post(
        f"/api/v1/trips/{trip_id}/expenses",
        json={
            "title": "Hotel",
            "amount": 1000
        }
    )

    assert response.status_code == 201


def test_negative_expense_rejected(client):

    trip_id = create_test_trip(client)

    response = client.post(
        f"/api/v1/trips/{trip_id}/expenses",
        json={
            "title": "Hotel",
            "amount": -100
        }
    )

    assert response.status_code == 400


def test_expense_cannot_exceed_budget(client):

    trip_id = create_test_trip(client)

    response = client.post(
        f"/api/v1/trips/{trip_id}/expenses",
        json={
            "title": "Luxury Hotel",
            "amount": 6000
        }
    )

    assert response.status_code == 400