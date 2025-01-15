# TaskMind

TaskMind is a Django-based task management web application designed to help users efficiently manage their tasks with features like task creation, updating, deletion, sorting, searching, and prioritization. The project is structured with Django best practices, ensuring scalability and maintainability.

## Features

- **Task Management**: Add, edit, delete, and mark tasks as completed.
- **Search & Sort**: Search tasks and sort them by due date, priority, or status.
- **Pagination**: View tasks with pagination for better navigation.
- **User Interface**: Responsive and intuitive UI with Bootstrap integration.
- **Future Integration**: A chatbot powered by Rasa will soon be integrated to handle task operations via natural language commands.

## Project Structure

This repository follows a well-organized structure for development and testing.

```plaintext
TaskMind/
├── manage.py
├── taskmind/                # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                   # Main app
│   ├── migrations/
│   ├── models.py           # Task model
│   ├── views.py            # Views for task operations
│   ├── forms.py            # Task form
│   ├── urls.py             # App-level URLs
│   ├── templates/
│   │   ├── base.html       # Base template
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       └── task_detail.html
│   ├── static/
│   │   └── css/
│   │       └── style.css  # Custom styles
├── tests/                   # Placeholder for tests
├── rasa_bot/                # Rasa chatbot setup (in progress)
│   ├── data/
│   ├── domain.yml
│   ├── actions.py
│   └── config.yml
└── README.md
```

## Installation

Follow these steps to set up and run TaskMind locally.

- Clone this repository:

    ```bash
    git clone https://github.com/yugratna19/TaskMind.git
    cd TaskMind
    
- Set up a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate     # For Windows

- Activate the virtual environment:

    ```bash
    .\venv\Scripts\activate

- Install required dependencies:

    ```bash
    pip install -r requirements.txt

- Apply Migrations:

    ```bash
    python manage.py migrate

- Run the Server:

    ```bash
    python manage.py runserver

- Access the App: Open your browser and visit http://127.0.0.1:8000/


### Chatbot Integration (In Progress)

The project will soon include a Rasa-powered chatbot for task management, offering features such as:

- **Adding Tasks**: Use natural language to create tasks.

- **Updating Tasks**: Modify task details via chat.

- **Task Recommendations**: Get smart suggestions based on due dates and priority.
