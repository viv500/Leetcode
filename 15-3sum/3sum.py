from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Skip the same value to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            p1, p2 = i + 1, len(nums) - 1
            
            while p1 < p2:
                total = nums[i] + nums[p1] + nums[p2]
                if total == 0:
                    sols.append([nums[i], nums[p1], nums[p2]])
                    # Skip duplicates
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                    p1 += 1
                    p2 -= 1
                elif total < 0:
                    p1 += 1
                else:
                    p2 -= 1
        
        return sols
