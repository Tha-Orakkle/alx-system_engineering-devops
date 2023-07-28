#!/usr/bin/python3
"""
Returns information about employee's todo list using api
and identifies the employee by the id passed as the argument
"""
import requests
import sys


def todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(employee_id))
    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data.get('name')

    response = requests.get(url + "todos", params={"userId": employee_id})
    if response.status_code == 200:
        todos = response.json()

    completed_tasks = [task['title'] for task in todos if task['completed']]
    firstline = "Employee {} is done with tasks({}/{}):"
    result = firstline.format(employee_name, len(completed_tasks), len(todos))

    for task in completed_tasks:
        result += "\n\t {}".format(task)

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <python file> <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            print(todo_list(employee_id))
        except ValueError:
            print("employee_id must be a valid id (int)")
