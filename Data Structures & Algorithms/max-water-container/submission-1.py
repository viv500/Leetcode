class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low, high = 0, len(heights) - 1
        max_water = 0

        while low < high:
            max_water = max(max_water, min(heights[low], heights[high]) * (high - low) )

            if heights[low] >= heights[high]: high -= 1
            else: low += 1

        return max_water
