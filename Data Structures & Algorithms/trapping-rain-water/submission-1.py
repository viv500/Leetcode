class Solution:
    def trap(self, height: List[int]) -> int:
        # trapped water is defined as the minimum of maximum of heights to the left and right of a cell (excluding itself)
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        

        # left[0] is 0 and right[-1] is 0
        for i in range(1, n):
            max_left[i] = max(height[i - 1], max_left[i - 1])
        
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        water = 0
        for i in range(n):
            level = min(max_left[i], max_right[i]) - height[i]
            if level > 0:
                water += level
        
        return water
