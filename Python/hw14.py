# Homework 14
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw14.txt
#
# ###############################################################################
#
import pickle


class Employee:
    count = 0
    ids_list = []

    def __init__(self, name, department, salary):
        self.__name = name
        self.__emp_id = Employee.count + 1
        self.__salary = salary
        self.__department = department

        self.ids_list.append(self.__emp_id)
        Employee.count += 1

    def set_name(self, name):
        self.__name = name

    def set_id(self, emp_id):
        self.__emp_id = emp_id

    def set_department(self, department):
        self.__department = department

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__emp_id

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def display_count(self):
        print("Total Employee %d" % self.count)

    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nID: ' + str(self.__emp_id) + \
               '\nDepartment: ' + self.__department + \
               '\nSalary: ' + str(self.__salary)


def dump_emp(emp, file):
    with open(file, 'wb') as f:
        pickle.dump(emp, f)
    f.close()


emp1 = Employee("Mary", "Network Department", 2000)
dump_emp(emp1, 'file.pickle')
