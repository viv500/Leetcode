# time is : 4^n leaves. and at each leaf you construct a string of length n
# run time: O(n * 4^n)
# space time: O(n) auxiliary space (tree height) or O(n * 4^n) total space (output array)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        result = []
        path = []

        # O(26) space
        n_to_c = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def backtrack(index):
            if index == len(digits):
                result.append("".join(path))
                return

            for char in n_to_c[int(digits[index])]:
                path.append(char)
                backtrack(index + 1)
                path.pop()

        backtrack(0)

        return result

            