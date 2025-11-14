class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        nums.sort() # required to avoid duplicates

        # brute force
        triplets = []

        for fixed in range(len(nums) - 2):
            complements = set() # need a new complement for each iteration
            num = nums[fixed]

            for i in range(fixed + 1, len(nums)):
                complement = -(num + nums[i])
                new = [nums[i], complement, num]
                if complement in complements and new not in triplets:
                    triplets.append(new)
                else:
                    complements.add(nums[i])

        return triplets


        # for i in range(len(nums)):
            # for j in range(i + 1, len(nums)):
                # for k in range(j + 1, len(nums)):
                    # if nums[i] + nums[j] + nums[k] == 0:
                        # triplets.append([nums[i], nums[j], nums[k]])


        return triplets