# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################

def longest_consecutive_sequence(arr):
    my_set = set(arr)
    counter = 1
    max = 0
    for i in arr:
        loop_iterator = i
        while loop_iterator + 1 in my_set:
            loop_iterator += 1
            counter+=1
        if counter > max:
            max = counter
        counter = 1 
    return max
        



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""