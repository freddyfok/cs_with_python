"""
Testing Queue class
"""

import unittest
from data_structure.queue import Queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        self.assertEqual(queue.is_empty(), True)
        self.assertEqual(queue.peek(), None)

        queue.queue("first_in_line")
        self.assertEqual(queue.peek(), "first_in_line")
        self.assertEqual(queue.is_empty(), False)

        queue.queue("second_in_line")
        self.assertEqual(queue.de_queue(), "first_in_line")
        self.assertEqual(queue.peek(), "second_in_line")

        self.assertEqual(queue.de_queue(), "second_in_line")
        self.assertEqual(queue.is_empty(), True)
        self.assertEqual(queue.peek(), None)
