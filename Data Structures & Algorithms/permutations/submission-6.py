class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result = []
        perm = []
        
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return

            for n in nums:
                if n not in seen:
                    seen.add(n)
                    perm.append(n)

                    backtrack()

                    seen.remove(n)
                    perm.pop()


        backtrack()
        return result