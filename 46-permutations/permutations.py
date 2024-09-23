class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sols = [], []

        def backtrack():
            if len(res) == n:
                sols.append(res[:])
                return

            for num in nums:
                if num not in res:
                    res.append(num)
                    backtrack()
                    res.pop()

        backtrack()

        return sols
