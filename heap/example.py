# # Enables Python 3 print function behavior in Python 2 environments
# from __future__ import print_function
# import math

# class MinHeap:
#     def __init__(self):
#         # Initialize the heap as an empty list
#         self.arr = []

#     # Get the index of the left child
#     def left(self, i): return 2 * i + 1

#     # Get the index of the right child
#     def right(self, i): return 2 * i + 2

#     # Get the index of the parent
#     def parent(self, i): return (i - 1) // 2
    
#     # Return the minimum element without removing it
#     def get_min(self):
#         return self.arr[0] if self.arr else None
    
#     # Insert a new key into the heap
#     def insert(self, k):
#         self.arr.append(k)
#         i = len(self.arr) - 1
        
#         # Fix the min heap property by bubbling up
#         while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
#             p = self.parent(i)
#             self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
#             i = p

#     # Decrease the value of a key at a specific index
#     def decrease_key(self, i, new_val):
#         self.arr[i] = new_val
        
#         # Percolate the new smaller value up to maintain heap property
#         while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
#             p = self.parent(i)
#             self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
#             i = p

#     # Remove and return the root (minimum) element
#     def extract_min(self):
#         if len(self.arr) <= 0: return None
#         if len(self.arr) == 1: return self.arr.pop()
        
#         res = self.arr[0]
#         # Replace root with the last element and heapify down
#         self.arr[0] = self.arr.pop() 
#         self.min_heapify(0)
#         return res

#     # Delete a key at index i by forcing it to root and extracting
#     def delete_key(self, i):
      
#         # Use negative infinity to ensure it becomes the new root
#         self.decrease_key(i, -float('inf'))
        
#         # Remove the forced root
#         self.extract_min()

#     # Recursive method to fix the heap property downwards
#     def min_heapify(self, i):
#         l, r, n = self.left(i), self.right(i), len(self.arr)
#         smallest = i
        
#         # Find the smallest among root, left child, and right child
#         if l < n and self.arr[l] < self.arr[smallest]: smallest = l
#         if r < n and self.arr[r] < self.arr[smallest]: smallest = r
          
#         # If the root is not the smallest, swap and continue heapifying
#         if smallest != i:
#             self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
#             self.min_heapify(smallest)

# # --- Execution ---
# h = MinHeap()
# h.insert(3)
# h.insert(2)
# h.delete_key(1)
# h.insert(15)
# h.insert(5)
# h.insert(4)
# h.insert(45)

# # Prints values on the same line separated by spaces
# print(h.extract_min(), end=" ") 
# print(h.get_min(), end=" ") 

# h.decrease_key(2, 1)
# print(h.extract_min())

# class MinHeap:
#     def __init__(self):
#         # Initialize the heap as an empty list
#         self.arr = []

#     def parent(self, i): return (i - 1) // 2

#     # Insert a new key into the heap
#     def insert(self, k):
#         self.arr.append(k)
#         i = len(self.arr) - 1

#         print("i",i)
        
#         # Fix the min heap property by bubbling up
#         while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
#             print("while working")
#             p = self.parent(i)
#             print("parent is", p)
#             self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
#             i = p

#     def get_arr(self):
#         return self.arr


class MinHeap:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i-1) // 2
    
    def get_arr(self):
        return self.arr

    def insert(self, num):
        self.arr.append(num)

        i = len(self.arr) - 1
        

        while i > 0 and self.arr[self.parent(i)] < self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]

            i = p



heap = MinHeap()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
print(heap.get_arr())