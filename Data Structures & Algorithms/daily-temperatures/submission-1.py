class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force is O(n^2)
        # monotonic stack : O(n) time and space
        # its monotonic (specifically, decreasing) cuz you only add elements to the stack if less than the top of stack
        # if you find one thats greater, then keep popping from stack and storing distance to current element for every element
        # thats less than the greater element

        stack = []
        output = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                new_temp, new_index = stack.pop()
                output[new_index] = index - new_index

            stack.append((temp, index)) # append at end (every element needs to get added at least once)

        
        return output
