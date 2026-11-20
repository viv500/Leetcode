class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            a = nums[i]
            if a > 0 or (i > 0 and nums[i] == nums[i - 1]): continue

            hi = len(nums) - 1
            lo = i + 1

            while hi > lo:
                b, c = nums[hi], nums[lo]
                summ = a + b + c

                if summ == 0:
                    result.append([a, b, c])
                    
                    # remove dups
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1

                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    
                    lo += 1
                    hi -= 1

                elif summ > 0:
                    hi -= 1
                else: lo += 1

        return result