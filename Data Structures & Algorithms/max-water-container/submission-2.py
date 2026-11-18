class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        low, high = 0, len(heights) - 1

        while low < high:
            height = min(heights[low], heights[high])
            highest = max((high - low) * height, highest)

            if heights[low] > heights[high]:
                high -= 1
            else:
                low  += 1


        return highest
