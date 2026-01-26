from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1: return -1
        if grid == [[0]]: return 1
       
        q = deque([(0, 0)])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    if (nr, nc) == (rows - 1, cols - 1): 
                        return grid[r][c] + 2

                    # no need to commpare shortest distance since if grid[nr][nc] = 0, then this IS the
                    # shortest path to this cell (bfs)
                    
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

        return -1





    
