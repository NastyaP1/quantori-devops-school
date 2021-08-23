# Homework 12
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw12.txt
#
# ###############################################################################
#


def fib(n):
    fib1, fib2 = 1, 1

    for i in range(n - 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib1


if __name__ == '__main__':
    n = int(input("Enter the position: "))
    print("=============================================")
    print("Value of {}-position is {}".format(n, fib(n)))
