# Homework 8
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw8.txt
#
# ###############################################################################
#
import re


def convert_str_to_int(s):
    if re.search(r'\D', s):
        return False
    else:
        if s:
            return (ord(s[-1]) - ord('0')) + 10 * convert_str_to_int(s[:-1])
        else:
            return 0


def compute():

    input_value = input("\nEnter the text : ")

    if input_value == "cancel":
        print("Bye!")
    else:
        output = convert_str_to_int(input_value)
        if not output:
            print("Не удалось преобразовать введенный текст в число.")
        elif output % 2 == 0:
            result = output // 2
            print(result)
        else:
            result = output * 3 + 1
            print(result)

            compute()


if __name__ == '__main__':
    compute()
