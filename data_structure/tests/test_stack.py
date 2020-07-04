"""
Testing Stack Class
"""
import unittest
from data_structure.stack import Stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack._head, None)

        stack.add_item("first_item")
        self.assertEqual(stack.peek(), "first_item")

        stack.add_item("second_item")
        self.assertEqual(stack.peek(), "second_item")

        stack.remove_item()
        self.assertEqual(stack.peek(), "first_item")

        stack.remove_item()
        self.assertEqual(stack.is_empty(), True)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack._head, None)


if __name__ == "__main__":
    unittest.main()
