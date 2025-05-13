from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        risultato = ""
        tmp = self.head
        while tmp:
            risultato += str(tmp.valore) + " -> "
            tmp = tmp.next
        risultato += "None"
        return risultato

    def append(self, valore):
        new_node = Node(valore)
        if not self.head:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node

    def add(self, valore):
        new_node = Node(valore)
        new_node.next = self.head
        self.head = new_node

    def remove(self, valore):
        if not self.head:
            raise ValueError("Lista vuota")
        if self.head.valore == valore:
            self.head = self.head.next
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.valore == valore:
                prev.next = curr.next
            prev = curr
            curr = curr.next
        raise ValueError("Valore non trovato")

    def find(self, valore):
        tmp = self.head
        while tmp:
            if tmp.valore == valore:
                return tmp
            tmp = tmp.next
        return None

    def modify(self, old_valore, new_valore):
        old_node = self.find(old_valore)
        old_node.valore = new_valore
    
    def contains(self, valore):
        return True if self.find(valore) is not None else False

