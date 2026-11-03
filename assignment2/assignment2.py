
# Task 2

import csv
import traceback
import os #task 10
import custom_module #task 11
from datetime import datetime #task 14

def read_employees():
    employees = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if "fields" not in employees:
                    employees["fields"] = row
                else:
                    rows.append(row)

            employees["rows"] = rows

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, Message : {trace[3]}"
            )

        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")

        message = str(e)
        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")
        raise SystemExit(1)

    return employees

#Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

#Task 4
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(
        lambda row: int(row[employee_id_column]) == employee_id,
        employees["rows"]
    ))
    return matches

#Task 7

def sort_by_last_name():
    employees["rows"].sort(
        key=lambda row: row[column_index("last_name")]
    )
    return employees["rows"]


# Task 8
def employee_dict(row):
    employee = {}

    for index in range(len(employees["fields"])):
        if employees["fields"][index] != "employee_id":
            employee[employees["fields"][index]] = row[index]

    return employee



# Task 9
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees


# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

#Task 12
def read_minutes_file(filename):
    minutes = {}
    rows = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if "fields" not in minutes:
                minutes["fields"] = row
            else:
                rows.append(tuple(row))

        minutes["rows"] = rows

    return minutes

def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")

    return minutes1, minutes2


# Task 13
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    return minutes1_set.union(minutes2_set)


# Task 14
def create_minutes_list():
    minutes = list(minutes_set)

    minutes_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes
    ))

    return minutes_list

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list




employees = read_employees()
print(employees)

#Task 3
employee_id_column = column_index("employee_id")

#Task 7
sort_by_last_name()
print(employees)

#Task 8
print(employee_dict(employees["rows"][0]))

#Task 9
print(all_employees_dict())

#Task 10
print(get_this_value())

#Task 11
set_that_secret("my_new_secret")
print(custom_module.secret)

#Task 12
minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

#Task 13
minutes_set = create_minutes_set()
print(minutes_set)

#Task 14
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15 
sorted_minutes = write_sorted_list()
print(sorted_minutes)