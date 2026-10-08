def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_get_all_trips(client):
    response = client.get("/api/v1/trips")

    assert response.status_code == 200
    assert response.is_json


def test_create_trip(client):
    payload = {
        "destination": "Cox Bazr Trip",
        "start_date": "2027-10-26",
        "end_date": "2028-12-15",
        "budget": 400000,
        "max_travelers": 20
    }

    response = client.post(
            "/api/v1/trips",
            json=payload
        )
    assert response.status_code in [200, 201]


def test_create_trip_invalid_budget(client):
    payload = {
            "destination": "Cox Bazr Trip",
            "start_date": "2027-10-26",
            "end_date": "2028-12-15",
            "budget": -400000,
            "max_travelers": 20
        }

    response = client.post(
            "/api/v1/trips",
            json=payload
        )
    assert response.status_code == 400