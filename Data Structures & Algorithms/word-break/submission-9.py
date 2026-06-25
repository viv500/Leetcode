class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(word) <= n - i and word == s[i:i+len(word)]:
                    dp[i] = dp[i + len(word)]

                if dp[i]: break



        return dp[0]
