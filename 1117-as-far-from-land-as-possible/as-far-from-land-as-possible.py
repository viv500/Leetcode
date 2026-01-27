from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # distance to NEAREST cell is MAXIMIZED
        # i.e. largest distance in bfs shortest path
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        furthest = 0

        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # mark land so that it doesnt get flagged
                    grid[row][col] = -1
                    q.append((row, col))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    if grid[r][c] == -1:
                        grid[nr][nc] = 1
                    else:
                        grid[nr][nc] = grid[r][c] + 1

                    q.append((nr, nc))

            
        for row in range(rows):
            for col in range(cols):
                furthest = max(furthest, grid[row][col])

        print(grid)
        return furthest if furthest != 0 else -1

        