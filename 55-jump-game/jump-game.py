class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # approach: greedy
        # time: O(n)
        # space: O(1)
        # intuition: dynamically change our target if we know that a target can get to n - 1
        # can reach if our target eventually reaches 0

        n = len(nums)
        target = n - 1

        for i in range(n - 1, -1, -1):
            max_jump = nums[i]
            # >= target implies we can reach our target
            if i + nums[i] >= target:
                target = i

        return target == 0

        # approach: top down DP (memoization)
        # time: (O(n)^2)
        # space: O(n) for recursive call stack

        n = len(nums)
        memo = {n - 1: True}
        # starting from index i, can i reach the last index?
        def canReach(i):
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i] + 1):
                if canReach(i + jump):
                    memo[i + jump] = True
                    return True

            memo[i] = False
            return False

        return canReach(0)

        # approach: recursive
        # time: (O(max nums)^n)
        # space: O(n) for recursive call stack

        n = len(nums)
        # starting from index i, can i reach the last index?
        def canReach(i):
            if i == n - 1:
                return True

            for jump in range(1, nums[i] + 1):
                if canReach(i + jump):
                    return True

            return False

        return canReach(0)