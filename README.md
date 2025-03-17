# Task Management API

[![Build Status](https://github.com/Maransuri/TaskManagmentAPI/actions/workflows/main.yml/badge.svg)](https://github.com/Maransuri/TaskManagmentAPI/actions/workflows/main.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This API provides a set of endpoints for managing tasks. It allows authenticated users to create, read, update, and delete their own tasks. The API also includes features for filtering, pagination, and restricted access for admin users to view all tasks.

## Features

* **Task Management (Authenticated Users):**
    * Create new tasks with titles, descriptions, and completion status.
    * Retrieve details of a specific task.
    * List all tasks created by the authenticated user.
    * Update task details (title, description, completed status).
    * Delete tasks.
* **User Authentication:**
    * Utilizes Django's built-in authentication system.
    * Implements token-based authentication using Django Rest Framework's `TokenAuthentication`.
* **Task Filtering:**
    * Filter tasks by `completed` status using the `completed` query parameter (e.g., `/api/tasks/?completed=true`).
    * Filter tasks by date ranges for `created_at` and `updated_at` using query parameters like `created_after`, `created_before`, `updated_after`, `updated_before` (e.g., `/api/tasks/?created_after=2024-01-01`).
* **Pagination:**
    * Implements pagination for the list of tasks, displaying 10 tasks per page. Use the `page` query parameter to navigate between pages.
* **Admin Access (Custom Permissions):**
    * A custom permission class ensures that only admin users can view the full list of all users' tasks.
* **Error Handling:**
    * Handles errors gracefully with appropriate HTTP status codes (e.g., 400 for bad requests, 404 for not found).

## Technologies Used

* **Backend Framework:** Python with Django
* **API Framework:** Django Rest Framework (DRF)
* **Authentication:** Django's built-in authentication, DRF's `TokenAuthentication`
* **Database:** SQLite (default for development)

## Getting Started

### Prerequisites

* Python (version >= 3.x)
* pip (Python package installer)

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Maransuri/TaskManagmentAPI.git](https://www.google.com/search?q=https://github.com/Maransuri/TaskManagmentAPI.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd TaskManagmentAPI
    ```
3.  Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Apply migrations:
    ```bash
    python manage.py migrate
    ```
6.  Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

### Running the API

1.  Start the development server:
    ```bash
    python manage.py runserver
    ```
2.  The API will be accessible at `http://localhost:8000/`.

### Testing the API

You can use a tool like Postman or `curl` to test the API endpoints.

**Postman Collection:**

A Postman collection is included in the repository (`TaskManagementAPI.postman_collection.json`). Import this collection into Postman to easily test the API endpoints.

**Curl Commands:**

Here are some example `curl` commands:

* **Register a new user:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}' http://localhost:8000/api/users/
    ```
* **Get an authentication token:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}' http://localhost:8000/api/token/
    ```
* **Create a new task (replace `YOUR_TOKEN` with the actual token):**
    ```bash
    curl -X POST -H "Content-Type: application/json" -H "Authorization: Token YOUR_TOKEN" -d '{"title": "My New Task", "description": "This is a test task"}' http://localhost:8000/api/tasks/
    ```
* **List all tasks (replace `YOUR_TOKEN`):**
    ```bash
    curl -X GET -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/tasks/
    ```
* **List tasks with filtering:**
    ```bash
    curl -X GET -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/tasks/?completed=false
    ```
* **List tasks with pagination (page 2):**
    ```bash
    curl -X GET -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/tasks/?page=2
    ```
* **Get a specific task (replace `YOUR_TOKEN` and `TASK_ID`):**
    ```bash
    curl -X GET -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/tasks/1/
    ```
* **Update a task (replace `YOUR_TOKEN` and `TASK_ID`):**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -H "Authorization: Token YOUR_TOKEN" -d '{"title": "Updated Task", "completed": true}' http://localhost:8000/api/tasks/1/
    ```
* **Delete a task (replace `YOUR_TOKEN` and `TASK_ID`):**
    ```bash
    curl -X DELETE -H "Authorization: Token YOUR_TOKEN" http://localhost:8000/api/tasks/1/
    ```

## API Endpoints

* `POST /api/users/`: Register a new user.
* `POST /api/token/`: Get an authentication token.
* `POST /api/tasks/`: Create a new task (requires authentication).
* `GET /api/tasks/`: List all tasks for the authenticated user (requires authentication). Supports filtering (`completed`, date ranges) and pagination.
* `GET /api/tasks/{id}/`: Get details of a specific task (requires authentication).
* `PUT/PATCH /api/tasks/{id}/`: Update a task (requires authentication, only the creator can update).
* `DELETE /api/tasks/{id}/`: Delete a task (requires authentication, only the creator can delete).
* `GET /api/admin/tasks/`: List all tasks across all users (requires admin authentication).

## Contributing

If you'd like to contribute to this API, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.

## License

MIT License

---

This is a clearer and more comprehensive README file for your Task Management API. It includes instructions for setup, examples of API usage, and information about the technologies used. Remember to commit this updated `README.md` file to your repository.