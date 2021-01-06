"""
in place
unstable sort (stable sort means that order is maintained after sort if it has a key)
(in other words, it is not guaranteed that the object appearing first will also appear first when it is sorted)


heap sort uses the heap data structure
for ascending order sort, build a max heap
for descending order sort, build a min heap

algorithm:
from a max heap, you swap the root element with the next available last element
you then "disconnect" the available last element from the heap
then heapify the root element

ie. from a heap heap
17, 15, 12, 5, 6, 7, 10
   17
 15  12
5 6 7 10

17 is now fixed, then you heapify 10
10, 15, 12, 5, 6, 7, [17]
   10
 15  12
5 6 7 17
"""
from typing import List


class MaxHeap:
    def __init__(self, array: List = None):
        if array is None:
            self._array = list()
        else:
            self._array = array
            self._build_heap()

    @staticmethod
    def get_parent_index(current_index):
        return (current_index - 1) // 2

    @staticmethod
    def get_left_child_index(current_index):
        return current_index * 2 + 1

    @staticmethod
    def get_right_child_index(current_index):
        return current_index * 2 + 2

    def heapify_down(self, starting_index, arr_length):
        left_index = self.get_left_child_index(starting_index)
        right_index = self.get_right_child_index(starting_index)
        largest = starting_index

        if left_index < arr_length and\
                self._array[left_index] > self._array[starting_index]:
            largest = left_index

        if right_index < arr_length and\
                self._array[right_index] > self._array[starting_index]:
            largest = right_index

        if largest != starting_index:
            self._array[largest], self._array[starting_index] =\
                self._array[starting_index], self._array[largest]
            self.heapify_down(largest, arr_length)

    def heapify_up(self, starting_index):
        parent_index = self.get_parent_index(starting_index)

        if parent_index >= 0 and\
                self._array[starting_index] > self._array[parent_index]:
            self._array[starting_index], self._array[parent_index] = self._array[parent_index], self._array[starting_index]
            self.heapify_up(parent_index)

    def _build_heap(self):
        # start from the last parent, heapify down
        arr_length = len(self._array)
        last_parent_index = self.get_parent_index(arr_length-1)
        for i in range(last_parent_index, -1, -1):
            self.heapify_down(last_parent_index, arr_length)

    def peek(self):
        return self._array[0]

    def remove(self):
        self._array[0] = self._array.pop(-1)
        self.heapify_down(0, len(self._array))

    def insert(self, value):
        self._array.append(value)
        self.heapify_up(len(self._array)-1)

    def sort(self):
        last_index = len(self._array) - 1
        for i in range(len(self._array)):
            self._array[0], self._array[last_index] = \
                self._array[last_index], self._array[0]
            last_index -= 1
            self.heapify_down(0, last_index)
