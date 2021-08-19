# Homework 14
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw14.txt
#
# ###############################################################################
#
import pickle
import Python.hw14


def load_emp(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    f.close()
    return data


emp2 = load_emp('file.pickle')
print(emp2)
