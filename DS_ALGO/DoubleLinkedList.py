class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert(self, prevNode, newdata):
        if prevNode is None:
            return
        
        newNode = Node(newdata)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next is not None:
            newNode.next.prev = newNode
    
    def append(self, newdata):
        newNode = Node(newdata)
        newNode.next = None

        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    
    def listprint(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

dllist = DoubleLinkedList()
#Add element
dllist.push(12)
dllist.push(8)
dllist.push(62)

#Print ELement
dllist.listprint(dllist.head)

#Insert element
dllist.insert(dllist.head.next, 13)

#Append at Last
dllist.append(45)