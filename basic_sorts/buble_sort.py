
# Bubble Sort
# Write a function called bubble_sort that sorts a list of integers in ascending order using the Bubble Sort algorithm.

# The function should perform the following tasks:

# Accept a parameter my_list that represents the list of integers to be sorted.

# Iterate through the list from the last element to the first element. For each element i, perform the following steps:

# Iterate through the list from the first element to the element at position i - 1. For each element j, perform the following steps:

# Compare the element at position j with the element at position j + 1. If the element at position j is greater than the element at position j + 1, swap the two elements.

# Return the sorted list.

def bubble_sort(my_list):
    for i in range(len(my_list), 0, -1):
        for j in range(i-1):
            if my_list[j+1] < my_list[j]:
                temp = my_list[j+1]
                my_list[j+1] = my_list[j]
                my_list[j] = temp
            print("compared two index", j, j+1)
    return my_list



print(bubble_sort([4,2,6,5,1,3])) 