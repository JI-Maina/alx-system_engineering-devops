#!/usr/bin/python3
"""This module provides a script that given an employee ID, returns information
about his/her TODO list progress.

Format:
    Employee EMPLOYEE_NAME is done with tasks(N0_OF_DONE_TASKS/N0_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks
"""

if __name__ == "__main__":
    import requests
    from sys import argv

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

    print(
            "Employee {} is done with tasks({}/{}):"
            .format(name, complete, len(todos)))

    for todo in todos:
        if todo["completed"]:
            print('\t ' + todo['title'])
