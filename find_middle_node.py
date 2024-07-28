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


    def find_middle_node(self):
        # ret = self.head
        slow_pointer = self.head
        fast_pointer = self.head
        while (fast_pointer.next and fast_pointer.next.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if fast_pointer.next != None and fast_pointer.next.next == None:
                print(fast_pointer.next)
                slow_pointer = slow_pointer.next

        print(slow_pointer.value)

        return slow_pointer





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.append(5)

print( my_linked_list.find_middle_node().value)



"""
    EXPECTED OUTPUT:
    ----------------
    3

"""