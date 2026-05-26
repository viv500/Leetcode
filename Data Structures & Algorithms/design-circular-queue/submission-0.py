# "space in front"
# [_, _, 30, 50, _]
# after the first 2 are dequeued, a linear queue will point to 30 and not realiz theres more space infront

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [-1] * k
        self.front, self.rear = 0, (k - 1)
        self.element_count = 0

    def enQueue(self, value: int) -> bool:
        if self.element_count == self.capacity:
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
    
        self.element_count += 1
        return True

    
    def deQueue(self) -> bool:
        if self.element_count == 0:
            return False

        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.capacity
        
        self.element_count -= 1
        return True
        

    def Front(self) -> int:
        return self.queue[self.front]      

    def Rear(self) -> int:
        return self.queue[self.rear]
        
    def isEmpty(self) -> bool:
        return not self.element_count

    def isFull(self) -> bool:
        return self.element_count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()