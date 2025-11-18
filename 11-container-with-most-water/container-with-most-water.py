class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_volume = 0

        # 2 pointer approach, start with maxmimal width: O(n)
        # if 1 side is bigger, move other side
        # greedy strategy!! 
        # explanation: if you move the larger side, the smaller side continues to be bottleneck, but with smaller width -> area goes down!
        # if you move smaller side, width might decrease but theres we're getting rid of the bottleneck, in hopes of finding a better height
        
        L, R = 0, len(height) - 1

        while L < R:
            max_volume = max(max_volume, (R - L) * min(height[R], height[L]))
            if height[R] > height[L]:
                L += 1
            else:
                R -= 1

        return max_volume

        # brute force

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_volume = max(max_volume, (j - i) * min(height[i], height[j]))

        return max_volume