#Deque
class Deque(object):
    def __init__(self, limit = 10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # check if queue is empty
    def isEmpty(self):
        return len(self.queue) <= 0

    # check if queue is full
    def isFull(self):
        return len(self.queue) >= self.limit

    # for inserting at rear
    def insertRear(self, data):
        if self.isFull():
            return
        else:
            self.queue.insert(0, data)

    # for inserting at front end
    def insertFront(self, data):
        if self.isFull():
            return
        else:
            self.queue.append(data)

    # deleting from rear end
    def deleteRear(self):
        if self.isEmpty():
            return
        else:
            return self.queue.pop(0)

    # deleting from front end
    def deleteFront(self):
        if self.isFull():
            return
        else:
            return self.queue.pop()

if __name__ == '__main__':
    myDeque = Deque()
    myDeque.insertFront(6)    # 6
    myDeque.insertRear(9)     # 9 6
    myDeque.insertFront(3)    # 9 6 3
    myDeque.insertRear(12)    #12 9 6 3
    print(myDeque)
    myDeque.deleteRear()      # 9 6 3
    print(myDeque)
    myDeque.deleteFront()     # 9 6
    print(myDeque)
