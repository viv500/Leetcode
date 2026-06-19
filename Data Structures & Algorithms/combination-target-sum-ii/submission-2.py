class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def dfs(curSum, index, combination):
            if curSum == target: 
                combinations.append(combination.copy())
                return
                
            if curSum > target or index >= len(candidates): return

            value = candidates[index]
            # take
            dfs(curSum + value, index + 1, combination + [value])

            # dont take (leave out all dupes)
            new_index = index
            while new_index < len(candidates) and candidates[new_index] == value:
                new_index += 1
            
            dfs(curSum, new_index, combination)

        dfs(0, 0, [])
        return combinations