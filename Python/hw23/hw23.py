# Homework 23
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw23.txt
#
# ###############################################################################


from copy import deepcopy


def gen_n_dimensional_array(array):
    try:
        for var in array:
            assert isinstance(var, int)
    except AssertionError:
        return "Input an integer!"

    n = len(array)
    last_el = array[-1]
    array.remove(array[-1])
    if n < 2:
        return [""] * last_el
    else:
        interim_arr = gen_n_dimensional_array(array)
        return [deepcopy(interim_arr) for i in range(last_el)]


ar = (gen_n_dimensional_array([2, 3, 3]))
ar[0][2][1] = 'x'
print(ar)
