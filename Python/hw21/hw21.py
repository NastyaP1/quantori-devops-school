# Homework 21
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw21.txt
#
# ###############################################################################


class NextValueWrapper(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_value = None
        self.finished = False
        self.get()

    def get(self):
        if self.finished:
            return
        value = self.next_value
        try:
            self.next_value = next(self.iterator)
        except StopIteration:
            self.finished = True
        return value


def iter_merge(iter1, iter2):

    wrap1 = NextValueWrapper(iter1)
    wrap2 = NextValueWrapper(iter2)

    while not (wrap1.finished and wrap2.finished):
        if (wrap2.finished or
               (not wrap1.finished and
                wrap1.next_value <= wrap2.next_value)):
            yield wrap1.get()
        else:
            yield wrap2.get()


if __name__ == '__main__':
    it1 = iter([1, 3, 5, 7])
    it2 = (x for x in range(2, 6))
    for item in iter_merge(it1, it2):
        print(item)
