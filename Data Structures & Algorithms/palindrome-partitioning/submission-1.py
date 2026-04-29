class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # constraints mention length <= 20
        # O(n) plaindrome check during backtracking is sufficient

        # backtracking pattern 2 (loop + 1 recrusive call) since decision is not binary, it can be one of many
        output = []
        substrings = []

        def backtrack(i):
            if i == len(s):
                output.append(substrings.copy())
                return

            j = i + 1

            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if substring == substring[::-1]:

                    substrings.append(substring)
                    backtrack(j + 1)
                    substrings.pop()

        backtrack(0)

        return output
