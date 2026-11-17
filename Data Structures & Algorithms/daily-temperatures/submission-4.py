class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                old_i, _ = stack.pop()
                result[old_i] = i - old_i

            stack.append((i, t))

        return result
