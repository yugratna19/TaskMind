# TaskMind

TaskMind is a productivity-focused web application built with Django and AI/ML integration. It allows users to manage their daily schedules, set productivity goals, and track their progress with intelligent recommendations.## Features

- **Task Scheduling**: Add and manage daily tasks.
- **Productivity Goals**: Set and track productivity goals.
- **AI-Enhanced Productivity**: Use AI/ML models to provide intelligent recommendations and tips for improving productivity.
- **MongoDB Integration**: Store data such as tasks, schedules, and user profiles using MongoDB.
- **Customizable Routine**: Chat with the app to set and modify your daily routine.
Project Structure

This repository follows a well-organized structure for development and testing.

```plaintext
taskmind/                    # Root project folder
├── .gitignore               # Ignore unnecessary files (e.g., venv, db)
├── README.md                # Instructions for setting up the project
├── requirements.txt         # List of project dependencies
├── manage.py                # Django management script
├── taskmind/                # Django project settings and configurations
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/                     # Main app folder for business logic
│   ├── models.py            # Database models (e.g., Task, Schedule)
│   ├── views.py             # Views for app logic
│   ├── urls.py              # URL routing for this app
│   ├── templates/           # HTML templates for frontend
│   │   ├── base.html        # Base template
│   │   └── home.html        # Homepage template
│   ├── static/              # Static assets (CSS, JS, images)
│   │   ├── css/             # Stylesheets
│   │   ├── js/              # JavaScript files
│   │   └── images/          # Images
├── ai_models/               # AI and ML models and related files
│   ├── notebooks/           # Notebooks for model training (Google Colab)
│   │   └── chatbot_training.ipynb
│   ├── models/              # Folder for trained models (e.g., .h5, .pkl)
├── static/                  # Global static folder
│   └── ...                  # Any other shared static assets
├── templates/               # Global HTML templates
│   └── ...                  # Shared templates if needed across multiple apps
├── db/                      # MongoDB data files (ignored by Git)
└── tests/                   # Unit and integration tests
    ├── test_views.py
    ├── test_models.py
    └── test_ai.py
```

## Setup

Follow these steps to set up and run TaskMind locally.

### Prerequisites

- Python 3.8+ (ensure it's installed on your machine)

- MongoDB (use local or cloud-based MongoDB like MongoDB Atlas)

### Install Dependencies

- Clone this repository:

    ```bash
    git clone https://github.com/yourusername/TaskMind.git
    cd TaskMind
    
- Set up a virtual environment:

    ```bash
    python -m venv venv

- Activate the virtual environment:

    ```bash
    .\venv\Scripts\activate

- Install required dependencies:

    ```bash
    pip install -r requirements.txt



### MongoDB Setup

If you're using MongoDB locally, make sure MongoDB is running. If using MongoDB Atlas, configure your connection string in`settings.py`.

### Running the Application

To run the development server, follow these steps:

- Run the migrations:

   ```bash
   python manage.py migrate

- Start the server:

   ```bash
   python manage.py runserver


The app will be available at `http://127.0.0.1:8000/`.

## AI/ML Integration

In this project, AI/ML is integrated to help the user improve productivity:

- AI Model: The app will use a trained AI model to analyze user data (e.g., daily routines) and provide intelligent productivity tips.
- Google Colab Notebooks: AI training is handled via Google Colab notebooks, which are stored in the `ai_models/notebooks/` folder.

### Training Models

To train the AI model:

- Open the Colab notebook stored in `ai_models/notebooks/`.
- Follow the instructions to train the model.
- Save the trained model in the `ai_models/models/` directory.

### Tests

Unit and integration tests are stored in the `tests/` folder.

- `test_views.py`: Tests for app views.
- `test_models.py`: Tests for the database models.
- `test_ai.py`: Tests for AI logic.

To run tests:

```bash
python manage.py test
