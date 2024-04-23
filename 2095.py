"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def __repr__(self):
        itr = self.head
        tList = []
        while itr is not None:
            tList.append(itr.data)
            itr = itr.next
        return str(tList)
    

class Solution:
    def deleteMiddle(self, head):
        if head is None:
            return head
        prev = Node(0)
        prev.next = head
        itr_slow = prev
        itr_fast = head
        while itr_fast is not None and itr_fast.next is not None:
            itr_fast = itr_fast.next.next
            itr_slow = itr_slow.next
        itr_slow.next = itr_slow.next.next
        return prev.next


ll1 = LinkedList()

ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)
# ll1.add(6)

print(ll1)

print(Solution().deleteMiddle(ll1.head))
# [1, 2, 3, 4, 5] --> [1, 2, 4, 5]
# []