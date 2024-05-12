# Given the head of a singly linked list, reverse the list, and return the reversed list.

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
        tList = []
        if not self.head:
            return tList
        else:
            current = self.head
            while current:
                tList.append(current.data)
                current = current.next
            return str(tList)
    

class Solution:
    def reverseList(self, head):
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        head = previous

        return head  # update the head to the last node encountered
        # # brute force
        # tList = []
        # current = head
        # while current:
        #     tList.append(current.data)
        #     current = current.next
        
        # newList = LinkedList()
        # tList_len = len(tList)
        # for i in range(tList_len):
        #     newList.add(tList.pop())
        
        # head = newList.head

        # return newList
    
    def recursivereverseList(self, head):
        if not head:
            return head
        newHead = head
        if head.next:
            newHead = self.recursivereverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead



ll1 = LinkedList()

for i in range(0,6):
    ll1.add(i)


print(ll1)

soln = Solution()
# new_head = soln.reverseList(ll1.head)
new_rec_head = soln.recursivereverseList(ll1.head)

# ll1.head = new_head


ll1.head = new_rec_head

print(ll1)