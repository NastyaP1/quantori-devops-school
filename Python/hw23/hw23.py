# Homework 23
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw23.txt
#
# ###############################################################################


def gen_n_dimensional_array(size):
    try:
        for var in size:
            assert isinstance(var, int)
    except AssertionError:
        return "Input an integer!"
    array = ""
    for var in size:
        array = [array] * var
    return array


if __name__ == '__main__':
    print(gen_n_dimensional_array([2, 2]))
    print(gen_n_dimensional_array([2, 2, 2]))
