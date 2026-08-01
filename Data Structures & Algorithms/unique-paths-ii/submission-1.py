class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        # change obstacle to -1 so it wont be confused 
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = -1

        obstacleGrid[rows - 1][cols - 1] = 1

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if obstacleGrid[row][col] == -1: continue

                if row + 1 < rows and obstacleGrid[row + 1][col] != -1:
                    obstacleGrid[row][col] += obstacleGrid[row + 1][col]
                if col + 1 < cols and obstacleGrid[row][col + 1] != -1:
                    obstacleGrid[row][col] += obstacleGrid[row][col + 1]

        print(obstacleGrid)
        return obstacleGrid[0][0]
