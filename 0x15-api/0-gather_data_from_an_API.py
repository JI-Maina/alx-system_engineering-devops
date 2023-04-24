#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list progress"""

from sys import argv
import requests

if __name__ == "__main__":
    pay = {'userId': argv[1]}
    pay1 = {'id': argv[1]}

    r = requests.get('https://jsonplaceholder.typicode.com/todos', params=pay)
    u = requests.get('https://jsonplaceholder.typicode.com/users', params=pay1)

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
