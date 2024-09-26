class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # DP solution (O(n^2))

        # greedy: keep shifting the goal backwards to make the final target simple

        goal = len(nums) - 1 # goal is intially at the end

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal: #nums[i] is the jump length, i is the current position
                goal = i # move the goal back to a closer possible goal

        return goal == 0 # only if we can reach the 0th index, the path is possible

        