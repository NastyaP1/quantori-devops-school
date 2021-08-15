# Homework 21
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw21.txt
#
# ###############################################################################


def concatenate_list(list1, list2):
    joined_list = []
    joined_list += (list1 + list2)

    return sorted(joined_list)


if __name__ == '__main__':
    print(concatenate_list([x for x in range(1, 4)], [x for x in range(2, 5)]))
