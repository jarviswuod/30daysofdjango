
def find_max(list_num):
    max_num = list_num[0]
    for number in list_num:
        if number > max_num:
            max_num = number
    return max_num

