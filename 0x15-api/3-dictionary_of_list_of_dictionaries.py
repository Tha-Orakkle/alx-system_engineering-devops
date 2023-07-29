#!/usr/bin/python3
"""
Returns information about employee's todo list using api
and identifies the employee by the id passed as the argument
"""
import csv
import json
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

    def to_dict(self, emp_id=0):
        """creates a dictionary of an employee's tasks"""

        if emp_id == 0:
            username = self.employee_data().get('username')
            todo = self.todo_list()
        else:
            username = requests.get(Employee.__url + "users/{}"
                                    .format(emp_id)).json().get('username')
            todo = requests.get(Employee.__url + "todos",
                                params={"userId": emp_id}).json()
        data = {}
        all_tasks = []
        for item in todo:
            task = {}
            task['task'] = item['title']
            task['completed'] = item['completed']
            task['username'] = username
            all_tasks.append(task)
        data[str(self.id)] = all_tasks

        return data

    def save_json(self):
        """saves data in json format"""
        if self.id != 0:
            data = self.to_dict()
            with open("{}.json".format(self.id), 'w', newline="") as jsonfile:
                json.dump(data, jsonfile)
        else:
            response = requests.get(Employee.__url + "users")
            if response.status_code == 200:
                employees = response.json()
            all_employees_tasks = {}
            for emp in employees:
                emp_id = emp.get('id')
                dic = self.to_dict(emp_id)
                all_employees_tasks[str(emp_id)] = list(dic.values())[0]
            with open("todo_all_employees.json", 'w', newline='') as jsonfile:
                json.dump(all_employees_tasks, jsonfile)


if __name__ == "__main__":
    employee = Employee()
    employee.save_json()
