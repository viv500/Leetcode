class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(1, numRows + 1):
            result.append([0] * i)
        
        for row in result:
            row[0] = 1
            row[-1] = 1
        
        for i in range(2, len(result)):
            for j in range(1, len(result[i]) - 1):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        
        return result