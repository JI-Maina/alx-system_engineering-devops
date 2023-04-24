#!/usr/bin/python3
"""Given employee ID, this script exports data in JSON format.

Format must be: { "USER_ID": [
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    ... ]}

File name must be: USER_ID.json
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    pay = {'userId': argv[1]}
    pay1 = {'id': argv[1]}

    r = requests.get('https://jsonplaceholder.typicode.com/todos', params=pay)
    u = requests.get('https://jsonplaceholder.typicode.com/users', params=pay1)

    todos = r.json()
    user = u.json()
    username = user[0]['username']
    id = argv[1]

    with open(f'{id}.json', 'w') as f:
        json.dump({id: [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username,
            } for todo in todos]}, f)
