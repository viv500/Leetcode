class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # n log n
        result = []
        i = 0

        for i in range(len(nums)):
            number = nums[i]
            if number > 0:
                break

            elif (i > 0 and nums[i] == nums[i - 1]):
                continue

            lo = i + 1
            hi = len(nums) - 1

            while lo < hi:
                summ = nums[lo] + nums[i] + nums[hi]

                if summ == 0:
                    result.append([nums[lo], nums[i], nums[hi]])
                    
                    while(lo < hi and nums[lo] == nums[lo + 1]):
                        lo += 1
                        
                    while(lo < hi and nums[hi] == nums[hi - 1]):
                        hi -= 1

                    lo += 1
                    hi -= 1
                elif summ > 0:
                    hi -= 1

                else:
                    lo += 1

        return result

                