class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        result = []
        path = []
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

            