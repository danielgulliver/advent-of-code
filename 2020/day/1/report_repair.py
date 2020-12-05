import math

def two_sum_to(my_list, total):
    for item in my_list:
        remainder = total - item
        if remainder > 0:
            list_copy = my_list.copy()
            list_copy.remove(item)
            if remainder in list_copy:
                return (item, remainder)
    return None

def three_sum_to(my_list, total):
    # for i in my_list:
    #     for j in my_list:
    #         for k in my_list:
    #             if i != j and j != k and i + j + k == total:
    #                 return (i, j, k)
    # return None
    for item in my_list:
        my_list.remove(item)
        remainder = total - item
        
        if remainder > 0:
            result = two_sum_to(my_list, total - item)
            if result is not None:
                return (item, result[0], result[1])
    return None

if __name__ == '__main__':
    test_result = two_sum_to([1721, 979, 366, 299, 675, 1456], 2020)
    # assert test_result == (1721, 299) or test_result == (299, 1721)
    print(test_result)
    
    with open('input.txt', 'r') as f:
        expenses = [int(n.strip()) for n in f.readlines()]
        result = two_sum_to(expenses, 2020)

        if result is not None:
            print('{} * {} = {}'.format(result[0], result[1], result[0] * result[1]))
        else:
            print('Result not found')

        result = three_sum_to(expenses, 2020)

        if result is not None:
            print('{} * {} * {} = {}'.format(result[0], result[1], result[2], result[0] * result[1] * result[2]))
        else:
            print('Result not found')