# Homework 5
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw5.txt
#
# ###############################################################################
#
if __name__ == '__main__':
    list_of_numbers = sorted([int(item) for item in input("Enter the list items : ").split()])
    for i in range(1, len(list_of_numbers) + 1):
        if i not in list_of_numbers:
            nextNumber = i
            break
        if i == len(list_of_numbers):
            nextNumber = list_of_numbers[-1] + 1
    print("==========================================")
    print(nextNumber)
