class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_right = 0
        left = [0] * len(height)
        right = [0] * len(height)
        summ = 0

        for i in range(len(height)):
            left[i] = max_left
            max_left = max(max_left, height[i])

        for i in range(len(height) - 1, -1, -1):
            right[i] = max_right
            max_right = max(max_right, height[i])

        for i in range(len(height)):
            summ += max(0, min(left[i], right[i]) - height[i])

        return summ
        