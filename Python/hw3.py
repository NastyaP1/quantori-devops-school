# Homework 3
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw3.txt
#
# ###############################################################################
#
if __name__ == '__main__':
    list_of_words = input("Enter the list items : ")
    word_count = {}
    for x in list_of_words.lower().split():
        if x not in word_count:
            word_count[x] = 1
        else:
            word_count[x] += 1

    n = max(word_count.values())

    print("==========================================")
    for item, amount in word_count.items():
        if amount == n:
            print("{} - {}".format(amount, item))
