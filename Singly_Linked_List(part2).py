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
        print()
    
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
        if index<0 or index>=self.length:
            return IndexError
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set(self, index, val):
        node = self.get(index)
        node.val = val

    def insert(self, index, val):
        if index<0 or index>self.length:
            return IndexError
        elif index==0:
            self.pushHead(val)
        elif index==self.length:
            self.push(val)
        else:
            newNode = Node(val)
            temp = self.head
            prev = temp
            for i in range(index):
                prev = temp
                temp = temp.next
            newNode.next = temp
            prev.next = newNode
        self.length += 1

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
print(l.get(2).val)
l.set(2, 100)
print(l.get(2).val)
l.insert(2, 99)
l.traverse()