from node import node

class list:
    def __init__(self):
        self.head = None

    def append(self, valore):
        new_node = node(valore)
        if not self.head:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
        tmp.next = new_node
    
    def add(self, valore):
        new_node = node(valore)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            

    def remove(self, valore):
        new_node = self.find(valore)


    def find(self, valore):
        new_node = node(valore)
        if not node:
            raise print("node pointer None")
        tmp = new_node
        check = self.head
        while tmp:
            if check == tmp:
                return check
            else:
                return None

    def contains(self, valore):
        new_node = node(valore)
        if not node:
            raise print("node pointer None")
        tmp = new_node
        check = self.head
        while tmp:
            if check == tmp:
                return True
            else:
                return False
            
    def toString():
