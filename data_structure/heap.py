from typing import List


class MinHeap:
    def __init__(self, array: List = None):
        """
        if array is given, heapify by building the heap
        otherwise just instantiate the object with an empty list
        """
        if array is None:
            self._array = list()
        else:
            self._array = array
            self.build_heap()

    @staticmethod
    def get_parent_index(current_index):
        """
        :param current_index: the node you get the parents from
        :return: the parent's index
        """
        return int((current_index - 1) / 2)

    @staticmethod
    def get_left_child_index(current_index):
        """
        :param current_index: node where you want to get children from
        :return: left child's indes
        """
        return current_index * 2 + 1

    @staticmethod
    def get_right_child_index(current_index):
        """
        :param current_index: node where you get children from
        :return: right child's index
        """
        return current_index * 2 + 2

    def peek(self):
        return self._array[0]

    def heapify_up(self, index):
        """
        Get the parent index, if element in parent index is greater, swap
        """
        parent = self.get_parent_index(index)

        if self._array[index] < self._array[parent] and parent >= 0:
            self._array[index], self._array[parent] = \
                self._array[parent], self._array[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        """
        The basic algo in heapify down is get the left and right child supposed index
        from there, you check if the index is smaller than length of array
        then you find the smallest one
        """
        left_child = self.get_left_child_index(index)
        right_child = self.get_right_child_index(index)
        arr_length = len(self._array)

        if left_child >= arr_length or right_child >= arr_length:
            return

        if self._array[left_child] < self._array[right_child] \
                and self._array[left_child] < self._array[index]:
            self._array[left_child], self._array[index] =\
                self._array[index], self._array[left_child]
            self.heapify_down(left_child)
        elif self._array[right_child] < self._array[index]:
            self._array[right_child], self._array[index] =\
                self._array[index], self._array[right_child]
            self.heapify_down(right_child)

    def insert(self, value):
        """
        In languages with static array, you need to check array size.
        Might need to double in size in order to add.
        """
        self._array.append(value)
        self.heapify_up(len(self._array)-1)

    def delete(self):
        """
        """
        self._array[0] = self._array.pop(-1)
        self.heapify_down(0)

    def build_heap(self):
        """
        Start from the last parent and bubble all element down
        Last parent is where the last child leaf is
        """
        last_parent_index = self.get_parent_index(len(self._array) - 1)

        for i in range(last_parent_index, -1, -1):
            self.heapify_down(i)
