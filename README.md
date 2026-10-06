# Smart Group Trip Planner API

A REST API for managing group trips using **Python, Flask, and SQLite**.

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite

## Setup and Run

### Automatic Run

```bash
./run.sh
```

The script creates the virtual environment, installs dependencies, initializes the database, and starts the API.

Application runs at:

```
http://127.0.0.1:5000
```

### Manual Run

```bash
pip install -r requirements.txt
python3 run.py
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response:

```json
{
    "status": "ok"
}
```

---

## Trip Management

### Create Trip

```
POST /api/v1/trips
```

Example:

```json
{
    "destination": "Coxs Bazar",
    "start_date": "2026-12-01",
    "end_date": "2026-12-05",
    "budget": 50000,
    "max_travelers": 5
}
```

### Get All Trips

```
GET /api/v1/trips
```

### Get Single Trip

```
GET /api/v1/trips/<trip_id>
```

### Update Trip

```
PUT /api/v1/trips/<trip_id>
```

### Delete Trip

```
DELETE /api/v1/trips/<trip_id>
```

---

## Current Validation Rules

- End date must be after start date
- Budget must be greater than zero
- Maximum travelers must be greater than zero
- Invalid trip IDs return 404

---

## Database

SQLite database is created automatically during application startup.

Database files are ignored by Git.

---

## Current Progress

Implemented:

- Flask setup
- SQLite persistence
- Trip model
- Trip CRUD API
- Trip validation
