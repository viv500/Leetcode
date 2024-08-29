class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            small = nums[0]
            small_index = 0
            for i, j in enumerate(nums):
                if j < small:
                    small = j
                    small_index = i
            
            nums[small_index] *= multiplier

            k -=1

        return nums
        