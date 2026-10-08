def test_add_traveler_to_trip(client):

    trip_response = client.post(
        "/api/v1/trips",
        json={
            "destination": "Cox Bazar",
            "start_date": "2026-01-01",
            "end_date": "2026-01-05",
            "budget": 5000,
            "max_travelers": 5
        }
    )

    assert trip_response.status_code == 201

    trip_id = trip_response.json["id"]

    response = client.post(
        f"/api/v1/trips/{trip_id}/travelers",
        json={
            "name": "John Doe",
            "email": "john_unique_1@gmail.com"
        }
    )

    assert response.status_code == 201


def test_duplicate_traveler_rejected(client):

    trip_response = client.post(
        "/api/v1/trips",
        json={
            "destination": "Cox Bazar",
            "start_date": "2026-01-01",
            "end_date": "2026-01-05",
            "budget": 5000,
            "max_travelers": 5
        }
    )

    assert trip_response.status_code == 201

    trip_id = trip_response.json["id"]

    payload = {
        "name": "John Doe",
        "email": "john@gmail.com"
    }

    first = client.post(
        f"/api/v1/trips/{trip_id}/travelers",
        json=payload
    )

    assert first.status_code == 201

    second = client.post(
        f"/api/v1/trips/{trip_id}/travelers",
        json=payload
    )

    assert second.status_code == 400


def test_missing_email_rejected(client):

    response = client.post(
        "/api/v1/trips/1/travelers",
        json={
            "name": "John Doe"
        }
    )

    assert response.status_code == 400


def test_invalid_email_rejected(client):

    response = client.post(
        "/api/v1/trips/1/travelers",
        json={
            "name": "John Doe",
            "email": "invalid-email"
        }
    )

    assert response.status_code == 400