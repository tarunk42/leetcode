"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        newNode = Node(val)

        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = newNode

    def __repr__(self):
        itr = self.head
        tList = []
        while itr:
            tList.append(itr.data)
            itr = itr.next
        return str(tList)

class Solution:
    def swapNodes(self, head, k: int):
        dummy = Node(0)
        

ll1 = LinkedList()

ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)
ll1.add(6)

print(ll1)