# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################

def find_pairs(arr1, arr2, target):
    my_dict = {}
    for i in arr1:
        my_dict[i] = True
    arr = []
    for i in arr2:
        if target - i in my_dict:
            arr.append((target - i, i))
    return arr



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""