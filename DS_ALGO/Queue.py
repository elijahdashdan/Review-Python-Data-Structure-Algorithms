#FIFO

class Queue:
    def __init__(self) -> None:
        self.queue = list()

    def addtoQ(self, data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        return False
    
    def removefromQ(self):
        if len(self.queue)>0:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

TheQueue = Queue()
TheQueue.addtoQ("Mon")
TheQueue.addtoQ("Tue")
TheQueue.addtoQ("Wed")
print(TheQueue.size())
print(TheQueue.removefromQ())