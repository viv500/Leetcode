class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brute force, iterate through every word in wordDict and try matchnig with s until we get to end

        # why is dp useful here?
        # if at some point we figured out that the word cannot be broken down further from a certain index, we wan't to
        # reuse that result for future checks -> elimates repeated work

        dp = [False] * (len(s) + 1)
        # base case
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

                # this needs to be done since we already found A word that makes dp[i] True
                # we dont want to overwrite it with a word that makes it false
                if dp[i]:
                    break
        print(dp)
        return dp[0]

        # brute force: worst case O(2^n)
        def canBreak(index):

            if index == len(s): return True

            for word in wordDict:
                if s[index : index + len(word)] == word:
                    if canBreak(index + len(word)): return True

            return False

        return canBreak(0)
        