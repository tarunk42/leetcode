"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
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
    def removeNthFromEnd(self, head, n):
        # dummy = Node(0)
        # dummy.next = head
        # first = dummy
        # second = dummy

        # for _ in range(n + 1):
        #     first = first.next

        # while first is not None:
        #     first = first.next
        #     second = second.next

        # second.next = second.next.next

        # return dummy.next

        length = 0
        dummy = Node(0)
        dummy.next = head
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        index = length - n
        cur1 = dummy
        while index > 0:
            index -= 1
            cur1 = cur1.next
        cur1.next = cur1.next.next
        return dummy.next
    

ll1 = LinkedList()

ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)

print(ll1)

Solution().removeNthFromEnd(ll1.head, 2)

print(ll1)


