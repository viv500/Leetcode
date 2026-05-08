from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # "minimum minutes" -> has to be BFS
        # "spread at the same time" needs to be level order with time tracking
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        freshOrangeCount = 0
        time = 0

        rotten_oranges = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))
                elif grid[row][col] == 1:
                    freshOrangeCount += 1

        
        while rotten_oranges and freshOrangeCount > 0: # accounts for when theres still rotten oranges but no more fresh fruits to spoil, timer should stop
            size = len(rotten_oranges)

            for _ in range(size):
                row, col = rotten_oranges.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        freshOrangeCount -= 1 # 1 less fresh orange
                        grid[nr][nc] = 2 # mark it rotten
                        rotten_oranges.append((nr, nc))         
           
            time += 1   # time is incremented after each level in bfs

        return -1 if freshOrangeCount > 0 else time # if not everything was rotten

