class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[n] = number of ways to decode string upto index n
        # if a b c d n , then dp[n] = dp[a b c | d n] + dp[a b c d | n] (if dn is <= 26)
        if s[0] == "0": return 0
        if len(s) == 1: return 1

        dp = [0] * len(s)
        dp[0] = 1
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1
        if int(s[1]) > 0:
            dp[1] += 1

        for i in range(2, len(s)):
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]
            if int(s[i]) > 0: 
                dp[i] += dp[i - 1]

        return dp[len(s) - 1]

