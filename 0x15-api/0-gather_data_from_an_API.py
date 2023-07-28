#!/usr/bin/python3
"""
Returns information about employee's todo list using api
"""
import os
import requests


def to_do_list(employee_id):
    #pass



if __name__ == "__main__":

    if len(os.argv) != 2:
        print("Usage: python3 <python file> <employee_id>")
    else
        try:
            employee_id = int(sys.argv[1])
            print(todo_list(employee_id), end='')
        except ValueError:
            print("employee_id must be a valid id (int)")

