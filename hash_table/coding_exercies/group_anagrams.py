# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################
def group_anagrams(arr):
    second_arr = []
    for i in arr:
        is_found = False
        for ind, val in enumerate(second_arr):
            str1 = val[0]
            str2 = i
            if len(str1) == len(str2):
                dict1 = to_dict(str1)
                dict2 = to_dict(str2)
                if is_found is False and dict1 == dict2:
                    second_arr[ind].append(i)
                    is_found = True
        if not is_found:
            second_arr.append([i])

    return second_arr
    
    # print("dict1:", dict1)
    # print("dict2:", dict2)

    # print("is equal:", dict1 == dict2)  # This should print False

def to_dict(s):
    my_dict = {}
    for i in s:
        my_dict[i] = True
    return my_dict  # Remove unnecessary print statements
        

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""