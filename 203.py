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
    
    def deleteNodebyIndex(self, index):
        if self.head is None:
            return None
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            current_index = 0
            while current and current_index < index-1:
                current = current.next
                current_index += 1
            
            if current and current.next:
                current.next = current.next.next


    def __repr__(self):
        itr = self.head
        tList = []
        while itr:
            tList.append(itr.data)
            itr = itr.next
        return str(tList)
    
# class Solution:
#     def removeElements(self, linkedlist, val):
#         # if head is None:
#         #     return head
#         # else:
#         #     current = head
#         #     while head and head.data == val:
#         #         head = head.next
#         #     while current and current.next:
#         #         if current.next.data == val:
#         #             current.next = current.next.next
#         #         else:
#         #             current = current.next
#         #     return head
#         dummy = Node()
#         fast = slow = dummy
#         dummy.next = linkedlist.head
#         fast = fast.next
#         while fast:
#             if fast.data == val:                
#                 slow.next = slow.next.next      
#             else:
#                 slow = fast                    
#             fast = fast.next                   
#         return dummy.next
"""
The issue with the code is that the `removeElements` method is not correctly updating the head of the LinkedList. 
It creates a new dummy node and assigns it to the head of the LinkedList, but it does not update the head of the LinkedList itself.
"""

# class Solution:
#     def removeElements(self, linkedlist, val):
#         dummy = Node()
#         dummy.next = linkedlist.head
#         current = dummy
#         while current.next:
#             if current.next.data == val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         linkedlist.head = dummy.next

class Solution:
    def removeElements(self, linkedlist, val):
        dummy = Node()
        fast = slow = dummy
        dummy.next = linkedlist.head
        fast = fast.next
        while fast:
            if fast.data == val:                
                slow.next = slow.next.next      
            else:
                slow = fast                    
            fast = fast.next                   
        linkedlist.head = dummy.next
        return linkedlist
        

ll1 = LinkedList()

ll1.add(1)
ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)

print(ll1)

# ll1.deleteNodebyIndex(1)

Solution().removeElements(ll1, 1)

print(ll1)

