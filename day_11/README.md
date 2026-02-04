# Day 11: Task Manager REST API

A RESTful API for managing tasks built with Flask.

## Features
- Create, read, update, delete tasks
- Filter by status and priority
- Task statistics
- Persistent storage (JSON)

## Installation
[steps]

## API Endpoints

### GET /api/tasks
Returns all tasks

### POST /api/tasks
Create a new task
Body: {"title": "...", "priority": "high"}

### GET /api/tasks/<id>
Get specific task

### PUT /api/tasks/<id>
Update task
Body: {"status": "completed"}

### DELETE /api/tasks/<id>
Delete task

## Testing
Use Postman or cURL to test endpoints

## What I Learned
- Building REST APIs with Flask
- HTTP methods and status codes
- JSON file storage
- Request/response handling