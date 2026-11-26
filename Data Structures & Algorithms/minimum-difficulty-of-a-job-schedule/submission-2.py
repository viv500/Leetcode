class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        j = jobDifficulty
        if len(j) < d: return -1

        dp = {}

        def dfs(index, days_left):
            if (index, days_left) in dp: return dp[(index, days_left)]
            if index == len(j): return 0 if days_left == 0 else float("inf")

            # impossible branch, prune
            if days_left == 0 or len(j) - index < days_left: return float("inf")

            # further pruning: last day
            if days_left == 1: return max(j[index:])

            current_max, best = 0, float("inf")

            for i in range(index, len(j)):
                current_max = max(current_max, j[i])
                best = min(best, current_max + dfs(i + 1, days_left - 1))

            dp[(index, days_left)] = best
            return best

        return dfs(0, d)