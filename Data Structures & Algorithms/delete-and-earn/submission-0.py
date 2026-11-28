from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(count.items())
        print(nums)

        def dfs(index, prev):
            if index == len(nums): return 0
            val, count = nums[index]

            if val == prev + 1: # cant take
                return dfs(index + 1, prev)
            else:
                skip = dfs(index + 1, prev)
                take = (val * count) + dfs(index + 1, val)

                return max(skip, take)

        return dfs(0, -1)


