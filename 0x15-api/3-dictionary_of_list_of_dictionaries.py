#!/usr/bin/python3
"""Export all user data in the JSON format

Format: { "USER_ID": [
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    ... ],
    "USER_ID": [ ... ] }

File name must be: todo_all_employees.json
"""

if __name__ == "__main__":
    import json
    import requests

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for user in users:
        for todo in todos:
            if todo['userId'] == user['id']:
                with open('todo_all_employees.json', 'w') as f:
                    json.dump({user['id']: [{
                        'username': user.get('username'),
                        'task': todo.get('title'),
                        'completed': todo.get('completed')
                        } for todo in todos]}, f)
