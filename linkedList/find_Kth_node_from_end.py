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

    for i in range(index-1):
        if fast_pointer.next:
            fast_pointer = fast_pointer.next
        else:
            return None

    while fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

if result.value:
    print(result.value)  # Output: 4
else:
    print(result)



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""

