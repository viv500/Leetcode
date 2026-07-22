class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        result = []
        perm = []
        
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    perm.append(nums[i])

                    backtrack()

                    used.remove(nums[i])
                    perm.pop()

        backtrack()
        return result