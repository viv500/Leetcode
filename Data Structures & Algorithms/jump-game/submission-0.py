class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # recursively checking each path is an exponential solution
        # constantly updating the goal looks like a nested o(n^2) for loop, but since we keep moving the goal back,
        # it actually is O(n)

        goal = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            distance = goal - i
            max_jump = nums[i]
            # possible to get there?
            if distance <= max_jump:
                goal = i


        return goal == 0