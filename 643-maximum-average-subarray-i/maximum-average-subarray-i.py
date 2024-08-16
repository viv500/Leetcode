class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # edge case
        if not nums:
            return 0
        
        # trivial case
        if len(nums) == k:
            return sum(nums) / k

        # sliding window

        a = 0
        b = k - 1

        cur_sum = sum(nums[a:b + 1])

        # cant initialize as 0 cuz the actual max couuld be negative
        current_max = cur_sum/k

        length = len(nums)

        while b < length - 1:
            cur_sum = cur_sum + nums[b + 1] - nums[a]
            current_max = max(current_max, cur_sum /k)

            b += 1
            a += 1


        return current_max


        ''' not the most efficient cuz we calculated sum individuall at each stage
        we can instead subtract and add the new and old values coming into the window

        while b < length:
            current_max = max(current_max, sum(nums[a:b + 1])/k)
            b += 1
            a += 1
'''


        