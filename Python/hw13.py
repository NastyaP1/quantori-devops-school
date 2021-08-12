# Homework 13
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw13.txt
#
# ###############################################################################
#


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5.0 * (fahrenheit - 32) / 9


def interactive_input():

    temperature = input("What temperature to convert? Please enter the number: \n")

    try:
        print('Input temperature is {}'.format(float(temperature)))
        temperature = float(temperature)
    except ValueError as err:
        print('Error you did not give a number, please, try one more time')
        print("=====================================================================")
        interactive_input()

    print("=====================================================================")

    type_of_temperature = input("If you want to convert it to fahrenheit, please, enter 1\nIf you want to convert it to celsius, "
                                "please, enter 2\nTo exit enter 3\n")

    print("=====================================================================")

    if type_of_temperature == '1':
        print('The temperature will be ' + str(celsius_to_fahrenheit(temperature)) + 'F')
    elif type_of_temperature == '2':
        print('The temperature will be ' + str(fahrenheit_to_celsius(temperature)) + 'C')
    elif type_of_temperature == '3':
        exit(0)
    else:
        print("You've entered incorrect option, please, try one more time")

    print("=====================================================================")
    interactive_input()


if __name__ == '__main__':
    interactive_input()
