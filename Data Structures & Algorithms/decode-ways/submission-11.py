class Solution:
    def numDecodings(self, s: str) -> int:
        # starts with 0 is impossible
        if not s or s[0] == "0": return 0
        if len(s) == 1: return 1

        # always potentially 2 ways of decoding
        # 1. if abcde -> abcde+f only possible if f isnt 0
        # 2. if abcde -> abcd+ef only possible if ef is >= 10 and <= 26

        dp = [0] * len(s)
        dp[0] = 1

        if s[1] != "0": dp[1] += 1
        if 10 <= int(s[0:2]) <= 26: dp[1] += 1


        for i in range(2, len(s)):
            if s[i] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26: 
                dp[i] += dp[i - 2]

        print(dp)
        return dp[len(s) - 1]       