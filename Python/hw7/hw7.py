# Homework 7
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw7.txt
#
# ###############################################################################
#


def count_shells(file):
    f = open(file)
    shell_count = {}
    for line in f:
        shell = line.rstrip().split(':')[-1]
        if shell not in shell_count:
            shell_count[shell] = 1
        else:
            shell_count[shell] += 1
    f.close()
    return shell_count


def set_groups(file):
    f = open(file)
    group_dict = {}
    for line in f:
        group_name = line.rstrip().split(':')[0]
        group_id = line.rstrip().split(':')[2]
        group_dict[int(group_id)] = group_name
    f.close()
    return group_dict


def set_users(file):
    f = open(file)
    users_dict = {}
    for line in f:
        user_id = line.rstrip().split(':')[2]
        group_id = line.rstrip().split(':')[3]
        users_dict[user_id] = int(group_id)
    f.close()
    return users_dict


def print_dict_as_text(dct):
    res = ''
    for item, amount in dct.items():
        res = res + "{} - {}".format(amount, item) + " ; "
    return res


def write_to_file(file, data):
    with open(file, 'a') as f:
        f.write(data)
        f.write('\n')
    f.close()


def search_uids_per_group(group_dict, users_dict):
    res = ''
    for group_id, group_name in group_dict.items():
        users_id = [user_id for (user_id, user_group_id) in users_dict.items() if group_id == user_group_id]
        if len(users_id) != 0:
            res = res + "{} - {}".format(group_name, ",".join(users_id)) + " , "
    return res


if __name__ == '__main__':
    shells = count_shells("resources/passwd")
    groups = set_groups("resources/group")
    users = set_users("resources/passwd")

    print(print_dict_as_text(count_shells("resources/passwd")))

    write_to_file('output.txt', print_dict_as_text(count_shells("resources/passwd")))
    write_to_file('output.txt', search_uids_per_group(groups, users))
