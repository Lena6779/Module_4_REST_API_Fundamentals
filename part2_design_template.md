# Module 4 Project — Part 2: Study Tracker API Design

**Your Name:**
**Date:**

---

## The App: Study Tracker

Design a REST API for a "Study Tracker" app. Students can:
- Log study sessions (course, duration, notes)
- Set study goals (target hours per course per week)
- View their progress and summaries

---

## Section 1 — Resources

List the resources your API will manage. Suggested: Students, Courses, Study Sessions, Goals.

| Resource | Key Attributes |
|----------|---------------|
| | |
| | |
| | |
| | |

---

## Section 2 — Relationships

Describe how your resources relate to each other:

- Student ↔ Course: _(describe)_
- Student ↔ Study Session: _(describe)_
- Course ↔ Study Session: _(describe)_
- Student ↔ Goal: _(describe)_

---

## Section 3 — Endpoints

Design at least:
- Full CRUD for study_sessions (5 endpoints)
- 3+ endpoints for related resources
- 1+ filtering endpoint

| Method | URI | Description | Auth Required? |
|--------|-----|-------------|----------------|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

---

## Section 4 — Request/Response Schemas

### POST /study_sessions — Create a new session

**Request body:**
```json
{

}
```

**Success response (201):**
```json
{

}
```

### GET /students/{id}/progress

**Response (200):**
```json
{

}
```

---

## Section 5 — Authentication

| Endpoint | Auth Required | Notes |
|----------|--------------|-------|
| GET /courses | | |
| POST /study_sessions | | |
| GET /students/{id}/progress | | |
| DELETE /study_sessions/{id} | | |

**Auth method and rationale:**
> _Write here._

---

## Section 6 — Error Responses for POST /study_sessions

| Status Code | When it occurs |
|-------------|---------------|
| 201 | |
| 400 | |
| 401 | |
| 404 | |
| 422 | |
