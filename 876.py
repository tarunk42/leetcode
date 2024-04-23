"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = newNode
    
    # def getListLength(self):
    #     count = 0
    #     current = self.head
    #     while current is not None:
    #         count += 1
    #         current = current.next
    #     return count
    
    def __repr__(self) -> str:
        itr = self.head
        temp_list = []
        while itr is not None:
            temp_list.append(itr.data)
            itr = itr.next
        return str(temp_list)

# class Solution:
#     def middleNode(self, head):
#         count = 0
#         temp_list = []
#         if head is None:
#             return None
#         else:
#             while head is not None:
#                 temp_list.append(head.data)
#                 count += 1
#                 head = head.next
#         temp_list = temp_list[count//2:]
#         return temp_list

# class Solution:
#     def middleNode(self, head):
#         count = 0
#         t_head = head
#         while head is not None:
#             count += 1
#             head = head.next
#         # temp = Node(None)
#         for i in range(count//2):
#             t_head = t_head.next
#         return t_head

class Solution:
    def middleNode(self, head):
        if head is None:
            return head
        itr_slow = head
        itr_fast = head
        while itr_fast is not None and itr_fast.next is not None:
            itr_fast = itr_fast.next.next
            itr_slow = itr_slow.next
        return itr_slow





ll1 = LinkedList()
ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)
ll1.add(6)
print(ll1)
# print(ll1.getListLength())


print(Solution().middleNode(ll1.head))

