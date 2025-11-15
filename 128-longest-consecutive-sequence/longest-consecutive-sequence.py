class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # idea: set() uses O(1) loop. confirm an element must be a starting element of a sequence before expanding. only 1 element will expand
        # may look like O(n^2) but each element is visited exactly once! the inner loop runns for a sequence of element which will never be visited agiab
        # this is because the inner loop only accesses all consecutive elements within the sequence. if a number isnt a part of this sequence, it will never viist   these again

        num_set = set(nums) # O(n)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set: # can be starting element
                length = 1
                cur = num
                while cur + 1 in num_set:
                    length += 1
                    cur += 1
                
                longest = max(longest, length)

        return longest



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

        # nums.sort()

        # if not nums:
            # return 0

        # longest = 0
        # current = 1
        
        # for i in range(1, len(nums)):
            # if nums[i - 1] == nums[i]:
                # continue

            # if nums[i - 1] + 1 == nums[i]:
                # current += 1
            
            # else:
                # longest = max(longest, current)
                # current = 1 # resent current

        
        # return max(longest, current)

