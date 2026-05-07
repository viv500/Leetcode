class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }


        output = []
        combination = []
        def backtrack(index):
            if index == len(digits):
                output.append(combination.copy())
                return

            number = int(digits[index])
            for char in mapping[number]:
                combination.append(char)
                backtrack(index + 1)
                combination.pop()

        backtrack(0)
        return [''.join(word) for word in output]