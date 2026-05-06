class MinStack:
    # to make getMin() O(1), maintain a stack of "current min so far" of the original stack
    # ex: stack = [1, 5, -3, 0, 4, -9, 4, 2]
    # ex: min stack = [1, 1, -3, -3, -9, -9, -9]

    # whenever a main stack element gets popped, pop 1 element from min stack too

    def __init__(self):
        
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        stack = self.stack
        min_stack = self.min_stack

        # append to stack
        stack.append(val)

        # append to min stack
        if not min_stack: 
            min_stack.append(val)
            return
        prev_min = min_stack[-1]
        if val < prev_min:
            min_stack.append(val)
        else:
            min_stack.append(prev_min)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
