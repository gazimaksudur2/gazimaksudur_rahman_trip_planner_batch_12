# Smart Group Trip Planner API

A REST API for managing group trips using Python, Flask, and SQLite.

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

### Manual Run

```bash
pip install -r requirements.txt
python3 run.py
```

Application:

```
http://127.0.0.1:5000
```

---

# API Endpoints

## Health Check

```
GET /health
```

---

# Trip Management

## Create Trip

```
POST /api/v1/trips
```

Example:

```json
{
    "destination": "Cox Bazar",
    "start_date": "2026-12-01",
    "end_date": "2026-12-05",
    "budget": 50000,
    "max_travelers": 5
}
```

## Get Trips

```
GET /api/v1/trips
```

## Get Single Trip

```
GET /api/v1/trips/<trip_id>
```

## Update Trip

```
PUT /api/v1/trips/<trip_id>
```

## Delete Trip

```
DELETE /api/v1/trips/<trip_id>
```

---

# Traveler Management

## Add Traveler

```
POST /api/v1/trips/<trip_id>/travelers
```

Example:

```json
{
    "name": "Rahim",
    "email": "rahim@gmail.com"
}
```

Features:
- Automatic user creation
- Duplicate prevention
- Overlapping trip prevention

## Remove Traveler

```
DELETE /api/v1/trips/<trip_id>/travelers/<traveler_id>
```

---

# Expense Management

## Add Expense

```
POST /api/v1/trips/<trip_id>/expenses
```

Example:

```json
{
    "title": "Hotel",
    "amount": 10000
}
```

Rules:
- Positive amount required
- Cannot exceed trip budget
- Allowed for PLANNED and ONGOING trips

---

# Trip Summary

```
GET /api/v1/trips/<trip_id>/summary
```

Returns:
- Traveler count
- Available seats
- Total expenses
- Remaining budget
- Trip status

---

# Trip Status

## Update Status

```
PATCH /api/v1/trips/<trip_id>/status
```

Allowed transitions:

```
PLANNED  → ONGOING
PLANNED  → CANCELLED
ONGOING  → COMPLETED
ONGOING  → CANCELLED
```

---

# Validation Rules

- End date must be after start date
- Budget must be greater than zero
- Maximum travelers must be greater than zero
- Duplicate travelers are rejected
- Expenses cannot exceed budget
- Invalid status transitions are rejected

---

# Database Design

```
User
 |
Traveler
 |
Trip
 |
Expense
```

- User stores traveler information
- Traveler represents trip membership
- Expense belongs to a trip

SQLite database is created automatically.

---

# Testing

Run tests:

```bash
python -m pytest -v
```

Implemented test coverage:

- Trip API tests
- Traveler API tests
- Expense API tests
- Summary API tests

---

# Implementation Status

Implemented:

- Flask application structure
- SQLite persistence
- Trip CRUD operations
- Traveler management
- Expense management
- Trip summary
- Status lifecycle
- Validation rules
- Automated testing
