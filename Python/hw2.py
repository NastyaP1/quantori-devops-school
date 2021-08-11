# Homework 2
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw2.txt
#
# ###############################################################################
#
if __name__ == '__main__':
    list_of_items = [item for item in input("Enter the list items : ").split()]
    output = []
    [output.append(i) for i in list_of_items if i not in output]

    print("==========================================")
    print(" ".join(output))
