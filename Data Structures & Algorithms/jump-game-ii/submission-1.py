class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy BFS-like
        # !! NOTE !! a solution is guarenteed
        # at each "bfs level" calculate the min and max range you can jump to from any element in that level
        jumps = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, nums[i])
            
            left = right + 1 # no point in exploring an element from current bfs level - this allows the alg to be O(n)
            right = right + farthest

            jumps += 1
        
        return jumps

        # brute force
        min_jumps = float("inf")
        def dfs(index, jumps):
            nonlocal min_jumps
            if index == len(nums) - 1:
                min_jumps = min(min_jumps, jumps)

            for i in range(1, nums[index] + 1):
                if index + i < len(nums):
                    dfs(index + i, jumps + 1)

        dfs(0, 0)

        return min_jumps