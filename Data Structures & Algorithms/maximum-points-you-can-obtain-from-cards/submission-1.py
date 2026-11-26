# O(2^k) time for brute force (depth is atmost k, not n) and O(k) space
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        dp = {}
        def dfs(start, end, taken):
            if (start, end, taken) in dp: return dp[(start, end, taken)]
            if taken == k: return 0

            take_start = cardPoints[start] + dfs(start + 1, end, taken + 1)
            take_end = cardPoints[end] + dfs(start, end - 1, taken + 1)

            dp[(start, end, taken)] = max(take_start, take_end)
            return dp[(start, end, taken)]
        
        return dfs(0, len(cardPoints) - 1, 0)
