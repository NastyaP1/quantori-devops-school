# Homework 10
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw10.txt
#
# ###############################################################################
#


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


if __name__ == '__main__':
    digits = [5, 4, 8]

    for i in digits:
        steps = 0
        output = i

        print("==========================================")
        print("Collatz conjecture fot digit: {}".format(i))
        while output != 1:
            output = collatz(output)
            steps += 1
            print(output)

        print('Steps: ', steps)
