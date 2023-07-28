#!/usr/bin/python3
"""
Returns information about employee's todo list using api
and identifies the employee by the id passed as the argument
"""
import csv
import requests
import sys


class Employee:
    """model for employee information"""
    __url = "https://jsonplaceholder.typicode.com/"

    def __init__(self, id=0):
        """initialisation"""
        self.id = id

    def employee_data(self):
        """Returns the employee data"""
        response = requests.get(Employee.__url + "users/{}".format(self.id))
        if response.status_code == 200:
            return response.json()

    def todo_list(self):
        """Return the all tasks of the employee"""
        response = requests.get(Employee.__url + "todos",
                                params={"userId": self.id})
        if response.status_code == 200:
            return response.json()

    def todo_progress(self):
        """Returns all completed tasks of the employee"""
        employee_name = self.employee_data().get('name')
        todo = self.todo_list()
        tasks_done = [task['title'] for task in todo if task['completed']]
        result = "Employee {} is done with tasks({}/{}):"\
            .format(employee_name, len(tasks_done),
                    len(todo))

        for task in tasks_done:
            result += "\n\t {}".format(task)

        return result

    def save_csv(self):
        """saves data in csv format"""
        todo = self.todo_list()
        username = self.employee_data().get('username')
        data = []
        for task in todo:
            row = [self.id, username, task['completed'], task['title']]
            data.append(row)

        with open("{}.csv".format(self.id), 'w', newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            writer.writerows(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <python file> <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])
            employee = Employee(emp_id)
            employee.save_csv()
        except ValueError:
            print("employee_id must be a valid id (int)")
