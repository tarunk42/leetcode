# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
#  The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node
    
    def __repr__(self):
        itr = self.head
        temp_list = []
        while itr is not None:
            temp_list.append(itr.data)
            itr = itr.next
        return str(temp_list)

ll1 = LinkedList()
ll1.add(1)
ll1.add(0)
ll1.add(1)
print(ll1)

print(ll1.head.next.data)

class Solution:
    def getDecimalValue(self, head):
        result = 0
        if head.data is None:
            return None
        else:
            while head is not None:     
                result = 2*(result)+head.data
                head = head.next
        
        return result


print(Solution().getDecimalValue(ll1.head))

   

# [1011]- lenght n binary no. - digit_n *2^n + digit_n-1*2^n-1


# 2*1
# 2*(2*1+0)
# 1*2^2 + 0*2^1 + 1*2^0
# 1*2*2+0*2+1


# 2*0+1

# 2*(1)+0

# 2*((2*1)+0)+1


# 1011
# 2*(0)+1                 - 1
# 2*(1) + 0         - 2
# 2*(2) + 1           - 5
# 2*(5) + 1           - 11

        
        