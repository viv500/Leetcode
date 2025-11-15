class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # brute force: for each item -> search entire array for consecutive elements
        #(O(n^2))

        # longest = 0

        # for num in nums:
            # length = 1
            # current = num

            # while current + 1 in nums:
                # current += 1
                # length += 1
            
            # longest = max(longest, length)

        # return longest


        # slighty better: sort and then 2 pointer (nlogn)

        nums.sort()

        if not nums:
            return 0

        longest = 0
        current = 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue

            if nums[i - 1] + 1 == nums[i]:
                current += 1
            
            else:
                longest = max(longest, current)
                current = 1 # resent current

        
        return max(longest, current)

