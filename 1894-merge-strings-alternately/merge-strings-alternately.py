class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""

        total = len(word1 + word2)

        for i in range(total):
            if i < len(word1):
                new += word1[i]
            if i < len(word2):
                new += word2[i]

        return new


        