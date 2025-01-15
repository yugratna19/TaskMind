# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionAddTask(Action):
    def name(self):
        return "action_add_task"

    def run(self, dispatcher, tracker, domain):
        title = tracker.get_slot("title")
        description = tracker.get_slot("description")
        due_date = tracker.get_slot("due_date")
        priority = tracker.get_slot("priority")

        if title:
            # Send data to Django backend
            response = requests.post("http://localhost:8000/api/tasks/", data={
                "title": title,
                "description": description,
                "due_date": due_date,
                "priority": priority
            })

            if response.status_code == 201:
                dispatcher.utter_message(text=f"Task '{title}' has been added!")
            else:
                dispatcher.utter_message(text="Failed to add the task. Please try again.")
        else:
            dispatcher.utter_message(text="I need a title to add a task.")

        return []

class ActionRecommendTask(Action):
    def name(self):
        return "action_recommend_task"

    def run(self, dispatcher, tracker, domain):
        # Fetch tasks from Django API
        response = requests.get("http://localhost:8000/api/tasks/recommend/")

        if response.status_code == 200:
            tasks = response.json()
            if tasks:
                recommendation = "\n".join([f"{task['title']} (Due: {task['due_date']}, Priority: {task['priority']})" for task in tasks])
                dispatcher.utter_message(text=f"Here are your recommended tasks:\n{recommendation}")
            else:
                dispatcher.utter_message(text="No tasks to recommend.")
        else:
            dispatcher.utter_message(text="Failed to fetch recommendations.")

        return []
