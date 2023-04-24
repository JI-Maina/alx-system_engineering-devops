#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list progress"""

import requests
from sys import argv

payload = {'userId': argv[1]}
payload1 = {'id': argv[1]}

r = requests.get('https://jsonplaceholder.typicode.com/todos', params=payload)
u = requests.get('https://jsonplaceholder.typicode.com/users', params=payload1)

user = u.json()
todos = r.json()

complete = 0
for todo in todos:
    if todo["completed"] == True:
        complete = complete + 1

print("Employee {} is done with tasks({}/{}):"
        .format(user[0]['name'], complete, len(todos)))

for todo in todos:
    if todo["completed"] == True:
        print('     ' + todo['title'])
