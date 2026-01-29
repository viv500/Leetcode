from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()

        # Step 1: DFS to find first island, mark as 2, add all cells to BFS queue
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1):
                return

            grid[r][c] = 2  # mark as island 1
            q.append((r, c))  # seed for BFS

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Find any cell of first island and DFS from it
        found = False
        for row in range(rows):
            if found: break
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break

        # Step 2: BFS outward from island 1 until we hit island 2
        steps = 0
        while q:
            level_size = len(q)

            for _ in range(level_size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            # reached island 2!
                            return steps
                        if grid[nr][nc] == 0:
                            # expand into water
                            grid[nr][nc] = 2
                            q.append((nr, nc))

            steps += 1

        return -1

# Time: O(m * n)
# Space: O(m * n) - queue in worst case