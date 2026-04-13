class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up dp where the relation is dp[i] = dp[i + len(word that fits)]
        # the array is 1 index longer than s to accomodate a "True" base case

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): # bottom up so starting from the
            for word in wordDict:
                # condition to see if we have enough characters at the end
                if i + len(word) <= len(s) and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]

                # if its a match, we can break and stop searching for words
                if dp[i]:
                    break

        return dp[0]