class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        total_water = 0

        for i in range(1, len(height)):
            left[i] = max(height[i - 1], left[i - 1])

        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])


        for i in range(len(height)):
            min_height = min(left[i], right[i])

            if min_height > height[i]:
                total_water += min_height - height[i]

        return total_water        