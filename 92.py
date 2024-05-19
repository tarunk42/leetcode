# Reverse a Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.

from linkedlist.linkedlist import LinkedList

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = LinkedList.Node()
        dummy.next = head
        previous = dummy

        for _ in range(left):
            previous = previous.next

        current = previous.next
        next_node = None

        for i in range(right-left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = previous.next
            previous.next = next_node
        
        return dummy.next
    

ll1 = LinkedList.linkedList()
for i in range(1,7):
    ll1.add(i)
print(ll1)

print(ll1)

soln = Solution()
# new_head = soln.reverseList(ll1.head)
new_head = soln.reverseBetween(ll1.head, 1, 4)

ll1.head = new_head

print(ll1)

