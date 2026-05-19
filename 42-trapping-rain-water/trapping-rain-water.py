class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        trapped_water = 0

        for i in range(len(height)):
            max_water_level = min(max_left[i], max_right[i])
            if height[i] < max_water_level:
                trapped_water += max_water_level - height[i]

        return trapped_water