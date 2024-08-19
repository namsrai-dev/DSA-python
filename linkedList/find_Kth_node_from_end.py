class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(list, index):
    fast_pointer = list.head
    slow_pointer = list.head
    is_found = False
    while fast_pointer.next:
        print("fast_pointer.value", fast_pointer.value)
        if fast_pointer.value == index and fast_pointer.next:
            print("True")
            is_found = True
        fast_pointer = fast_pointer.next
        if is_found:
            slow_pointer = slow_pointer.next



    return slow_pointer if is_found else None




my_linked_list = LinkedList()
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)


k = 5
result = find_kth_from_end(my_linked_list, k)

# print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""

