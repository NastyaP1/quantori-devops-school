# Homework 11
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw11.txt
#
# ###############################################################################
#
from string import ascii_letters


def letters_range(start, stop, step=1):
    output = []
    for i in range(ascii_letters.index(start), ascii_letters.index(stop), step):
        output.append(ascii_letters[i])
    print(output)


if __name__ == '__main__':
    letters_range('b', 'w', 2)
    letters_range('a', 'g')
    letters_range('g', 'p')
    letters_range('p', 'g', -2)
    letters_range('a', 'a')
