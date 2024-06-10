class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
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
    
    def deleteNode(self, node):
        # Copy the value of the next node into the current node
        if node.next:
            node.data = node.next.data
            # Skip the next node
            node.next = node.next.next
        else:
            print("Can't delete the last node with this method")
    


ll1 = LinkedList()

ll1.add(1)
ll1.add(2)
ll1.add(3)
ll1.add(4)
ll1.add(5)
ll1.add(6)

print(ll1)

node_to_delete = ll1.head  # This is the node with value 3

ll1.deleteNode(node_to_delete)

# Printing the linked list after deletion
print("Linked List after deletion:", ll1)