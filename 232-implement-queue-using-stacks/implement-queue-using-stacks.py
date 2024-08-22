
class MyQueue:

    def __init__(self):
        self.length = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        self.length += 1
        self.stack.append(x)
        

    def pop(self) -> int:
        popped = self.stack[0]
        self.stack = self.stack[1:]
        self.length -= 1
        
        return popped
        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return self.length == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()