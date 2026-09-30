class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        used = set()
        result = []

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            for i, n in enumerate(nums):
                if n not in used:
                    used.add(n)
                    permutation.append(n)

                    backtrack()

                    used.remove(n)
                    permutation.pop()

                
        backtrack()
        return result