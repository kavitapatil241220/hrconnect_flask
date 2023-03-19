"""
Write a program to get details of employees who's salary is > 9000. The output should
be in following format
"""

from typing import List

from utils.csvfile import HandleCSV


def get_data_info() -> List:
    reader = HandleCSV.read_entire_csv()
    emp_data = {}
    j = 1
    for i in reader:
        if int(i["SALARY"]) > 9000:
            emp_data[j] = {"Name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                      "email": i["EMAIL"], "Phone": i["PHONE_NUMBER"].replace(".", "")}
            j += 1
    return emp_data



if __name__ == "__main__":
    print(get_data_info())