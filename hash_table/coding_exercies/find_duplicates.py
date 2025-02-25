# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################


def find_duplicates(arr):
    ret = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in ret:
                ret.append(arr[i])
    return ret

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

