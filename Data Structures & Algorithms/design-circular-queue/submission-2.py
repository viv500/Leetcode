class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.size = k
        self.count = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.count += 1
        self.rear = (self.rear + 1) % self.size

        self.q[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.count -= 1
        self.front = (self.front + 1) % self.size 

        return True
        

    def Front(self) -> int:
        return self.q[self.front] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        return self.q[self.rear] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()