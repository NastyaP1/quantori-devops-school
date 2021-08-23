# Homework 6
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw6.txt
#
# ###############################################################################
#


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    return s == reverse(s)


def binary_str(n):
    return "{0:b}".format(n)


if __name__ == '__main__':
    result = sum(i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(binary_str(i)))
    print("==========================================")
    print(result)
