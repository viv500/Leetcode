class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # "match" - no moves, advance both pointers once
        # "delete" - advance i pointer once, dont advance j +1 move
        # "insert" - advance j pointer once, dont advance i +1 move
        # "replace" - advance both pointers, +1 move

        dp = {}

        def compare(i, j):
            if i == len(word1) and j == len(word2): return 0
            if i == len(word1): return len(word2) - j
            if j == len(word2): return len(word1) - i

            if (i, j) in dp: return dp[(i, j)]
            match = float("inf")
            if word1[i] == word2[j]:
                match = compare(i + 1, j + 1)
            
            delete = 1 + compare(i + 1, j)
            insert = 1 + compare(i, j + 1)
            replace = 1 + compare(i + 1, j + 1)

            dp[(i, j)] = min(match, delete, insert, replace)
            return dp[(i, j)]

        return compare(0, 0)
            
