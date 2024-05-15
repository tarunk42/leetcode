import unittest
import sys
import os

# Adjust the Python path to find the linkedlist module
sys.path.append(os.path.join(os.path.dirname(__file__), '../build/lib'))

from linkedlist.LinkedList import linkedList

class TestLinkedList(unittest.TestCase):
    
    def test_add(self):
        ll = linkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(repr(ll), "[1, 2, 3]")

    def test_contains(self):
        ll = linkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertTrue(ll.contains(2))
        self.assertFalse(ll.contains(4))

    def test_delete(self):
        ll = linkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertTrue(ll.delete(2))
        self.assertEqual(repr(ll), "[1, 3]")
        self.assertFalse(ll.delete(4))

    def test_insert(self):
        ll = linkedList()
        ll.add(1)
        ll.add(3)
        ll.insert(1, 2)
        self.assertEqual(repr(ll), "[1, 2, 3]")
        with self.assertRaises(IndexError):
            ll.insert(5, 4)

    def test_reverse(self):
        ll = linkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.reverse()
        self.assertEqual(repr(ll), "[3, 2, 1]")

    def test_getLength(self):
        ll = linkedList()
        ll.add(1)
        ll.add(2)
        ll.add(3)
        self.assertEqual(ll.getLength(), 3)

    def test_isEmpty(self):
        ll = linkedList()
        self.assertTrue(ll.isEmpty())
        ll.add(1)
        self.assertFalse(ll.isEmpty())

    def test_clear(self):
        ll = linkedList()
        ll.add(1)
        ll.add(2)
        ll.clear()
        self.assertEqual(repr(ll), "[]")

if __name__ == "__main__":
    unittest.main()
