class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        L, R = 0, len(height) - 1

        while L < R:
            max_area = max(max_area, (R - L)*min(height[R], height[L]))
            if height[L] < height[R]:
                L +=1
            else:
                R -= 1
        return max_area


        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                max_area = max(max_area, (r - l)*min(height[l], height[r]))

        return max_area    