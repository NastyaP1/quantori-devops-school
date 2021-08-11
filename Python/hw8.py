# Homework 8
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw8.txt
#
# ###############################################################################
#
import re


def compute():

    input_value = input("\nEnter the text : ")

    if input_value == "cancel":
        print("Bye!")
    else:
        if re.search(r'\D', input_value):
            print("Не удалось преобразовать введенный текст в число.")
        elif int(input_value) % 2 == 0:
            result = int(input_value) // 2
            print(result)
        else:
            result = int(input_value) * 3 + 1
            print(result)

            compute()


if __name__ == '__main__':
    compute()
