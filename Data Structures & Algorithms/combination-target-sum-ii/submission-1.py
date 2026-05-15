class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # combination sum 1: can use numbers as many times as needed
        # combination sum 2: input array has dupes but each number can only be used once

        # changes -> sort input array so dupes are adjacent

        # INTUITION! -> if we choose to skip a number, never consider it again! it will create dupes
        # if we find a dupe, skip all dupe indices and then recurse in the "skip branch"
        # this will help avoid "duplicate results" ex target = 7, input = [1, 1, 6] => [[1, 6], [1, 6]]
        candidates.sort()

        output = []
        combination = []

        def dfs(i, summ):
            # check this before the base case below so the last element isn't skipped
            if summ == target:
                output.append(combination.copy())
                return

            if summ > target or i >= len(candidates): return

            number = candidates[i]

            # take branch
            combination.append(number)
            dfs(i + 1, summ + number)

            # skip branch
            combination.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, summ)

        dfs(0, 0)

        return output 