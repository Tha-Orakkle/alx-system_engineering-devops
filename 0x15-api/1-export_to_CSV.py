#!/usr/bin/python3
"""
Returns information about employee's todo list using api
and identifies the employee by the id passed as the argument
"""
import csv
import requests
import sys


def todo_list(employee_id):
    """
    Gets information about an employee
        Arsgs:
            employee_id (int) - id of employee

    Return Values:

        idx 0 (dict) - Employee data
        idx 1 (dict) - All the tasks of the employee and the status
        idx 2 (str)  - tasks done by the employee
    """

    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(employee_id))
    if response.status_code == 200:
        employee_data = response.json()
        employee_name = employee_data.get('name')

    response = requests.get(url + "todos", params={"userId": employee_id})
    if response.status_code == 200:
        todos = response.json()

    all_tasks = {}
    for task in todos:
        t = (task['title'])
        status = task['completed']
        all_tasks[t] = status

    completed_tasks = [task['title'] for task in todos if task['completed']]
    firstline = "Employee {} is done with tasks({}/{}):"
    result = firstline.format(employee_name, len(completed_tasks), len(todos))

    for task in completed_tasks:
        result += "\n\t {}".format(task)

    return [employee_data, all_tasks, result]


def save_csv(employee_id):
    """saves info in csv fomat"""

    emp_id = employee_id
    data = []
    employee = todo_list(emp_id)
    all_tasks = employee[1]
    username = employee[0].get('username')
    for task, status in all_tasks.items():
        row = [emp_id, username, status, task]
        data.append(row)

    with open("{}.csv".format(emp_id), 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <python file> <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            save_csv(employee_id)
        except ValueError:
            print("employee_id must be a valid id (int)")
