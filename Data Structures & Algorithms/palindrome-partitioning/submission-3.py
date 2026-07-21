class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partition = []
        result = []

        def backtrack(index):
            if index == len(s):
                result.append(partition.copy())
                return

            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if substring == substring[::-1]:
                    partition.append(substring)
                    backtrack(i)
                    partition.pop()


        backtrack(0)
        return result