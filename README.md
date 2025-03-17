📌 Task Management API
A Django-based RESTful API that allows users to manage tasks efficiently.
Supports authentication, CRUD operations, filtering, pagination, Docker deployment, and GitHub integration.

🔹 Features
✅ User Authentication – JWT-based authentication system
✅ CRUD Operations – Create, Read, Update, and Delete tasks
✅ Filtering & Pagination – Filter tasks by status, date, and paginate results
✅ Docker Support – Easily run with Docker
✅ GitHub Deployment – Push code to GitHub

📌 1️⃣ Prerequisites
Ensure you have:

Python 3.11+ installed (Download Here)
pip & virtualenv installed (pip install virtualenv)
PostgreSQL (optional) if using a database other than SQLite
Git installed (Download Here)
Docker (if running with Docker)
GitHub Account (Sign Up Here)
📌 2️⃣ Git Setup
Run the following to configure Git:

bash

git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
📌 3️⃣ Clone the Project
Run:

bash

git clone https://github.com/Maransuri/TaskManagmentAPI.git
cd TaskManagmentAPI
📌 4️⃣ Create a Virtual Environment
bash

python -m venv venv
Activate the virtual environment:

Windows:
bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:
bash

source venv/bin/activate
📌 5️⃣ Install Dependencies
bash

pip install -r requirements.txt
📌 6️⃣ Configure the Database
By default, the project uses SQLite. If using PostgreSQL, update settings.py:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
📌 7️⃣ Run Migrations
bash

python manage.py migrate
📌 8️⃣ Create a Superuser (Admin)
To create an admin account, run:

bash

python manage.py createsuperuser
Follow the prompts to set a username, email, and password.

📌 9️⃣ Start the Django Server
bash

python manage.py runserver
Now, visit http://127.0.0.1:8000/admin/ to access the Django Admin panel.

📌 🔟 API Endpoints
Method	Endpoint	Description
POST	/api/token/	Generate JWT access and refresh tokens
POST	/api/token/refresh/	Refresh access token
POST	/api/tasks/	Create a new task
GET	/api/tasks/	List all tasks
GET	/api/tasks/{id}/	Get details of a task
PUT	/api/tasks/{id}/	Update a task
DELETE	/api/tasks/{id}/	Delete a task
Use Postman or curl to interact with these endpoints.

📌 1️⃣1️⃣ Running the Project with Docker (Optional)
To run the project using Docker, follow these steps:

1️⃣ Build the Docker Image

bash

docker build -t taskmanager-api .
2️⃣ Run the Container

bash

docker run -p 8000:8000 taskmanager-api
Now, the app should be running at http://localhost:8000 🚀

📌 1️⃣2️⃣ Testing the API
Run tests using:

bash

python manage.py test
📌 1️⃣3️⃣ Pushing the Project to GitHub
🔹 Step 1: Initialize Git
If you haven’t initialized Git in your project folder, run:

bash

git init
🔹 Step 2: Create a .gitignore File
Run:

bash

echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "db.sqlite3" >> .gitignore
🔹 Step 3: Add & Commit Your Files
bash

git add .
git commit -m "Initial commit - Task Management API"
🔹 Step 4: Create a GitHub Repository
Go to GitHub → Click on New Repository.
Name it TaskManagmentAPI.
Do NOT initialize with a README (since we already have one).
Copy the provided remote URL.
🔹 Step 5: Add Remote Repository
bash

git remote add origin https://github.com/Maransuri/TaskManagmentAPI.git
git branch -M main
🔹 Step 6: Push to GitHub
bash

git push -u origin main
📌 1️⃣4️⃣ Verifying Deployment
Open GitHub.
Ensure your project files appear.
📌 1️⃣5️⃣ Troubleshooting
1. "Command Not Found: python"
Ensure Python is installed.
Try using python3 instead of python.
2. Database Connection Error
Ensure PostgreSQL is running and credentials are correct.
3. Docker Issues
Run docker ps to check if the container is running.
Restart Docker if necessary.
📌 🌟 Contributing
Fork the repository
Create a new branch (git checkout -b feature-name)
Commit your changes (git commit -m "Added new feature")
Push to GitHub (git push origin feature-name)
Open a Pull Request
📌 📜 License
This project is open-source under the MIT License.