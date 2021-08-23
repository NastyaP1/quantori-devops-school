# Homework 4
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw4.txt
#
# ###############################################################################
#
if __name__ == '__main__':
    input_string = input("Enter the string: ")

    sum = 0
    index = 0
    is_dash = False

    while index < len(input_string):
        result = ''
        digit = input_string[index]

        if digit == '-' and not input_string[index - 1].isdigit():
            is_dash = True

        while digit.isdigit():
            result += digit
            index += 1
            if index < len(input_string):
                digit = input_string[index]
            else:
                break
        index += 1
        if result != '':
            if is_dash:
                sum -= int(result)
                is_dash = False
            else:
                sum += int(result)

    print(sum)
