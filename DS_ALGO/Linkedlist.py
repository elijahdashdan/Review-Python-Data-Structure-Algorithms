class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class SLinkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    def insertBeg(self, newdata):
        newNode = Node(newdata)

        newNode.next = self.head
        self.head = newNode
    
    def insertEnd(self,newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        
        lastElement = self.head
        while lastElement.next:
            lastElement = lastElement.next
        lastElement.next = newNode
        
    def insertBet(self, middleNode, newData):
        if middleNode is None:
            print("No node")
            return
        
        newNode = self.head
        newNode.next = middleNode.next
        middleNode.next = newNode

    def remove(self, Removekey):
        head = self.head
         
        if (head is not None):
            if (head.data == Removekey):
                self.head = head.next
                head = None
                return
        while (head is not None):
            if head.data == Removekey:
                break
            prev = head
            head = head.next

        if (head == None):
            return

        prev.next = head.next
        head = None


list = SLinkedlist()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link Node 2 to 1
list.head.next = e2
#Link Node 3 to 2
e2.next = e3

#Print All nodes
list.listprint()

#Insert at Start
list.insertBeg("Sun")
list.listprint()

#Insert at End
list.insertEnd("Thu")
list.listprint()

#Insert between
list.insertBet(list.head.next,"Fri")