from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(count.items())
        print(nums)
        dp = {}

        def dfs(index, prev):
            if (index, prev) in dp: return dp[(index, prev)]
            if index == len(nums): return 0
            val, count = nums[index]

            skip = dfs(index + 1, prev)
            if val == prev + 1: # cant take
                dp[(index, prev)] = skip
            else:
                take = (val * count) + dfs(index + 1, val)

                dp[(index, prev)] = max(skip, take)

            return dp[(index, prev)]

        return dfs(0, -1)


