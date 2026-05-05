class Solution:
    # brute force: nested loop O(n^2)
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(heights) - 1

        # greedily move the bar with the shorter height

        # this is cuz the shorter bar is the bottleneck.
        # if we move the taller bar
        #   1. the width reduces
        #   2. the shorter bar still decides the volume
        # we are GUARENTEED that moving the taller bar will ALWAYS hurt. 
        # and also GUARENTEED that the pair we found with the shorter bar is the OPTIMAL PAIR that includes the shorter bar (most wdith)

        # since moving the taller bar always hurts, move the shorter bar

        while left < right:
            min_height = min(heights[left], heights[right])
            max_volume = max(max_volume, min_height * (right - left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_volume
