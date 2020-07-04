import unittest

from data_structure.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def tearDown(self) -> None:
        del self.linked_list

    def test_list(self):
        self.assertEqual(self.linked_list.is_empty(), True)
        self.linked_list.append(5)
        self.assertEqual(self.linked_list.is_empty(), False)
        self.assertEqual(self.linked_list.head.value, 5)

        self.linked_list.append(10)
        self.linked_list.append(15)

        self.linked_list.delete_with_value(10)
        self.assertEqual(self.linked_list.head.next_node.value, 15)

        self.linked_list.prepend(2)
        self.assertEqual(self.linked_list.head.value, 2)

        self.linked_list.delete_with_value(2)
        self.assertEqual(self.linked_list.head.value, 5)


