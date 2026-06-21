class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def ispalindrome(s):
            return s == s[::-1]

        output = []
        partition = []

        def backtrack(index_from):
            if index_from >= len(s):
                output.append(partition.copy())
                return

            for index_to in range(index_from, len(s)):
                substring = s[index_from:index_to + 1]
                if ispalindrome(substring):

                    partition.append(substring)
                    backtrack(index_to + 1)
                    partition.pop()
        
        backtrack(0)
        return output