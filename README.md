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

### Create Trip

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

# Traveler Management

Users are automatically created when joining a trip.

### Add Traveler

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
- Duplicate trip membership prevention
- Traveler-trip relationship tracking

### Remove Traveler From Trip

```
DELETE /api/v1/trips/<trip_id>/travelers/<traveler_id>
```

(Removes trip membership only, keeps user data.)

---

# Expense Management

### Add Expense

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
- Expense amount must be positive
- Total expenses cannot exceed trip budget

---

# Trip Summary

### Get Trip Summary

```
GET /api/v1/trips/<trip_id>/summary
```

Returns:

- Traveler count
- Available seats
- Total expenses
- Remaining budget
- Current trip status

---

# Trip Status Lifecycle

### Update Status

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
- Duplicate travelers cannot join the same trip
- Expenses cannot exceed trip budget
- Invalid status transitions are rejected

---

# Database Design

Main entities:

```
User
 |
Traveler
 |
Trip
 |
Expense
```

- Users represent people.
- Travelers represent trip membership.
- Expenses belong to trips.

SQLite database is created automatically during application startup.

---

# Current Implementation

Implemented:

- Flask application structure
- SQLite persistence
- Trip CRUD operations
- User and traveler management
- Expense tracking
- Trip summary calculation
- Trip status lifecycle management
- Validation and business rules