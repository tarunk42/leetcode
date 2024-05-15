class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class linkedList:
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

    def contains(self, val):
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False
    
    def delete(self, val):
        current = self.head
        previous = None
        while current:
            if current.data == val:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
            previous = current
            current = current.next
    
    def insert(self, index, val):
        newNode = Node(val)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        current = self.head
        count = 0
        previous = None
        while current and count < index:
            previous = current
            current = current.next
            count += 1
        
        if count == index:
            previous.next = newNode
            newNode.next = current
        else:
            raise IndexError("Index out of bounds")
    
    def reverse(self):
        previous = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        self.head = previous
    
    def getLength(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def isEmpty(self):
        return self.head is None
    
    def clear(self):
        self.head = None


    def __repr__(self):
        tList = []
        if not self.head:
            return str(tList)
        else:
            current = self.head
            while current:
                tList.append(current.data)
                current = current.next
            return str(tList)


ll1 = linkedList()
print(ll1)
for i in range(0,4):
    ll1.add(i)

print(ll1)
ll1.delete(1)
print(ll1)
print(ll1.getLength())
print(ll1.contains(2))
print(ll1.isEmpty())
ll1.clear()
print(ll1)