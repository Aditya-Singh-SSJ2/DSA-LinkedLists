# data, value - val
# pointer to next node - next
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def traverse(self):
        current = self.head
        while (current!=None):
            print(current.val, end='->')
            current = current.next
    
    def push(self, val): #Append
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
    
    def pushHead(self, val): #Add at the side of head, i.e. front
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self, key=-1):
        if self.head == None:
            return
        
        temp = self.head
        if key == 0:
            self.head = temp.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp
        
        if key>=self.length:
            return
        
        if key==self.length-1 or key==-1: #pop from end
            while (temp.next):
                prev = temp
                temp = temp.next
            prev.next = None
            self.tail = prev        
        else:
            for i in range(key):
                prev = temp
                temp = temp.next
            prev.next = temp.next
        
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp #Popped node

    def get(self, index):
        pass
    def set(self, index, val):
        pass
    def insert(self, index, val):
        pass

#TEST
l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
# l.pop()
# l.pop(0)
l.pushHead(0)
l.pushHead(-1)
l.traverse()