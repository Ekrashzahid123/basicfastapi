# Day 40: FastAPI Basics

This project demonstrates the fundamentals of building a REST API using FastAPI. It includes a small in-memory student management system with validation and structured routes.

## What is a REST API?

A REST API (Representational State Transfer API) is a way for applications to communicate over HTTP using standard methods such as GET, POST, PUT, and DELETE. REST APIs allow different systems to exchange data in a structured format, usually JSON.

## Difference between GET and POST

- GET: Used to fetch data from the server. It is typically safe and does not modify the server state.
- POST: Used to send new data to the server, usually to create a new record.

Example:

- GET /students → retrieve all students
- POST /students → create a new student

## What is Pydantic used for?

Pydantic is used to validate request data and ensure it matches the expected schema before the application processes it. It helps enforce rules such as required fields, data types, minimum and maximum values, and string lengths.

For example, the student model requires:

- name: string with a valid length
- age: integer between 1 and 120
- course: string with a valid length

If invalid input is sent, FastAPI automatically returns a validation error.

## Project Structure

```text
Day-40/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── students.py
│   └── schemas/
│       └── student.py
├── requirements.txt
└── README.md
```

## API Structure

- `app/main.py` contains the main FastAPI application instance.
- `app/routes/students.py` defines the CRUD routes for students.
- `app/schemas/student.py` defines the Pydantic models for requests and responses.

## Endpoints

### GET /
Returns a welcome message.

### GET /health
Returns the status of the API.

### GET /students
Returns a list of all students.

### POST /students
Creates a new student.

### GET /students/{id}
Gets a single student by ID.

### PUT /students/{id}
Updates a student by ID.

### DELETE /students/{id}
Deletes a student by ID.

## Example Requests and Responses

### Create a student

Request:

```http
POST /students
Content-Type: application/json

{
  "name": "Ali",
  "age": 20,
  "course": "AI Engineering"
}
```

Response:

```json
{
  "id": 1,
  "name": "Ali",
  "age": 20,
  "course": "AI Engineering"
}
```

### Get all students

Request:

```http
GET /students
```

Response:

```json
[
  {
    "id": 1,
    "name": "Ali",
    "age": 20,
    "course": "AI Engineering"
  }
]
```

### Health check

Request:

```http
GET /health
```

Response:

```json
{
  "status": "ok",
  "message": "API is healthy and running successfully."
}
```

## How to Run the Project

1. Open a terminal in the `Day-40` folder.
2. Create and activate a virtual environment if needed.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Start the API:

```bash
uvicorn app.main:app --reload
```

5. Open Swagger UI in your browser:

```text
http://127.0.0.1:8000/docs
```

6. Open the ReDoc docs:

```text
http://127.0.0.1:8000/redoc
```

## Swagger and Testing

FastAPI automatically generates interactive API documentation using OpenAPI and Swagger UI. This makes it easy to test the application without external tools.

You can also test API endpoints using Postman or Thunder Client.

## Notes

This project uses an in-memory dictionary instead of a database so it is easy to understand the basics of FastAPI and API structure. In later projects, the same pattern can be connected to a database and deployed in a real backend service.
