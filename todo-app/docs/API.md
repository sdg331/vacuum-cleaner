# Todo API

## Base URL

- `http://localhost:5000/api`

## Health Check

- `GET /health`
- Response: `200 OK`

{ "status": "ok" }

## Get Todos

- `GET /todos`
- Query Parameters (optional)
- `completed=true|false`
- Response: `200 OK`

[
{
"id": 1,
"title": "예시 할 일",
"completed": false,
"created_at": "2025-12-05T12:00:00",
"updated_at": "2025-12-05T12:00:00"
}
]

## Create Todo

- `POST /todos`
- Request Body:

{ "title": "새 할 일" }

- Response: `201 Created`
{
"id": 1,
"title": "새 할 일",
"completed": false,
"created_at": "...",
"updated_at": "..."
}
## Update Todo

- `PUT /todos/{id}`
- Request Body (one or both):
{ "title": "수정된 제목", "completed": true }

text
- Response: `200 OK` (updated todo)

## Delete Todo

- `DELETE /todos/{id}`
- Response: `204 No Content`

## Delete All Todos (Debug)

- `DELETE /todos`
- Response: `200 OK`
{ "deleted": 3 }

text
undefined
