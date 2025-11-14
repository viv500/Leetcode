class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_volume = 0

        L = 0
        R = len(height) - 1

        while L < R:
            Left = height[L]
            Right = height[R]
            max_volume = max(max_volume, min(Left, Right) * (R - L))

            if Left <= Right:
                L += 1
            else:
                R -= 1

        
        return max_volume



        
        # brute force : try all pairs of lines and volume = distance bw * min height of both lines

        # for i in range(len(height)):
            # for j in range(i, len(height)):
                # max_volume = max(max_volume, min(height[i], height[j]) * (j - i))

        # return max_volume