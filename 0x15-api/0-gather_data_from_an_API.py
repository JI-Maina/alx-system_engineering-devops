#!/usr/bin/python3
"""
This module provides a script that given an employee ID, returns information
about his/her TODO list progress.
"""

from sys import argv
import requests

if __name__ == "__main__":
    pay = {'userId': argv[1]}
    pay1 = {'id': argv[1]}

    r = requests.get('https://jsonplaceholder.typicode.com/todos', params=pay)
    u = requests.get('https://jsonplaceholder.typicode.com/users', params=pay1)

    user = u.json()
    todos = r.json()
    name = user[0]['name']

    complete = 0
    for todo in todos:
        if todo["completed"]:
            complete = complete + 1

    print(f"Employee {name} is done with tasks({complete}/{len(todos)}):")

    for todo in todos:
        if todo["completed"]:
            print('\t ' + todo['title'])
