# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################

def two_sum(arr, num):
    my_dict = {}
    for i, val in enumerate(arr):
        my_dict[val] = i
    print(my_dict)
    for i, val in enumerate(arr):
        target = num - val
        idx = my_dict.get(target, -1)
        if i != idx and idx != -1:
            return [i, idx]
    return []
    
    
    
print(two_sum([5,25,75], 100))  
# print(two_sum([4, 2, 11, 7, 6, 3], 9))  
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
# print(two_sum([1, 3, 5, 7, 9], 10))  
# print ( two_sum([1, 2, 3, 4, 5], 10) )
# print ( two_sum([1, 2, 3, 4, 5], 7) )
# print ( two_sum([1, 2, 3, 4, 5], 3) )
# print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


