class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # idea : array of max value seen the the left for each value (excluding self)
        # array of max value seen the the right for each value (excluding self)
        # potential water for each spot = min(max l value, max r value)
        # actual water = potential water - height
        # if actual < 0: actual = 0

        left_array = []
        right_array = []
        
        max_left = 0
        max_right = 0

        for h in range(len(height)):
            left_array.append(max_left)
            max_left = max(max_left, height[h])

        for h in range(len(height) - 1, -1, -1):
            right_array.append(max_right)
            max_right = max(max_right, height[h])

        right_array.reverse()

        sum = 0
        for i in range(len(left_array)):
            sum += max(0, min(left_array[i], right_array[i]) - height[i]) # avoids negatives

        return sum
        
        print(right_array)

