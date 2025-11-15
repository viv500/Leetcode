from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # level by level processing the oranges
        # modify grid (part of the problem) don't need to use visited

        EMPTY = 0
        ORANGE = 1
        ROTTEN_ORANGE = 2

        rotten = deque()
        time = 0
        fresh_count = 0  # FIX: Track fresh oranges to check if all rot

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN_ORANGE:
                    rotten.append((r, c))
                elif grid[r][c] == ORANGE:  # Count fresh oranges
                    fresh_count += 1
        
        # FIX: Only process if there are fresh oranges and rotten oranges to spread
        while(rotten and fresh_count > 0):
            oranges_this_level = len(rotten)

            for _ in range(oranges_this_level):
                rot = rotten.popleft()

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for row, col in directions:
                    nr, nc = row + rot[0], col + rot[1]

                    # FIX: Check grid value directly, not if coordinates in visited
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ORANGE:
                        rotten.append((nr, nc))
                        grid[nr][nc] = ROTTEN_ORANGE
                        fresh_count -= 1  # FIX: Decrease fresh count

            time += 1

        # FIX: Return -1 if there are still fresh oranges that couldn't be reached
        return -1 if fresh_count > 0 else time