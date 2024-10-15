# The Eyedde Web Application

The Eyedde Web Application is a digital content publishing platform developed using Python and the Django framework. It allows users to create, post, and publish various types of digital content as posts.

## Features

- User authentication and authorization
- Create and publish digital content posts
- Browse and view posts from other users
- User profiles and dashboards
- Search functionality for posts
- Responsive design for mobile and desktop

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Hashara13/The-Eyedde-Web-Application.git
   ```

2. Navigate to the project directory:
   ```
   cd The-Eyedde-Web-Application
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (admin) account:
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Open your web browser and navigate to `http://localhost:8000` to access the application.

3. Log in with your superuser account or create a new user account to start posting content.


## Contact

Hashara - [GitHub Profile](https://github.com/Hashara13)

Project Link: [https://github.com/Hashara13/The-Eyedde-Web-Application](https://github.com/Hashara13/The-Eyedde-Web-Application)