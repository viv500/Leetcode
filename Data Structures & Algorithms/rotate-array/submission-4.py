class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 0. mod k
        # 1. reverse array
        # 2. reverse first k elements
        # 3. reverse remaining element

        k = k % len(nums)

        def reverse(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1


        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)

    
        