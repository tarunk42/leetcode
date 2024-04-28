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
    def removeNthFromEnd(self, head, index):
        if head is None:
            return None
        if index == 0:
            head = head.next
        else:
            current = head
            current_index = 0
            while current and current_index < index-1:
                current = current.next
                current_index += 1
            
            if current and current.next:
                current.next = current.next.next
        
        return head
    

ll1 = LinkedList()

ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)

print(ll1)

Solution().removeNthFromEnd(ll1.head, 2)

print(ll1)


