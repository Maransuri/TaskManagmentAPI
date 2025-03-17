# Task Management API

[![Build Status](https://github.com/Maransuri/TaskManagmentAPI/actions/workflows/main.yml/badge.svg)](https://github.com/Maransuri/TaskManagmentAPI/actions/workflows/main.yml)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

This document outlines the specifications and usage of the Task Management API, designed to streamline task management for users and provide administrative oversight. Developed using Python with the Django framework and Django Rest Framework (DRF), this API offers a robust and secure solution for creating, retrieving, updating, and deleting tasks. It incorporates features for authentication, filtering, pagination, and role-based access control, ensuring efficient and organized task management.

## Key Features

* **User-Centric Task Management:** Empower users to create, view, modify, and remove their own tasks, fostering individual productivity and organization.
* **Secure Authentication:** Leverages Django's built-in authentication system combined with DRF's `TokenAuthentication` to ensure that all API interactions are secure and authenticated.
* **Advanced Task Filtering:** Enables users to filter tasks based on completion status and date ranges for creation and updates, facilitating focused task management.
* **Efficient Pagination:** Implements pagination for task lists, improving performance and user experience by displaying tasks in manageable chunks.
* **Role-Based Access Control:** Utilizes custom permissions to restrict access to sensitive administrative functions, ensuring that only authorized admin users can view all tasks across the system.
* **Robust Error Handling:** Provides clear and informative error responses with appropriate HTTP status codes, enhancing the developer experience and simplifying debugging.
* **Version Control:** Managed using Git and hosted on GitHub, allowing for collaborative development and easy tracking of changes.

## Technologies

* **Backend Framework:** Python (>= 3.x) with Django
* **API Framework:** Django Rest Framework (DRF)
* **Authentication:** Django's built-in authentication, DRF's `TokenAuthentication`
* **Database:** SQLite (default for development), PostgreSQL, MySQL, etc. (configurable)
* **Containerization:** Docker (optional, for deployment and consistency)
* **Version Control:** Git

## Getting Started

Follow these steps to set up and run the Task Management API.

### Prerequisites

* Python (version >= 3.x)
* pip (Python package installer)
* Git (for cloning the repository)

### Installation

1.  **Clone the repository from GitHub:**
    ```bash
    git clone [https://github.com/Maransuri/TaskManagmentAPI.git](https://github.com/Maransuri/TaskManagmentAPI.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd TaskManagmentAPI
    ```
3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate     # On Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser for admin access:**
    ```bash
    python manage.py createsuperuser
    ```

### Running the API

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
2.  The API will be accessible at `http://localhost:8000/`.

### Testing the API

The API can be tested using tools like Postman or by using Docker.

#### Postman Collection

A Postman collection (`TaskManagementAPI.postman_collection.json`) is included in the repository. Import this into Postman to easily interact with the API endpoints. Ensure you update the environment variables with a valid authentication token after obtaining it via the `/api/token/` endpoint.

#### Docker Support

For a consistent and isolated environment, you can use Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t taskmanagementapi .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 taskmanagementapi
    ```
    The API will be available at `http://localhost:8000/`.

    **Note:** To create a superuser within the Docker container, use:
    ```bash
    docker exec -it <container_id> python manage.py createsuperuser
    ```
    Replace `<container_id>` with the ID of your running container (found using `docker ps`).

## API Endpoints

| Method | Endpoint                | Description                                                                                                                                                                                             | Authentication Required |
| :----- | :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------- |
| POST   | `/api/users/`           | Registers a new user.                                                                                                                                                                                 | No                      |
| POST   | `/api/token/`           | Retrieves an authentication token for a user.                                                                                                                                                           | No                      |
| POST   | `/api/tasks/`           | Creates a new task for the authenticated user.                                                                                                                                                            | Yes                     |
| GET    | `/api/tasks/`           | Lists all tasks for the authenticated user. Supports filtering by `completed` status and date ranges, and pagination.                                                                                       | Yes                     |
| GET    | `/api/tasks/{id}/`      | Retrieves the details of a specific task.                                                                                                                                                                | Yes                     |
| PUT/PATCH | `/api/tasks/{id}/`      | Updates a specific task. Only the creator of the task can perform this action.                                                                                                                            | Yes                     |
| DELETE | `/api/tasks/{id}/`      | Deletes a specific task. Only the creator of the task can perform this action.                                                                                                                            | Yes                     |
| GET    | `/api/admin/tasks/`     | Lists all tasks across all users. Requires admin authentication.                                                                                                                                         | Yes (Admin)             |

## Contributing

We welcome contributions to the Task Management API. Please adhere to the following guidelines:

1.  **Fork the repository:** Create your own fork of the repository on GitHub using the "Fork" button.
2.  **Clone your fork locally:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/TaskManagmentAPI.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/TaskManagmentAPI.git)
    cd TaskManagmentAPI
    ```
3.  **Create a new branch:** Make your changes in a dedicated branch, named according to the feature or bug fix.
    ```bash
    git checkout -b feature/new-feature
    ```
4.  **Implement your changes:** Write clean, well-documented code.
5.  **Commit your changes:**
    ```bash
    git add .
    git commit -m "Add new feature or fix bug"
    ```
6.  **Push your changes to your fork:**
    ```bash
    git push origin feature/new-feature
    ```
7.  **Submit a pull request:** Once your changes are complete and tested, submit a pull request from your fork to the main repository on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For any issues or questions, please refer to the project's issue tracker on GitHub.