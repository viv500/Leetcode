class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [num for num in range(1, n + 1)]
        if k > n: return []

        output = []
        combination = []
        
        def backtrack(index):
            if len(combination) == k:
                output.append(combination.copy())
                return

            if index == n: return

            # take branch
            combination.append(numbers[index])
            backtrack(index + 1)

            # leave branch
            combination.pop()
            backtrack(index + 1)

        backtrack(0)
        return output
