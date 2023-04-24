#!/usr/bin/python3
"""Given employee ID, the script exports data in CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    id2 = {'userId': argv[1]}
    id1 = {'id': argv[1]}

    t = requests.get('https://jsonplaceholder.typicode.com/todos', params=id2)
    u = requests.get('https://jsonplaceholder.typicode.com/users', params=id1)

    todos = t.json()
    user = u.json()

    username = user[0]['username']

    # Add username to todos obj
    for todo in todos:
        todo['un'] = username

    # Open csv file for writing
    with open(f'{argv[1]}.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for todo in todos:
            d = [todo['userId'], todo['un'], todo['completed'], todo['title']]
            writer.writerow(d)
