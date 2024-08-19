class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i+(j%2)*(len(nums)//2)] for i in range(len(nums)//2) for j in range(2) ]