class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index = stack.pop()[0]
                result[index] = i - index

            stack.append((i, t))

        return result

