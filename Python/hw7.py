# Homework 7
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw7.txt
#
# ###############################################################################
#


def count_shells(file):
    f = open(file)
    for line in f:
        shell = line.rstrip().split(':')[-1]
        if shell not in shell_count:
            shell_count[shell] = 1
        else:
            shell_count[shell] += 1
    f.close()


def set_groups(file):
    f = open(file)
    for line in f:
        group_name = line.rstrip().split(':')[0]
        group_id = line.rstrip().split(':')[2]
        group_dict[int(group_id)] = group_name
    f.close()


def set_users(file):
    f = open(file)
    for line in f:
        user_id = line.rstrip().split(':')[2]
        group_id = line.rstrip().split(':')[3]
        users_dict[user_id] = int(group_id)
    f.close()


def print_dict_as_text(dct):
    res = ''
    for item, amount in dct.items():
        res = res + "{} - {}".format(amount, item) + " ; "
    print(res)


def search_uids_per_group():
    res = ''
    for group_id, group_name in group_dict.items():
        users_id = [user_id for (user_id, user_group_id) in users_dict.items() if group_id == user_group_id]
        if len(users_id) != 0:
            res = res + "{} - {}".format(group_name, ",".join(users_id)) + " , "
    print(res)


if __name__ == '__main__':
    shell_count = {}
    count_shells("resources/passwd")
    print("==========================================================================")
    print_dict_as_text(shell_count)

    group_dict = {}
    users_dict = {}

    set_groups("resources/group")

    set_users("resources/passwd")

    print("==========================================================================")
    search_uids_per_group()
