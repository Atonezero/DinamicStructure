class Node:
    def __init__(self, valore):
        self.valore = valore
        self.next = None

class CircularBuffer:
    def __init__(self, size):
        self.head = None
        self.coda = None
        self.count = 0
        self.size = size

    def put(self, valore):
        newNode = Node(valore)
        if self.count == self.size:
            return None
        if self.count == 0:
            self.head = newNode
            self.coda = newNode
            newNode.next = newNode
            self.count += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
        
        self.count += 1;

    def get(self):
        if self.count > 0:
    
