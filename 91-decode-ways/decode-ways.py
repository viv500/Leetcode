class Solution:
    def numDecodings(self, s: str) -> int:
        # dp
        # at an index i, we can either split by 0...i - 1 | i or 0 ... i - 2 | i - 1, i
        # we need to check if each way is valid, and if so, add to total number of ways
        # time: O(n)

        if s[0] == "0": return 0
        if len(s) == 1: return 1

        dp = [0] * len(s)
        dp[0] = 1

        if s[1] != "0":
            dp[1] += dp[0]
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1


        for i in range(2, len(s)):
            if s[i] != "0":
                dp[i] += dp[i - 1]

            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i - 2]


        print(dp)
        return dp[len(s) - 1]

        